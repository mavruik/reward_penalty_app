import json
import pytest
import data_manager


@pytest.fixture(autouse=True)
def redirect_data_file(tmp_path, monkeypatch):
    monkeypatch.setattr(data_manager, "DATA_FILE", str(tmp_path / "team_data.json"))


def empty_data():
    return {"team_members": []}


def make_data_with_member(**kwargs):
    defaults = {"name": "Alice", "id": "A1", "kudos": 0, "whip_points": 0, "activity_log": []}
    defaults.update(kwargs)
    return {"team_members": [defaults]}


class TestLoadData:
    def test_missing_file_returns_empty_structure(self):
        result = data_manager.load_data()
        assert result == {"team_members": []}

    def test_valid_json_loads_correctly(self, tmp_path):
        path = tmp_path / "team_data.json"
        payload = {"team_members": [{"id": "X1", "name": "Bob"}]}
        path.write_text(json.dumps(payload))
        data_manager.DATA_FILE = str(path)
        result = data_manager.load_data()
        assert result == payload

    def test_corrupted_json_returns_empty_structure(self, tmp_path):
        path = tmp_path / "team_data.json"
        path.write_text("not valid json {{")
        data_manager.DATA_FILE = str(path)
        result = data_manager.load_data()
        assert result == {"team_members": []}


class TestSaveData:
    def test_save_and_reload(self):
        data = {"team_members": [{"id": "Z9", "name": "Zara"}]}
        data_manager.save_data(data)
        loaded = data_manager.load_data()
        assert loaded == data


class TestAddMember:
    def test_success(self):
        data = empty_data()
        ok, msg = data_manager.add_member(data, "Alice", "A1")
        assert ok is True
        assert msg is None
        assert len(data["team_members"]) == 1
        assert data["team_members"][0]["id"] == "A1"

    def test_duplicate_id_returns_false_with_message(self):
        data = empty_data()
        data_manager.add_member(data, "Alice", "A1")
        ok, msg = data_manager.add_member(data, "Alice2", "A1")
        assert ok is False
        assert msg


class TestFindMember:
    def test_found_returns_dict(self):
        data = make_data_with_member()
        result = data_manager.find_member(data, "A1")
        assert result is not None
        assert result["id"] == "A1"

    def test_not_found_returns_none(self):
        data = empty_data()
        assert data_manager.find_member(data, "MISSING") is None


class TestGiveKudos:
    def test_success_increments_kudos(self):
        data = make_data_with_member()
        ok, msg = data_manager.give_kudos(data, "A1", 5, "great work")
        assert ok is True
        assert msg is None
        assert data["team_members"][0]["kudos"] == 5

    def test_unknown_id_returns_false_with_message(self):
        data = empty_data()
        ok, msg = data_manager.give_kudos(data, "NOPE", 5, "reason")
        assert ok is False
        assert msg


class TestGiveWhipPoints:
    def test_success_increments_whip_points(self):
        data = make_data_with_member()
        ok, msg = data_manager.give_whip_points(data, "A1", 3, "missed deadline")
        assert ok is True
        assert msg is None
        assert data["team_members"][0]["whip_points"] == 3

    def test_unknown_id_returns_false_with_message(self):
        data = empty_data()
        ok, msg = data_manager.give_whip_points(data, "NOPE", 3, "reason")
        assert ok is False
        assert msg


class TestLogActivity:
    def test_appends_activity_with_correct_fields(self):
        member = {"name": "Alice", "id": "A1", "kudos": 0, "whip_points": 0, "activity_log": []}
        data_manager.log_activity(member, "kudos", 10, "delivered feature")
        assert len(member["activity_log"]) == 1
        entry = member["activity_log"][0]
        assert entry["type"] == "kudos"
        assert entry["points"] == 10
        assert entry["reason"] == "delivered feature"
        assert "timestamp" in entry

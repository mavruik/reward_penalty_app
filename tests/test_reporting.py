from reporting import (
    get_most_kudos,
    get_most_whip_points,
    get_average_kudos,
    get_average_whip_points,
)


def make_data(members):
    return {"team_members": members}


def member(name, kudos, whip_points):
    return {"name": name, "kudos": kudos, "whip_points": whip_points}


class TestGetMostKudos:
    def test_empty_team_returns_none(self):
        assert get_most_kudos(make_data([])) is None

    def test_single_member(self):
        m = member("Alice", 10, 0)
        result = get_most_kudos(make_data([m]))
        assert result["name"] == "Alice"

    def test_multiple_members_returns_highest(self):
        data = make_data([member("Alice", 5, 0), member("Bob", 15, 0), member("Carol", 10, 0)])
        assert get_most_kudos(data)["name"] == "Bob"


class TestGetMostWhipPoints:
    def test_empty_team_returns_none(self):
        assert get_most_whip_points(make_data([])) is None

    def test_single_member(self):
        m = member("Alice", 0, 7)
        result = get_most_whip_points(make_data([m]))
        assert result["name"] == "Alice"

    def test_multiple_members_returns_highest(self):
        data = make_data([member("Alice", 0, 3), member("Bob", 0, 9), member("Carol", 0, 6)])
        assert get_most_whip_points(data)["name"] == "Bob"


class TestGetAverageKudos:
    def test_empty_team_returns_zero(self):
        assert get_average_kudos(make_data([])) == 0

    def test_single_member(self):
        assert get_average_kudos(make_data([member("Alice", 8, 0)])) == 8.0

    def test_multiple_members(self):
        data = make_data([member("Alice", 10, 0), member("Bob", 20, 0)])
        assert get_average_kudos(data) == 15.0


class TestGetAverageWhipPoints:
    def test_empty_team_returns_zero(self):
        assert get_average_whip_points(make_data([])) == 0

    def test_single_member(self):
        assert get_average_whip_points(make_data([member("Alice", 0, 4)])) == 4.0

    def test_multiple_members(self):
        data = make_data([member("Alice", 0, 6), member("Bob", 0, 14)])
        assert get_average_whip_points(data) == 10.0

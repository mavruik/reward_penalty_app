from utils import validate_member_id, is_positive_integer


def make_data(*ids):
    return {"team_members": [{"id": mid} for mid in ids]}


class TestValidateMemberId:
    def test_unique_id_returns_true(self):
        data = make_data("A1", "A2")
        assert validate_member_id(data, "A3") is True

    def test_duplicate_id_returns_false(self):
        data = make_data("A1", "A2")
        assert validate_member_id(data, "A1") is False

    def test_empty_team_returns_true(self):
        data = make_data()
        assert validate_member_id(data, "A1") is True


class TestIsPositiveInteger:
    def test_positive_int_returns_true(self):
        assert is_positive_integer(5) is True

    def test_positive_string_returns_true(self):
        assert is_positive_integer("10") is True

    def test_zero_returns_false(self):
        assert is_positive_integer(0) is False

    def test_negative_returns_false(self):
        assert is_positive_integer(-3) is False

    def test_non_numeric_string_returns_false(self):
        assert is_positive_integer("abc") is False

    def test_float_string_that_is_int_castable_returns_true(self):
        # int("3.0") raises ValueError, but int(3.0) == 3 > 0
        assert is_positive_integer(3.0) is True

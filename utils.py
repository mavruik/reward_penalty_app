def validate_member_id(data, member_id):
    """Validates that a member ID is unique."""
    return not any(member['id'] == member_id for member in data['team_members'])

def is_positive_integer(value):
    """Checks if a value is a positive integer."""
    try:
        value = int(value)
        return valu{
            "team_members": []
        }
        e > 0
    except ValueError:
        return False

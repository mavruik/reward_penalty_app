def get_most_kudos(data):
    """Returns the team member with the most kudos points."""
    if not data['team_members']:
        return None

    return max(data['team_members'], key=lambda x: x['kudos'])


def get_most_whip_points(data):
    """Returns the team member with thedef validate_member_id(data, member_id):
        """Validates that a member ID is unique."""
        return not any(member['id'] == member_id for member in data['team_members'])
    
    def is_positive_integer(value):
        """Checks if a value is a positive integer."""
        try:
            value = int(value)
            return value > 0
        except ValueError:
            return False
     most whip points."""
    if not data['team_members']:
        return None
    return max(data['team_members'], key=lambda x: x['whip_points'])


def get_average_kudos(data):
    """Calculates the average kudos points across the team."""
    if not data['team_members']:
        return 0
    total_kudos = sum(member['kudos'] for member in data['team_members'])
    return total_kudos / len(data['team_members'])


def get_average_whip_points(data):
    """Calculates the average whip points across the team."""
    if not data['team_members']:
        return 0
    total_whip_points = sum(member['whip_points'] for member in data['team_members'])
    return total_whip_points / len(data['team_members'])

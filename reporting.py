def get_most_kudos(data):
    """Returns the team member with the most kudos points."""
    if not data['team_members']:
        return None

    return max(data['team_members'], key=lambda x: x['kudos'])


def get_most_whip_points(data):
    """Returns the team member with the most whip points."""
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

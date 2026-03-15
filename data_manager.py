import json
import os
from datetime import datetime

DATA_FILE = "team_data.json"  # Define a constant for the file path

def load_data():
    """Loads data from the JSON file.  Creates the file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        # Create the file with an empty structure if it doesn't exist
        with open(DATA_FILE, 'w') as f:
            json.dump({"team_members": []}, f, indent=4) # Initialize with empty team_members

    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"team_members": []}  # Return an empty structure if the file is not found
    except json.JSONDecodeError:
        print("Error decoding JSON.  The file may be corrupted.  Returning an empty dataset.")
        return {"team_members": []} # Handle corrupted JSON gracefully


def save_data(data):
    """Saves data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def add_member(data, name, member_id):
    """Adds a new team member to the data."""
    if any(member['id'] == member_id for member in data['team_members']):
        return False, "Member ID already exists."

    new_member = {
        "name": name,
        "id": member_id,
        "kudos": 0,
        "whip_points": 0,
        "activity_log": []
    }
    data['team_members'].append(new_member)
    return True, None


def give_kudos(data, member_id, points, reason):
    """Awards kudos points to a team member."""
    member = find_member(data, member_id)
    if not member:
        return False, "Member ID not found."

    member['kudos'] += points
    log_activity(member, "kudos", points, reason)
    return True, None


def give_whip_points(data, member_id, points, reason):
    """Assigns whip points to a team member."""
    member = find_member(data, member_id)
    if not member:
        return False, "Member ID not found."

    member['whip_points'] += points
    log_activity(member, "whip_points", points, reason)
    return True, None


def find_member(data, member_id):
    """Finds a team member by ID."""
    for member in data['team_members']:
        if member['id'] == member_id:
            return member
    return None


def log_activity(member, activity_type, points, reason):
    """Logs an activity for a team member."""
    activity = {
        "type": activity_type,
        "points": points,
        "reason": reason,
        "timestamp": datetime.now().isoformat()
    }
    member['activity_log'].append(activity)

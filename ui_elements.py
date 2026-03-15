import streamlit as st
import pandas as pd

def add_member_form():
    """Displays a form to add a new team member."""
    with st.form("add_member"):
        name = st.text_input("Name")
        member_id = st.text_input("Member ID")
        submitted = st.form_submit_button("Add Member")
        return name, member_id, submitted


def kudos_form():
    """Displays a form to award kudos points."""
    with st.form("give_kudos"):
        member_id = st.text_input("Member ID")
        points = st.number_input("Points", min_value=1, step=1)
        reason = st.text_area("Reason")
        submitted = st.form_submit_button("Give Kudos")
        return member_id, int(points) if points else None, reason, submitted # Ensure points is an int or None


def whip_points_form():
    """Displays a form to assign whip points."""
    with st.form("give_whip_points"):
        member_id = st.text_input("Member ID")
        points = st.number_input("Points", min_value=1, step=1)
        reason = st.text_area("Reason")
        submitted = st.form_submit_button("Assign Whip Points")
        return member_id, int(points) if points else None, reason, submitted # Ensure points is an int or None


def display_team_table(data):
    """Displays team member information in a table."""
    if data and data['team_members']:
        df = pd.DataFrame(data['team_members'])
        df = df.sort_values(by="name")
        df = df[["name", "id", "kudos", "whip_points"]]  # Select relevant columns
        st.dataframe(df, hide_index=True)  # Display dataframe in Streamlit
    else:
        st.write("No team members to display.")


def display_activity_log(member):
    """Displays the activity log for a team member."""
    if member and member['activity_log']:
        df = pd.DataFrame(member['activity_log'])
        df = df[["timestamp", "type", "points", "reason"]]  # Select relevant columns
        st.dataframe(df, hide_index=True)
    else:
        st.write("No activity log for this member.")

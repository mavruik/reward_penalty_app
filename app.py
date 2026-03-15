import streamlit as st
import data_manager as dm
import ui_elements as ui
import utils
import reporting

st.title("Kudos and Whip Points Tracker")

# Load data from JSON file
data = dm.load_data()

# Add Member Form
st.header("Add New Member")
name, member_id, add_submitted = ui.add_member_form()
if add_submitted:
    if not utils.validate_member_id(data, member_id):
        st.error("Member ID already exists. Please use a unique ID.")
    else:
        success, message = dm.add_member(data, name, member_id)
        if success:
            dm.save_data(data)
            st.success(f"Member {name} added successfully!")
        else:
            st.error(message)

# Award Kudos Form
st.header("Award Kudos")
kudos_member_id, kudos_points, kudos_reason, kudos_submitted = ui.kudos_form()
if kudos_submitted:
    if not kudos_member_id:
        st.error("Member ID is required.")
    elif not kudos_points:
        st.error("Points must be a positive number")
    else:
        success, message = dm.give_kudos(data, kudos_member_id, kudos_points, kudos_reason)
        if success:
            dm.save_data(data)
            st.success(f"{kudos_points} kudos points awarded to member {kudos_member_id}!")
        else:
            st.error(message)

# Assign Whip Points Form
st.header("Assign Whip Points")
whip_member_id, whip_points, whip_reason, whip_submitted = ui.whip_points_form()
if whip_submitted:
    if not whip_member_id:
        st.error("Member ID is required.")
    elif not whip_points:
        st.error("Points must be a positive number")
    else:
        success, message = dm.give_whip_points(data, whip_member_id, whip_points, whip_reason)
        if success:
            dm.save_data(data)
            st.success(f"{whip_points} whip points assigned to member {whip_member_id}!")
        else:
            st.error(message)

# Display Team Table
st.header("Team Members")
ui.display_team_table(data)

# Activity Log
st.header("Activity Log")
selected_member_id = st.selectbox("Select Member", [member['id'] for member in data['team_members']] if data['team_members'] else [])

if selected_member_id:
    member = dm.find_member(data, selected_member_id)
    ui.display_activity_log(member)
else:
    st.write("No members available to display activity log.")

# Reporting Section
st.header("Reporting")
most_kudos_member = reporting.get_most_kudos(data)
most_whip_points_member = reporting.get_most_whip_points(data)
average_kudos = reporting.get_average_kudos(data)
average_whip_points = reporting.get_average_whip_points(data)

if most_kudos_member:
    st.write(f"Most Kudos: {most_kudos_member['name']} ({most_kudos_member['kudos']})")
else:
    st.write("No members to calculate most kudos.")

if most_whip_points_member:
    st.write(f"Most Whip Points: {most_whip_points_member['name']} ({most_whip_points_member['whip_points']})")
else:
    st.write("No members to calculate most whip points.")

st.write(f"Average Kudos: {average_kudos:.2f}")
st.write(f"Average Whip Points: {average_whip_points:.2f}")

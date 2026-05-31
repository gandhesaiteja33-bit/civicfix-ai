import streamlit as st
import pandas as pd

from database import (
    get_all_complaints,
    update_status
)

from config import (
    STATUSES
)

# -------------------------
# LOGIN CHECK
# -------------------------

# -------------------------
# LOGIN CHECK
# -------------------------

if (
    "user" not in st.session_state
    or st.session_state.user is None
):

    st.warning(
        "Please login first"
    )

    st.stop()

# -------------------------
# ADMIN CHECK
# -------------------------

if (
    st.session_state.user.get("role")
    != "Admin"
):

    st.error(
        "Only Admin can access this page"
    )

    st.stop()

# -------------------------
# ADMIN CHECK
# -------------------------


if (
    st.session_state.user.get("role")
    != "Admin"
):

    st.error(
        "Only Admin can access this page"
    )

    st.stop()

# -------------------------
# LOAD DATA
# -------------------------

rows = get_all_complaints()

columns = [
    "id",
    "name",
    "location",
    "issue",
    "category",
    "priority",
    "status",
    "image_path",
    "created_at"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

# -------------------------
# PAGE
# -------------------------

st.title("🛠 Admin Panel")

if len(df) == 0:

    st.info(
        "No complaints found"
    )

    st.stop()

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

complaint_id = st.selectbox(
    "Select Complaint ID",
    df["id"]
)

new_status = st.selectbox(
    "Update Status",
    STATUSES
)

if st.button(
    "Update Complaint"
):

    update_status(
        complaint_id,
        new_status
    )

    st.success(
        "Status Updated Successfully"
    )

    st.rerun()
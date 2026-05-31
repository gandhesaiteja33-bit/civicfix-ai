import streamlit as st
import pandas as pd

from database import (
    get_all_complaints
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
# USER DATA
# -------------------------

user = st.session_state.user

st.title("👤 Profile")

st.subheader(
    user["username"]
)

st.write(
    f"Role: {user['role']}"
)

# -------------------------
# USER COMPLAINTS
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

user_df = df[
    df["name"] ==
    user["username"]
]

st.metric(
    "My Complaints",
    len(user_df)
)

st.dataframe(
    user_df,
    use_container_width=True
)
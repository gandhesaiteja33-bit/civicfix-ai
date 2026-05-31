import streamlit as st
from datetime import datetime
import os

from database import add_complaint
from ai_utils import (
    categorize_issue,
    detect_priority
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
# PAGE
# -------------------------

st.title("📝 Submit Complaint")

name = st.text_input(
    "Your Name",
    value=st.session_state.user["username"]
)

location = st.text_input(
    "Location"
)

issue = st.text_area(
    "Describe the issue"
)

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if st.button("Submit Complaint"):

    if not location or not issue:
        st.error("Please fill all required fields")
        st.stop()

    category = categorize_issue(issue)

    priority = detect_priority(issue)

    image_path = ""

    if uploaded_file:

        image_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(
            image_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

    add_complaint(
        name=name,
        location=location,
        issue=issue,
        category=category,
        priority=priority,
        status="Submitted",
        image_path=image_path,
        created_at=str(datetime.now())
    )

    st.success(
        "Complaint Submitted Successfully"
    )

    st.info(
        f"""
        Category: {category}
        | Priority: {priority}
        """
    )
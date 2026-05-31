import streamlit as st

from database import get_complaint_by_id

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

st.title("🔍 Track Complaint")

complaint_id = st.number_input(
    "Enter Complaint ID",
    min_value=1,
    step=1
)

if st.button("Track Complaint"):

    complaint = get_complaint_by_id(
        complaint_id
    )

    if complaint:

        st.success(
            "Complaint Found"
        )

        st.write(
            f"Complaint ID: {complaint[0]}"
        )

        st.write(
            f"Name: {complaint[1]}"
        )

        st.write(
            f"Location: {complaint[2]}"
        )

        st.write(
            f"Issue: {complaint[3]}"
        )

        st.write(
            f"Category: {complaint[4]}"
        )

        st.write(
            f"Priority: {complaint[5]}"
        )

        st.write(
            f"Status: {complaint[6]}"
        )

        st.write(
            f"Created At: {complaint[8]}"
        )

        if complaint[7]:

            st.image(
                complaint[7],
                caption="Uploaded Evidence"
            )

    else:

        st.error(
            "Complaint Not Found"
        )
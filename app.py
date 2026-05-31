import streamlit as st

from config import APP_NAME
from database import initialize_database
from auth import (
    register_user,
    login_user,
    create_admin
)

initialize_database()
create_admin()

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🏙️",
    layout="wide"
)

# -------------------------
# SESSION
# -------------------------

if "user" not in st.session_state:
    st.session_state.user = None
if st.session_state.user is None:
    st.info(
        "Please login to access CivicFix AI."
    )


# -------------------------
# HOME
# -------------------------

st.title("🏙️ CivicFix AI")

st.write(
    """
    Smart Civic Complaint
    Management System
    """
)

# -------------------------
# LOGIN / REGISTER
# -------------------------

if st.session_state.user is None:

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    # -----------------
    # LOGIN
    # -----------------

    with tab1:

        st.subheader(
            "Login"
        )

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button(
            "Login"
        ):

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.user = user

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

    # -----------------
    # REGISTER
    # -----------------

    with tab2:

        st.subheader(
            "Register"
        )

        new_username = st.text_input(
            "New Username"
        )

        new_password = st.text_input(
            "New Password",
            type="password"
        )

        if st.button(
            "Register"
        ):

            success = register_user(
                new_username,
                new_password
            )

            if success:

                st.success(
                    "Account Created"
                )

            else:

                st.error(
                    "Username Already Exists"
                )

# -------------------------
# LOGGED IN
# -------------------------

else:

    st.success(
        f"""
        Logged in as
        {st.session_state.user['username']}
        """
    )

    st.info(
        f"""
        Role:
        {st.session_state.user['role']}
        """
    )

    if st.button(
        "Logout"
    ):

        st.session_state.user = None

        st.rerun()

    st.write(
        """
        Use the Pages menu
        in the sidebar   to navigate.
        """
    )
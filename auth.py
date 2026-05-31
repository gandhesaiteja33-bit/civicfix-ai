import hashlib

from database import (
    add_user,
    get_user
)


# -------------------------
# HASH PASSWORD
# -------------------------

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# -------------------------
# REGISTER USER
# -------------------------

def register_user(
    username,
    password,
    role="Citizen"
):

    username = username.strip()

    if not username or not password:
        return False

    existing_user = get_user(
        username
    )

    if existing_user:
        return False

    hashed_password = hash_password(
        password
    )

    add_user(
        username,
        hashed_password,
        role
    )

    return True


# -------------------------
# LOGIN USER
# -------------------------

def login_user(
    username,
    password
):

    username = username.strip()

    user = get_user(
        username
    )

    if not user:
        return None

    hashed_password = hash_password(
        password
    )

    if user[2] == hashed_password:

        return {
            "id": user[0],
            "username": user[1],
            "role": user[3]
        }

    return None


# -------------------------
# CREATE DEFAULT ADMIN
# -------------------------

def create_admin():

    admin_user = get_user(
        "admin"
    )

    if admin_user:
        return

    admin_password = hash_password(
        "admin123"
    )

    add_user(
        "admin",
        admin_password,
        "Admin"
    )
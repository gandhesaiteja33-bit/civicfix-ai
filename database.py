import sqlite3
from config import DB_PATH


def get_connection():
    return sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # Complaints Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        issue TEXT,
        category TEXT,
        priority TEXT,
        status TEXT,
        image_path TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


# -------------------------
# USER FUNCTIONS
# -------------------------

def add_user(username, password, role):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (username,password,role)
        VALUES(?,?,?)
        """,
        (username, password, role)
    )

    conn.commit()
    conn.close()


def get_user(username):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# -------------------------
# COMPLAINT FUNCTIONS
# -------------------------

def add_complaint(
    name,
    location,
    issue,
    category,
    priority,
    status,
    image_path,
    created_at
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO complaints
    (
    name,
    location,
    issue,
    category,
    priority,
    status,
    image_path,
    created_at
    )
    VALUES
    (?,?,?,?,?,?,?,?)
    """,
    (
        name,
        location,
        issue,
        category,
        priority,
        status,
        image_path,
        created_at
    ))

    conn.commit()
    conn.close()


def get_all_complaints():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM complaints"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_complaint_by_id(cid):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM complaints
        WHERE id=?
        """,
        (cid,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def update_status(cid, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET status=?
        WHERE id=?
        """,
        (
            status,
            cid
        )
    )

    conn.commit()
    conn.close()


initialize_database()
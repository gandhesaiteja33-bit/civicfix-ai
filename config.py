import os

# Database
DB_PATH = "data/civicfix.db"

# Upload Folder
UPLOAD_FOLDER = "uploads"

# Create folders automatically
os.makedirs("data", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

# App Name
APP_NAME = "CivicFix AI"

# Complaint Statuses
STATUSES = [
    "Submitted",
    "In Progress",
    "Resolved",
    "Rejected"
]

# User Roles
ROLES = [
    "Citizen",
    "Admin"
]
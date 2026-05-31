## 🛠️ How This Project Was Built

CivicFix AI was developed as a full-stack civic complaint management system using Python and Streamlit.

### Step 1: Project Setup
- Created a Python virtual environment
- Installed required libraries (Streamlit, SQLite, Pandas)
- Structured the project into modular files (auth, database, utils, pages)

### Step 2: Backend Development
- Built authentication system using hashed passwords
- Designed SQLite database for storing users and complaints
- Created functions for adding, retrieving, and updating complaints

### Step 3: Core Features Implementation
- Complaint submission system with image upload
- Auto categorization of complaints (Road, Water, Electricity, etc.)
- Priority detection based on keywords
- Complaint tracking using unique ID system

### Step 4: Admin Panel
- Created admin dashboard to view all complaints
- Added ability to update complaint status
- Implemented role-based access control (Admin vs Citizen)

### Step 5: Frontend (Streamlit UI)
- Built multi-page Streamlit application
- Created pages for Dashboard, Submit Complaint, Track Complaint, Admin Panel, and Profile
- Added clean UI with tables and forms

### Step 6: Git & Version Control
- Initialized Git repository locally
- Connected project to code.swecha.org
- Pushed all code using Git commands for version tracking

### Step 7: Testing
- Tested login and registration system
- Verified complaint submission and tracking
- Tested admin workflow and status updates

### Final Outcome
A working CivicTech platform that allows citizens to report issues and helps authorities manage and resolve them efficiently.
# 🤖 AGENTS.md - CivicFix AI

This document describes the AI agents, automation logic, and system behavior used in the CivicFix AI project.

---

## 🧠 Overview

CivicFix AI uses rule-based AI logic to assist in:
- Complaint categorization
- Priority detection
- Data organization
- Workflow automation

The system is designed to simulate intelligent civic issue handling.

---

## 🤖 AI Components

### 1. Complaint Classification Agent

**Purpose:**
Automatically assigns a category to user complaints.

**Categories:**
- Road Issues
- Water Supply Issues
- Electricity Issues
- Waste Management
- Public Safety
- Other

**Logic:**
- Keyword-based classification from complaint text
- Example:
  - "pothole", "road broken" → Road Issues
  - "water leak", "no water" → Water Supply

---

### 2. Priority Detection Agent

**Purpose:**
Determines urgency level of complaint.

**Priority Levels:**
- High
- Medium
- Low

**Logic:**
- High: dangerous, accident, urgent, flooding
- Medium: damaged, issue, problem
- Low: minor, small issue

---

### 3. Complaint Processing Agent

**Purpose:**
Handles structured storage of complaints.

**Functions:**
- Assign unique Complaint ID
- Store user input in database
- Save image evidence path
- Timestamp creation

---

### 4. Admin Workflow Agent

**Purpose:**
Helps administrators manage complaints.

**Functions:**
- View all complaints
- Update status:
  - Submitted
  - In Progress
  - Resolved
- Track resolution lifecycle

---

### 5. User Session Agent

**Purpose:**
Manages login sessions.

**Functions:**
- Stores logged-in user in session state
- Controls access to pages
- Enforces role-based access (Admin / Citizen)

---

## ⚙️ System Workflow

```text id="flow1"
User Complaint → Classification Agent → Priority Agent → Database Storage → Admin Review → Status Update → User Tracking
# 🏙️ CivicFix AI

An AI-powered Civic Complaint Management System that allows citizens to report public issues, track status in real time, and helps administrators efficiently manage and resolve civic complaints.

---

## 📌 Problem Statement

Citizens often face delays and lack of transparency when reporting civic issues like potholes, water leakage, garbage accumulation, etc. CivicFix AI solves this by providing a centralized, intelligent complaint management system.

---

## 🚀 Features

### 👤 Citizen Features
- User Registration & Login system
- Submit civic complaints with details
- Upload image evidence for issues
- Automatic category detection (Road, Water, Electricity, Waste, etc.)
- Automatic priority classification (High / Medium / Low)
- Track complaint status using Complaint ID
- View personal complaint history

### 🛠️ Admin Features
- Secure Admin Login
- View all complaints in dashboard
- Update complaint status (Submitted → In Progress → Resolved)
- Monitor and manage civic issues efficiently

### 📊 Analytics & Insights
- Complaint distribution by category
- Priority-based filtering
- Status tracking dashboard
- CSV export for reports

---

## 🧠 AI Capabilities
- Intelligent complaint categorization
- Priority detection using keywords
- Smart classification of civic issues
- Structured complaint processing

---

## 🏗️ Tech Stack

- Python 🐍  
- Streamlit 🌐  
- SQLite 🗄️  
- Pandas 📊  
- Plotly 📈  

---

## 📁 Project Structure
.civicfix-ai/
│
├── app.py
├── auth.py
├── database.py
├── config.py
├── ai_utils.py
│
├── pages/
│ ├── 1_Dashboard.py
│ ├── 2_Submit_Complaint.py
│ ├── 3_Track_Complaint.py
│ ├── 4_Admin_Panel.py
│ └── 5_Profile.py
│
├── utils/
│ ├── charts.py
│ ├── theme.py
│ └── export.py
│
├── data/
├── uploads/
└── requirements.txt
## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://code.swecha.org/teja_456/civicfix-ai.git
cd civicfix-ai
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run app.py

🔐 Default Admin Login
Username: admin
Password: admin123

📈 Future Improvements
Google Maps integration for complaints
AI-based sentiment analysis
Email/SMS notifications
Mobile app version
Government department integration

📜 License

This project is for educational and hackathon purposes.

live working url:

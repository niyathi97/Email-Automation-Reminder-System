# 📧 Email Automation & Reminder System

## 🚀 Project Overview

The Email Automation & Reminder System is a Python-based automation project that automatically sends personalized reminder emails to users using contact data stored in CSV files.

The system reads contacts, loads email templates, personalizes messages, sends emails using SMTP, tracks status, and generates reports.

This project simulates how companies automate reminders, follow-ups, webinar notifications, meeting alerts, and task reminders.

---

# 🎯 Problem Statement

Manually sending repetitive emails to multiple users is time-consuming and inefficient.

This project automates the process of:
- Sending reminder emails
- Personalizing messages
- Tracking sent/failed emails
- Generating reports automatically

---

# 💡 Features

✅ Automated Email Sending  
✅ Personalized Email Templates  
✅ CSV Contact Management  
✅ SMTP Email Integration  
✅ Streamlit Dashboard  
✅ Email Status Tracking  
✅ CSV Report Generation  
✅ Beginner-Friendly Python Project  

---

# 🛠️ Tech Stack

- Python
- Pandas
- Streamlit
- smtplib
- email.message
- schedule
- CSV Files

---

# 📂 Folder Structure

```text
Email-Automation-Reminder-System/
│
├── data/
│   └── contacts.csv
│
├── templates/
│   └── email_template.txt
│
├── src/
│   ├── email_sender.py
│   ├── scheduler.py
│   └── template_loader.py
│
├── outputs/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Email-Automation-Reminder-System.git
```

## Open Project Folder

```bash
cd Email-Automation-Reminder-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
streamlit run main.py
```

---

# 📄 Email Workflow

Contacts CSV  
↓  
Load Email Template  
↓  
Personalize Message  
↓  
SMTP Email Sending  
↓  
Track Email Status  
↓  
Generate CSV Report

---

# 📊 Sample Output

| Name | Email | Status |
|---|---|---|
| John Doe | johndoe@gmail.com | Sent |
| Alice Smith | alice@gmail.com | Sent |

---

# 📸 Screenshots

## Project Folder
(Add Screenshot)

## Streamlit Dashboard
(Add Screenshot)

## Contacts CSV
(Add Screenshot)

## Email Report CSV
(Add Screenshot)

---

# 🌍 Industry Relevance

This project demonstrates how organizations automate repetitive communication tasks such as:
- Meeting reminders
- Webinar reminders
- Payment notifications
- HR follow-ups
- Task alerts
- Student notifications

It reflects real-world business automation systems.

---

# 🧠 Learning Outcomes

- Email Automation
- SMTP Integration
- CSV Data Handling
- Streamlit UI Development
- Python Automation
- Report Generation
- GitHub Project Management

---

# 🔒 Security Note

❌ Never upload real passwords to GitHub.

Use:
- Gmail App Passwords
- Environment Variables
- .gitignore

---

# 🔮 Future Improvements

- Scheduled Email Automation
- Database Integration
- WhatsApp/SMS Notifications
- Dashboard Analytics
- Bulk Email Campaigns
- FastAPI Backend

---

# 👨‍💻 Author

Developed as a Python Automation Project for learning and portfolio building.

---

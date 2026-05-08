import pandas as pd
import streamlit as st
from datetime import datetime

from src.template_loader import load_template
from src.email_sender import send_email


st.set_page_config(page_title="Email Automation System", layout="wide")

st.title("📧 Email Automation & Reminder System")


# Sender Details
sender_email = st.text_input("Sender Gmail")

sender_password = st.text_input(
    "Gmail App Password",
    type="password"
)


# Email Subject
subject = st.text_input(
    "Email Subject",
    "Reminder Notification"
)


# Load Template
template = load_template("templates/email_template.txt")


st.subheader("📄 Email Template")

st.code(template)


# Send Button
if st.button("Send Emails"):

    contacts = pd.read_csv("data/contacts.csv")

    results = []

    st.write("## Sending Emails...")

    for index, row in contacts.iterrows():

        name = row["name"]

        receiver_email = row["email"]

        # Personalize Message
        message = template.format(name=name)

        # Send Email
        status = send_email(
            sender_email,
            sender_password,
            receiver_email,
            subject,
            message
        )

        results.append({
            "Name": name,
            "Email": receiver_email,
            "Status": status,
            "Timestamp": datetime.now()
        })

        st.write(f"{name} → {status}")

    # Save Report
    report = pd.DataFrame(results)

    output_path = "outputs/email_report.csv"

    report.to_csv(output_path, index=False)

    st.success("Email Automation Completed!")

    st.success(f"Report Saved At: {output_path}")

    st.dataframe(report)
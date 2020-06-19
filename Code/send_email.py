#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:52:14 2020

@author: Michael
"""

# %% -----------------------------------------------------------------------------------------------
# Import modules

import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# %% -----------------------------------------------------------------------------------------------
# Send email

def send_email(item_list):

    port = 587  # For SSL
    smtp_server = "smtp.office365.com"
    #password = input("Type your password and press enter: ")
    password = 'K4ng4r00'
    sender_email = "z3526971@ad.unsw.edu.au"
#    receiver_email = "z3526971@ad.unsw.edu.au"
    receiver_email = ["z3526971@unsw.edu.au","rowheenee@gmail.com"]
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Hello Fresh Shopping list this week"
    message["From"] = sender_email
#    message["To"] = receiver_email
    message["To"] = ", ".join(receiver_email) # concatenate the emails together split by commas
    
    text = str(item_list)
    html = str(item_list)
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain") 
    part2 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    
    
    
    
    
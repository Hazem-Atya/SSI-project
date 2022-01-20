import smtplib, ssl
import sys,os
import math, random
import config.constants as config


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = config.emailCredentials['email']
password=config.emailCredentials['password']

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(5) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def sendVerificationCode(receiver_email,receiver_name):
    otp=generateOTP()
    message = f"""\
Subject: Verification code

Hello {receiver_name},\n This is your OTP code: {otp}.\n
This code is only valid for 5 minutes.
"""
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return otp

import requests
import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##############################
# This is a script that can be used to somewhat automate 
# checking for new job offers.
# It's a simple web scraper that checks a specific
# URL's contents and finds whether a given keyword has 
# been found. If so, it sends an e-mail to notify you
# of said job offer.
#
# This version of the script asks the user to enter their
# password instead of storing it in plaintext.
#
# By Kamiel de Visser
##############################

# Enter your e-mail address here
MY_EMAIL = "my@gmail.com"

# Enter the receiver's email address here (can be MY_EMAIL)
RECEIVER_EMAIL = MY_EMAIL

# Enter the URL at which your job offer is posted here
URL = "https://www.some-url.com"
# Enter the keyword for the job offer here (i.e. your town's name or a position)
KEYWORD = "Amsterdam"

page = requests.get(URL)

if(str(page.content).find(KEYWORD) != -1):
    port = 465
    context = ssl.create_default_context()

    password = input("Please enter your e-mail password: \n") 

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(MY_EMAIL, password)

        sender = MY_EMAIL
        receiver = RECEIVER_EMAIL

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Job offer available!"
        body = "There is a new job offer available at " + URL + "\nGo take a look!"
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(sender, receiver, msg.as_string())

        print("Success! Job found!")
        exit()

print("Script ran but no job was found")
# Import libraries
import urllib.request
import smtplib, time, hashlib


# Function to send email
def send_email(email_string):
    # Fill credentials for sender's email and receiver's email
    email_from = 'enter sender\'s email'
    password = 'enter password'
    email_to = 'enter reciever\'s email'
    # Enter subject line
    subject = "Status of website"

    # Connect to gmail's smtp server
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login to the gmail server
    smtp_server.login(email_from, password)

    # Content of email
    message = f"Subject: {subject}\n\n{email_string}"

    # Send email through the smtp server
    smtp_server.sendmail(email_from, email_to, message)

    # Close the server connection
    smtp_server.close()


# Monitor the website
def monitor_website():
    # Run the loop the keep monitoring
    while True:
        # Visit the website to know if it is up
        status = urllib.request.urlopen(input_website).getcode()
        # If it returns 200, the website is up
        if status != 200:
            # Call email function
            send_email("The website is down")
        else:
            send_email("The website is up")
            # Open url and create the hash code
            response = urllib.request.urlopen(input_website).read()
            current_hash = hashlib.sha224(response).hexdigest()
            # Revisit the website after time delay
            time.sleep(time_delay)
            # Visit the website after delay, and generate the new website
            response = urllib.request.urlopen(input_website).read()
            new_hash = hashlib.sha224(response).hexdigest()
            # Check the hash codes
            if new_hash != current_hash:
                send_email("The website changed")


# Read the website and read time interval
input_website = input('Enter the website to monitor: ')
input_website = 'https://' + input_website
time_delay = int(input('Enter the time interval to check website: '))

# Monitoring website
monitor_website()


import smtplib

email = input("SENDER EMAIL: ")
receiver_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")

message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# go to your gamil account and endable two factor authentication
#on the search bar , search for app passwords 
# create new app. give it a  name copy the name and paste it here.
server.login(email, "")

server.sendmail(email, receiver_email, text)

print("Email has been sent to " + receiver_email)


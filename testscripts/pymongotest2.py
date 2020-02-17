import pymongo
import datetime
import time
import serial
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'makeuoft1@gmail.com'
password = 'Chealsie'
send_to_email = 'makeuoft1@gmail.com'
subject = 'You Saved Power!'
message = 'Your outlet was automatically shut off to save power on' + (datetime.datetime.now()).strftime("%d-%b-%Y (%H:%M:%S.%f)")

ser = serial.Serial('/dev/tty96B0', 9600)
client = pymongo.MongoClient("mongodb+srv://Edmund:iamhere10@cluster0-nkp9x.mongodb.net/PowerBoi") # defaults to port 27017
db = client.PowerBoi.Usage
PowerOn = True


while True:

    if(ser.in_waiting > 0):
        line = ser.readline()
        line2 = line.decode('ASCII')
        line2 = line2.strip('\n')
        line2 = line2.strip('\r')
        line2 = line2.split(",")
        line2 = [float(i) for i in line2]

        print(line2)

        post = {"Power": line2[0],
                "Current": line2[1],
                "Temperature": line2[2],
                "Time": datetime.datetime.now()}

        post_id = db.insert_one(post).inserted_id
        print("done")

    if(PowerOn):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login("makeuoft1@gmail.com", "Chealsie")



    # print the number of documents in a collection
print(db.estimated_document_count())

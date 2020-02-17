import pymongo
import datetime
import time
import serial

ser = serial.Serial('/dev/tty96B0', 9600)
client = pymongo.MongoClient("mongodb+srv://Edmund:iamhere10@cluster0-nkp9x.mongodb.net/PowerBoi") # defaults to port 27017
db = client.PowerBoi.Usage

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


    # print the number of documents in a collection
print(db.estimated_document_count())

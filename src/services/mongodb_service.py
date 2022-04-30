# MongoDB SERVICE
from decouple import config
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
from datetime import datetime
# Get environment variables
# pip install python-decouple
# python -m pip install pymongo



#####################################################################
#
# Mongo DB Setup
#
#####################################################################

# env variables 
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASS = config('DB_PASS')

# connection string
DB_URL = f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

# connection
client = MongoClient(DB_URL)

# database select
db = client.boiler

######################################################################
#
# Issue the serverStatus command and print the results
#
######################################################################

#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

######################################################################
#
# Add reading 
#
######################################################################
def add_temp_reading(sensor_id,degrees_celcius): 
    
    """
    adds a reading into the database. 
    """
    temp_reading = {
        'timeStamp': datetime.timestamp(datetime.now()),
        'sensorId': sensor_id,
        'degrees_celcius': degrees_celcius
    }
    result = db.sensorReading.insert_one(temp_reading)

######################################################################
#
# Authenticate
#
######################################################################

def authenticate(id):    # authenticate
    if DB_HOST is None:
        print('User is undefined')
    print("authenticating user", DB_HOST, id)
    

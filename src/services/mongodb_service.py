# MongoDB SERVICE



from decouple import config
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
from random import randint
from datetime import datetime
import json
import os
import re



#####################################################################
#
# Mongo DB Setup
#
#####################################################################

# Get environment variables
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
db = client[DB_NAME]

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
def add_temp_reading(sensor_id,degrees_fahrenheit,collection): 
    javascript_timestamp = datetime.timestamp(datetime.now()) * 1000

    """
    adds a reading into the database. 
    """
    temp_reading = {
        'timeStamp': javascript_timestamp,
        'sensorId': sensor_id,
        'degreesFahrenheit': degrees_fahrenheit
    }
    result = db[collection].insert_one(temp_reading)
######################################################################
#
# Get or Create System
#
######################################################################
def getSystem(system_id):
    query = { "_id": system_id }
    '''
     get a system.  if not system exists, creates one
    '''
    collection = db['systems']
    document = collection.find_one(query)
    if  document is None:
        system = {
            "_id": str(system_id)
            }
        document = collection.insert_one(system)
    return document

def getOrAddSystem(system_id):
    collection = db['systems']
    if system_id is None:
        print('adding new system...')
        _id = collection.insert_one({ "AIDatapipes Controller": datetime.now()})
        print ('adding' + str(_id.inserted_id) + 'into database')
        with open("system.json", 'r') as f:
            data = json.load(f)   #print(data['system']['id'])
            data['system']['systemId'] = str(_id.inserted_id)
        os.remove("system.json")
        with open("system.json", 'w') as f:
            json.dump(data, f, indent=4)
        return (_id)

    else:
        print('system is: ' + system_id)
######################################################################
#
# Add Hydronic Zone
#
######################################################################
def addHydroZoneData(system_id,zone_index,line_type,degF):
    '''
    ######################################################################
    #
    # Add hyrdronic zone epecific sensor data (temperatures/humidy)
    # Includes 
    #   - Return Temp   (lineRT)
    #   - Supply Temp   (lineST)
    #   - Room Temp     (lineRMTMP)
    #   - Room Humidiy  (lineRMHD)
    #
    ######################################################################
    '''
    exists = getSystem(system_id)
    if not exists:
        raise Exception("system id does not exist")
    
    result = db.systems.update_one({"_id" : system_id},{"$push": {"zone"+str(zone_index): {line_type :[{"timeStamp": datetime.now(), "degF": degF}]}}})
    print (result)
    return result


######################################################################
#
# Authenticate
#
######################################################################

def authenticate(id):    # authenticate
    if DB_HOST is None:
        print('User is undefined')
    print("authenticating user", DB_HOST, id)


    

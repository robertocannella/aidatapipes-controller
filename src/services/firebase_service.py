################################################################################
#
#   GOOGLE FIRESTORE NOSQL DATA BASE SERVICE
#   
################################################################################

#**************************   IMPORTS   ***************************************#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from decouple import config
from datetime import datetime


################################################################################
#
#   GOOGLE FIRESTORE INSTANCE
#   
################################################################################

# Import credentials from json 
cred = credentials.Certificate("fs-aidatapipes-key-04-30-2022.json")

# Initialize app
firebase_admin.initialize_app(cred)

# create db object
db = firestore.client() 

#**************************   CRUD   ***************************************#


######################################################################
#
# Add temperature reading
#
######################################################################
def overwrite_last_temp_reading(sensor_id,degrees_fahrenheit,type): 
    """
    adds a reading into the database. 
    """
    # generate link to collection 
    doc_ref = db.collection(type).document(sensor_id)

    # generate timestamp
    javascript_timestamp = datetime.timestamp(datetime.now()) * 1000

    # write to database
    doc_ref.set({
        'timeStamp': javascript_timestamp,
        'sensorId': sensor_id,
        'degreesFahrenheit': degrees_fahrenheit
    })
   
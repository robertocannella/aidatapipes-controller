# MongoDB SERVICE
from decouple import config
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
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



#Step 2: Create sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.reviews.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')

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
        'sensorId': sensor_id,
        'degrees_celcius': degrees_celcius
    }
    result = db.sensorReading.insert_one(temp_reading)
    print(result)


def authenticate(id):    # authenticate
    if DB_HOST is None:
        print('User is undefined')
    print("authenticating user", DB_HOST, id)
    

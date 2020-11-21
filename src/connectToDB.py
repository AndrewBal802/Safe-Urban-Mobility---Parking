import pymongo

#Connect to Database
client = pymongo.MongoClient("mongodb+srv://Andrew:AstroCode@cluster0.jke3h.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client['ParkingLotDB'] #Accessing ParkingLot DB
parkingLot = db['ParkingLot']

def insertDB(tableName, _id, capacity, reservation_type, fee, hourlyRate, maxHours, hours, lon, lat):
    if (findRecord(tableName, _id) != None):
        print("In table: " + tableName + ", RECORD _id:" + str(_id) + " already exists!")
        return None

    table = db[tableName]
    record = {
        '_id': _id,
        'capacity': capacity,
        'reservation_type': reservation_type,
        'fee': fee,
        'hourly_rate': hourlyRate,
        'maxHours': maxHours,
        'hours': hours,
        'lon': lon,
        'lat':  lat,

    }
    result = table.insert_one(record)

    return result #returns recordID



def findRecord(tableName, _id):
    table = db[tableName]

    for record in table.find():
        if (record.get("_id") == _id):
            return record
    
    return None #no existing record

def updateRecord(tableName, _id, newRecord):
    if (findRecord(tableName, _id) == None):
        print("In table: " + tableName + ", RECORD _id:" + str(_id) + " does not exist!")
        return None
    
    table = db[tableName]
    getRecord = { '_id': _id }
    updateRecord = { '$set': newRecord} # newRecord should be:
                                        # { 'attributeName': value, ... }

    table.update_one(getRecord, updateRecord)

def printDB(tableName):
    table = db[tableName]

    for record in table.find():
        print(record)

###
def main():
    insertDB('ParkingLot', 1, 200, 'Public', True, 4, 10, '3pm-10pm', -34.2, 74)
    print(findRecord('ParkingLot', 1))

    updateRecord('ParkingLot', 1, { 'capacity': 5000})

    print(findRecord('ParkingLot', 1))
    
    updateRecord('ParkingLot', 1, { 'capacity': 400})
   
    #insertDB('ParkingLot', 2, 24.3, 47, 1000, '$5/hour', 'Public', 'Y') 
    #updateRecord('ParkingLot', 2, { 'capacity': 20}) #Testing Invalid

    printDB('ParkingLot')


if __name__ == '__main__':
    main()

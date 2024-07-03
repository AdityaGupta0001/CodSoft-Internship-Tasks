from pymongo import MongoClient

def get_data():
    client = MongoClient('localhost',27017)
    db = client.BookBuddy
    collection = db.contacts
    data = []
    for j in collection.find():
        data.append(j)
    contacts = [["Name", "Phone", "Email", "Address", "City", "State", "Country"]]
    for i in range(len(data)):
        temp = []
        temp.append(data[i]['name'])
        temp.append(data[i]['phone'])
        temp.append(data[i]['email'])
        temp.append(data[i]['address'])
        temp.append(data[i]['city'])
        temp.append(data[i]['state'])
        temp.append(data[i]['country'])
        contacts.append(temp) 
    client.close()
    return contacts

def add_data(name,phone,email,address,city,state,country):
    client = MongoClient('localhost',27017)
    db = client.BookBuddy
    collection = db.contacts
    collection.insert_one({'name':name, 'phone':phone, 'email':email, 'address':address, 'city':city, 'state':state, 'country':country})
    client.close()

def delete_data(contact):
    client = MongoClient('localhost',27017)
    db = client.BookBuddy
    collection = db.contacts
    try:
        collection.delete_one({'phone':contact})
    except:
        collection.delete_one({'email':contact})
    client.close()

def buddyexists(contact):
    contacts = get_data()
    found = False
    for i in contacts:
        if contact in i:
            found = True
            break
    return found

def search_data(contact):
    contacts = get_data()
    search_results = [["Name", "Phone", "Email", "Address", "City", "State", "Country"]]
    for i in contacts:
        if contact in i:
            search_results.append(i)
    return search_results

def update_data(contact, new_data):
    client = MongoClient('localhost',27017)
    db = client.BookBuddy
    collection = db.contacts
    try:
        collection.update_one({'phone':contact},{"$set": {'name':new_data['name'], 'phone':new_data['phone'], 'email':new_data['email'], 'address':new_data['address'], 'city':new_data['city'], 'state':new_data['state'], 'country':new_data['country']}})
    except:
        collection.update_one({'email':contact},{"$set": {'name':new_data['name'], 'phone':new_data['phone'], 'email':new_data['email'], 'address':new_data['address'], 'city':new_data['city'], 'state':new_data['state'], 'country':new_data['country']}})
    client.close()
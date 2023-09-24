from pymongo import MongoClient

# Constants
CONNECTION_STRING = "mongodb://localhost:27017"
DB_NAME = "project3"

def connect():
    try:
        client = MongoClient(CONNECTION_STRING)
        return client[DB_NAME]
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None

db = connect()

def troop_lookup():
    troop_number = input("Enter the troop number: ")
    troop = db.troops.find_one({'number': troop_number})
    if troop:
        print(f"Number: {troop['number']}\nFounding Date: {troop['founding_date']}\nCommunity: {troop['community']}\n")
        print("Scouts:")
        for scout in troop.get('scouts', []):
            print(scout.get('name'))
    else:
        print("Troop not found")

def scout_lookup():
    first_name = input("Enter the scout's first name: ")
    last_name = input("Enter the scout's last name: ")
    scouts = db.troops.find({
        'scouts.name': {'$regex': f'^{first_name} {last_name}$'}
    }, {
        'scouts.$': 1
    })
    
    for troop in scouts:
        scout = troop['scouts'][0]
        print(f"Name: {scout['name']}\nBirthday: {scout['birthday']}\nGrade Level: {scout['grade_level']}\n")
        print("Adults:")
        for adult in scout.get('adults', []):
            print(adult.get('name'))
        print("\nAllotments:")
        for allotment in scout.get('allotments', []):
            print(f"Date: {allotment['date']} | Cookie Type: {allotment['cookies']['type']} | Amount: {allotment['cookies']['amount']} | Total Value: {allotment.get('total_value', 0):.2f}")

def sales_report():
    troop_number = input("Enter the troop number: ")
    pipeline = [
        {'$match': {'number': troop_number}},
        {'$unwind': '$scouts'},
        {'$unwind': '$scouts.allotments'},
        {'$unwind': '$scouts.allotments.cookies'},
        {'$lookup': {'from': 'cookietypes', 'localField': 'scouts.allotments.cookies.cookietype', 'foreignField': 'name', 'as': 'cookie_type'}},
        {'$unwind': '$cookie_type'},
        {'$project': {'scout_name': '$scouts.name', 'totalvalue': {'$multiply': ['$scouts.allotments.cookies.boxes', {'$toDecimal': '$cookie_type.price'}]}}},
        {'$group': {'_id': '$scout_name', 'totalvalue': {'$sum': '$totalvalue'}}}
    ]
    
    result = db.troops.aggregate(pipeline)
    print(f"Sales Report for Troop {troop_number}\n")
    for row in result:
        print(f"{row['_id']} - Total Value: ${row['totalvalue']:.2f}\n")

def main():
    while True:
        print("\nMain Menu\n---------\n1. Troop Lookup\n2. Scout Lookup\n3. Sales Report\n4. Quit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            troop_lookup()
        elif choice == '2':
            scout_lookup()
        elif choice == '3':
            sales_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

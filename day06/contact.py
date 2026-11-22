import json
contacts = [
    {"name": "Sam", "phone": "21612345678"},
    {"name": "Lina", "phone": "21698765432"},
]
def save_contacts(filename,contacts) :
    with open(filename, "w") as f:
           
       json.dump(contacts, f, indent=2)
    
#save_contacts("contacts.json",contacts)

def load_contacts(filename) : 
        try :
            with open(filename) as f:
                
               return json.load(f)
               #return loaded 
            #loaded = load_contacts("contacts.json")
        except (FileNotFoundError, json.JSONDecodeError) :
                            
                 return[]

loaded = load_contacts("data.json")

#print(loaded==contacts)
def is_valid_phone(phone) :  
        if phone.isdigit() and (
        len(phone) == 8 or
        (len(phone) == 11 and phone.startswith("216")))  :

            return True
        else : 
            return False    
#print(is_valid_phone("58614523"))
def ask_phone():
    while True:
        phone = input("Phone: ").strip()

        if is_valid_phone(phone):
            if len(phone) == 8:
                phone = "216" + phone
            return phone
        else:
            print("Invalid phone, try again.")

#print(ask_phone())
def ask_name():
    while True:
        name = input("name: ").strip()
        if  name.isalpha() and name !=" " :              
             return name
        else:
            print("Invalid name, try again")
#print(ask_name()) 
def add_contact(contacts) :
  name=ask_name()
  phone = ask_phone()
  contacts.append({
        "name": name,
        "phone": phone
    })  
  return contacts

#ask_phone()
#ask_name()
#add_contact(loaded)
#save_contacts("contacts.json", loaded)
def list_contacts(contacts) :
    if  len(loaded) == 0:
        print("The contact list is empty")
    for i, contact in enumerate(contacts, 1):

        if contacts :

            print(i, contact)
        
#list_contacts(loaded)
def search_contacts(contacts) : 

    text = input("Search: ").strip().lower()
    for contact in contacts :

        if text in contact["name"].lower():

            print(contact)
            return contact

    print("No contact found.")
    return None
#search_contacts(loaded)
def delete_contact(contacts):

    result = search_contacts(contacts)

    if result is None:
        print("No matches")
        return contacts

    text = result["name"].strip().lower()

    for contact in contacts:
        if text == contact["name"].strip().lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break

    return contacts

#delete_contact(loaded)          
#save_contacts("contacts.json", loaded)
 
def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add a contact")
    print("2. List contacts")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Quit")
    
#show_menu()
def main(filename):
    contacts = load_contacts(filename)
    while True:
        show_menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            add_contact(contacts)
            save_contacts(filename,contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(filename,contacts)

        elif choice == "5":
            break
        else:
            print("Invalid choice.")
main("contacts.json")
import json
import logging
from pathlib import Path
from typing import TypedDict

#logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


logger = logging.getLogger(__name__)
class Contact(TypedDict):
    name: str
    phone: str
def save_contacts(filename,contacts) :
    with open(filename, "w") as f:
           
       json.dump(contacts, f, indent=2)
def load_contacts(path: Path) -> list[Contact]:
    try:
        contacts = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        logger.warning("contacts file not found, starting empty")
        return []
    except json.JSONDecodeError:
        logger.exception("contacts file is corrupted, starting empty")
        backup = path.with_suffix(".bak")
        path.rename(backup)
        logger.warning("corrupted file saved as %s", backup.name)
        return []
     
    return contacts 
#loaded = load_contacts(Path("contacts.json"))
#print(load_contacts(Path("contacts.json")))
def is_valid_phone(phone:int)-> bool :  
        if phone.isdigit() and (
        len(phone) == 8 or
        (len(phone) == 11 and phone.startswith("216")))  :
            return True
        else : 
            return False   
def ask_phone()->str:
    while True:
        phone = input("Phone: ").strip()

        if is_valid_phone(phone):
            if len(phone) == 8:
                phone = "216" + phone
            return phone
        else:
            logger.warning("invalid phone entered")

            print("Invalid phone, try again.")
#print(ask_phone())
def ask_name()-> str:
    while True:
        name = input("name: ").strip()
        if  name.isalpha() and name !=" " :              
             return name
        else:
            logger.warning("invalid name entered")
            print("Invalid name, try again")
def find_matches(contacts, text):
    matches = []
    for contact in contacts:
        if text in contact["name"].lower():
            matches.append(contact)
    return matches
def ask_choice(maximum):
    while True:
        try:
            number = int(input("Number to delete: "))
            if 1 <= number <= maximum:
                return number
        except ValueError:
            pass
        print("Invalid number, try again.")
#print(ask_name()) 
def add_contact(contacts) :
  name=ask_name()
  phone = ask_phone()
  contacts.append({
        "name": name,
        "phone": phone
    })
  logger.info("added contact %s", name)
  return contacts 

#ask_phone()
#ask_name()
#print(add_contact(loaded))
def list_contacts(contacts) :
    if  not contacts:

        print("The contact list is empty")
    for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")    
#list_contacts(loaded)
def search_contacts(contacts):
    text = input("Search: ").strip().lower()
    if not text:
        print("Please type something to search.")
        return
    matches = find_matches(contacts, text)
    if not matches:
        print("No contact found.")
        
        return
    for i, contact in enumerate(matches, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
#search_contacts(loaded)
def delete_contact(contacts):
    text = input("Name to delete: ").strip().lower()
    if not text:
        print("Please type a name.")
        return
    matches = find_matches(contacts, text)
    if not matches:
        
        print("No contact found.")
        return
    for i, contact in enumerate(matches, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    number = ask_choice(len(matches))
    chosen = matches[number - 1]
    contacts.remove(chosen)
    print("Contact deleted.")
    logger.info("deleted is %s",chosen["name"])

#delete_contact(loaded) 
def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add a contact")
    print("2. List contacts")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Quit")
    
#show_menu()
def main(filename):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    contacts = load_contacts(Path("contacts.json"))
    logger.info("program started")
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
    logger.info("program stopped")
main("contacts.json")
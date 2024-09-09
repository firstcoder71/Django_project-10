# contact book crud operation with search

contact_book=[
    {
        "name": "Rashed", 
        "phone": "01544551896", 
        "email":"Rashed@gmail.com",
        "area":"barisal",
        
    },
    {
        "name": "Roan", 
        "phone": "0171896", 
        "email":"Roman@gmail.com",
        "area":"sylet",
        
    },
    {
        "name": "Roki", 
        "phone": "01791896", 
        "email":"Roki@gmail.com",
        "area":"Dhaka",
        
    },
    {
        "name": "Roman", 
        "phone": "01741896", 
        "email":"Roman@gmail.com",
        "area":"Bogra",
        
    },
    {
        "name": "Roman", 
        "phone": "01741896", 
        "email":"Roman@gmail.com",
        "area":"Bogra",
        
    },
]
# create----contact -----
def create_contact():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    number = input("Enter your Phone number: ")
    area = input("Enter your area name: ")
    
    contact  = {
    "name": name,
    "phone": number,
    "email": email,
    "area": area
    }
    contact_book.append(contact)
    print("create contact successfully")
    
# create_contact()

#Read-------contact-----

def view_all_contact():
    for contact in contact_book:
        print(contact["name"],contact["phone"],contact["email"],contact["area"],
            sep="|")
        
#view_all_contact()

#Search------contact------

def search_contact():
    search_term = input("Enter the name of the contact you want to search: ")
    for contact in contact_book:
        if search_term.lower() in contact["name"].lower():
            print(f"Found: {contact['name']} - {contact['email']} - {contact['phone']} - {contact['area']}") 
            
#search_contact()


#Remove----contact--------

def remove_contact():
    search_term = input("Enter the name of the contact you want to remove: ")
    for index, contact in enumerate (contact_book):
        if search_term.lower() in contact["name"].lower():
            print(f"{index+1}.  {contact['name']} - {contact['phone']} - {contact['email']} - {contact['area']}")
            
    selected_index = input("Enter your contact to remove:  ")
    
    selected_index = int(selected_index) 
    
    contact_book.pop(selected_index-1)
    
    print("succesfully deleted this contact ")
    
#remove_contact()
#view_all_contact()

print(" \n Welcome to our Contact-book operation system")

menu_text = """
What do you want now ?

1. Create contact
2. View all contact
3. Search any contact
4. Remove any contact
5. exit

"""

while True:
    print(menu_text)
    choice = input("Enter your choice: ")
    
    if choice  == "1":
        create_contact()
    elif choice ==  "2":
        view_all_contact()
    elif choice ==  "3":
        search_contact()
    elif choice ==  "4":
        remove_contact()
    elif choice == "5":
        print("Thank you for using our contact book system")
        break
    else:
        print("Invalid choice. Please choose a valid option.") 

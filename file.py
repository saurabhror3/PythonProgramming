# # Step 1: Create an empty list to store contact information
# contacts = []

# # Step 2: Prompt the user to enter contact names and phone numbers
# print("Enter contact details. Type 'done' when finished.\n")

# while True:
#     name = input("Enter contact name: ")
#     if name.lower() == 'done':
#         break

#     phone = input("Enter phone number: ")
#     if phone.lower() == 'done':
#         break

#     # Step 3: Store each contact as a tuple (name, phone)
#     contact = (name, phone)

#     # Step 4: Add the contact to the contact list
#     contacts.append(contact)

# # Step 5: Write contacts to contacts.txt
# with open('contacts.txt', 'w') as file:
#     for name, phone in contacts:
#         file.write(f"Name: {name}, Phone: {phone}\n")

# # Step 6: Read the contents of contacts.txt and print it
# print("\nSaved contacts:")
# with open('contacts.txt', 'r') as file:
#     content = file.read()
#     print(content)

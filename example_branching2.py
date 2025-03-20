places = ["Colorado", "Washington DC", "Vegas", "OBX"]
wishlist = []
#user Inputed Location
user_input = input("Enter a place you've travelled to: ")

#If Statement, Have I been to the user's place?
if user_input in places:
    print(f"Yes, I've been too {user_input}.")

else:
    print(f"I have not yet been too {user_input}.")
    wishlist.append(user_input)

print(f"My wishlist: {wishlist}")
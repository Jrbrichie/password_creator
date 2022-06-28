import password_creator as p  # importing password_creator file

p1 = p.Password_Creator()
password = ""

p1.set_has_letters(input("Does password have letters (Y/N)? ").upper() == "Y")
p1.set_has_numbers(input("Does password have numbers (Y/N)? ").upper() == "Y")
p1.set_has_symbols(input("Does password have symbols (Y/N)? ").upper() == "Y")

length = int(input("Enter the length of the password: "))
while not p1.valid_length(length):
    length = int(input("Invalid length! Enter another length: "))

p1.set_length(length)

must_include = input("Enter a phrase you want to include in the password (NA if none): ")
while not p1.valid_must_include(must_include):
    must_include = input("Invalid phrase! Enter another phrase (NA if none): ")

p1.set_must_include(must_include)
create_new_password = True

while create_new_password:
    p1.create_password()
    print("Password:", p1.password)
    create_new_password = input("Create new password (Y/N)? ").upper() == "Y"

print("\nYour password is:", p1.password)








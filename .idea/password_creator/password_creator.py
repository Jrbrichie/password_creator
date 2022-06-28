import csv, random as r, validators
import passwords_writer

class Password_Creator:

    """
    Class Variables
    """
    password = ""
    length = 0
    email = ""
    wesbite_url = ""

    has_letters = False
    has_numbers = False
    has_symbols = False
    has_must_include = False
    must_include = ""

    pw = password_writer()
    f = open("passwords.csv", "w")
    writer = csv.writer(f)
    valid_characters = []


    """
    Class Setters
    """
    # sets has letters as true
    def set_has_letters(self, boolean):
        self.has_letters = boolean

    # sets had numbers as true
    def set_has_numbers(self, boolean):
        self.has_numbers = boolean

    # sets symbols as true
    def set_has_symbols(self, boolean):
        self.has_symbols = boolean

    # sets phrase that must be included
    def set_must_include(self, string):
        if string != "NA" and self.valid_must_include(string):
            self.has_must_include = True
            self.must_include = string
            return "Valid Must Included String"
        return "Invalid Must Included String, Try Again"

    # sets length of password
    def set_length(self, length):
        if(self.valid_length(length)):
            self.length = length
            return "Valid Length"
        return "Invalid Length, Try Again"

    # sets website url for password
    def set_website_url(self, url):
        if(self.valid_website_url(url)):
            self.wesbite_url = url
            return "Valid Website URL"
        return "Invalid Website URL, Try Again"

    # sets email for password
    def set_email(self, email):
        if(self.valid_email(email)):
            self.email = email
            return "Valid Email"
        return "Invalid Email, Try Again"


    """
    Checks if variable exists
    """
    # returns True if must_include is valid
    def valid_must_include(self, string):
        return len(string) <= self.length

    # returns True if password length is valid
    def valid_length(self, length):
        return 0 < length <= 256

    # creates array of valid characters
    def valid_choices(self):
        if self.has_letters:
            self.valid_characters.append("letters")
        if self.has_numbers:
            self.valid_characters.append("numbers")
        if self.has_symbols:
            self.valid_characters.append("symbols")

    # checks if the email is valid (no spaces, has @, no illegal characters)
    def valid_email(self, email):
        if ("@" in email) and (" " not in email) and (len(email) >= 64 and len(email) > 0):
            for i in "!#$%&'*+-/=?^_`{|}~(),:;<>@[\]":
                if i in email:
                    return False
            for i in range(10):
                if i in email:
                    return False
            return True
        else:
            return False

    # checks if the website url is valid
    def valid_website_url(self, url):
        return validators.url(url)


    """
    Adds to variable
    """
    # adds letters to password
    def add_letters(self):
        letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        return letters[r.randint(0, 51)]

    # adds numbers to password
    def add_numbers(self):
        return str(r.randint(0, 9))

    # adds symbols to password
    def add_symbols(self):
        symbols = "!{}[]()-.?_`;:#^%*&+="
        return symbols[r.randint(0, 20)]

    # runs add functions
    def add_characters(self, character):
        if character == "letters":
            return self.add_letters()
        elif character == "numbers":
            return self.add_numbers()
        elif character == "symbols":
            return self.add_symbols()


    """
    Creates a password according to the specifications above made by the user
    :returns the self.password variable 
    """
    def create_password(self):
        self.password = ""
        self.valid_characters = []
        if self.has_must_include and len(self.valid_characters) != 0:
            self.valid_choices()
            must_include_index = r.randint(0, self.length - len(self.must_include) - 2)

            while len(self.password) <= self.length - len(self.must_include) - 1:
                character = self.valid_characters[r.randint(0, len(self.valid_characters) - 1)]
                self.password += self.add_characters(character)

            first_part = self.password[0:must_include_index]
            last_part = self.password[must_include_index::]
            self.password = first_part + self.must_include + last_part
        elif self.has_must_include:
            self.password = self.must_include
        else:
            self.password = 12345678  # default password

        return self.password


    # saves password to password.txt
    def save_password(self, password, email, url):
        if(not self.pw.has_duplicates(url)):
            self.writer.writerow(password + "," + email + "," + url)
            return "Password saved successfully"







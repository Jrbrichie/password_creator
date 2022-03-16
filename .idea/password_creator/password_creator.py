import random as r


class password:
    password = ""
    length = 0
    has_letters = False
    has_numbers = False
    has_symbols = False
    has_must_include = False
    must_include = ""
    valid_characters = []


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
        if string != "NA":
            self.has_must_include = True
            self.must_include = string

    # sets length of password
    def set_length(self, length):
        self.length = length

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

    # returns password randomly based on options chosen
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

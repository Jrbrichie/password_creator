import csv, password_creator, password_creator_gui, passwords.csv, pandas as pd

class Passwords_Writer:

    """
    Class Varibles
    """
    passwords = "passwords.csv"
    pc = password_creator.Password_Creator()

    # readers, writers
    output = open(passwords, "wb")
    input = open(passwords, "rb")
    writer = csv.writer(output)
    reader = csv.reader(passwords, delimeter=",")
    pd_reader = pd.read_csv(passwords)
    pd_col_reader = pd.read_csv(self.passwords, usecols=col_list)


    """
    Save/delete password combination (password, email, and website url)
    """
    # saves password to password.txt
    def save_password_combination(self, password, email, url):
        self.writer.writerow(password + ',' + email + ',' + url)

    # deletes password from password.txt using wesbite url
    def delete_password_cobination(self, url):
        if(self.pc.valid_website_url(url)):
            i = 0
            for i in self.reader:
                if url in self.reader:
                    # reads csv file using the pandas module, searches the URL row and deletes the row contianing url
                    self.pd_reader.set_index("URLs", inplace=True).drop(url)
                i += 1

    # deletes all password combinations with the same password
    def delete_password_cobination_all_password(self, password):
        if(self.exists(password, "Passwords")):
            i = 0
            for row in self.reader:
                if password in row:
                    self.pd_reader.set_index("Passwords", inplace=True).drop(password)
        else:
            return "Could not delete all same password combination" \
                   "with password because password does not exist."


    # deletes all password combinations with the same email
    def delete_password_combination_all_email(self, email):
        if(self.exists(email, "Emails")):
            i = 0
            for row in self.reader:
                if email in row:
                    self.pd_reader.set_index("Emails", inplace=True).drop(email) # deletes all elments in the email column
        else:
            return "Could not delete all same password combination" \
                   "with email because email does not exist."

    # checks if password exists using password, website or email
    def exists(self, str, col_name):
        column = self.pd_col_reader[col_name]
        return str in column

    # searches csv file to find index of element
    def find_index(self, str, col_name):
        i = 0
        for j in self.pd_col_reader[col_name]:
            if j == str:
                return i
            i += 1


    """
    Edit and Get Password, Email, or Website URL
    """
    # edits password and recieves and new password and url of website as input
    def edit_element(self, new_element, url, col_name):
        if(self.exists(url, "URLs")):
            index = self.find_index(new_element, col_name)
            #locates the element in index and column password and replaces it with new_password
            self.pd_reader.loc[index , "Passwords"] = new_element
            return col_name[:-1], "sucessfully replaced to", new_element
        else:
            return col_name[:-1] + ":", new_element, "unsucessfully replaced"

    # edits all same passwords, receives new_password and url of website as input
    def edit_same_element(self, new_element, old_element, col_name):
        if(self.exists(old_element, col_name)):
            p_col = self.pd_col_reader[col_name]
            i = 0
            j = 0
            edited = False

            for p in p_col:
                if p == old_element:
                    self.pd_reader.loc[i, "Passwords"] = new_element
                    edited = True
                    j += 1
                i += 1
            return j, "passwords, formerly", old_element, "replaced with", new_element
        else:
            return col_name[:-1] + ":", old_element, "could not be replaced because it does not exist"


    # gets all matching passwords and returns full password, email and url
    def get_all_same_element(self, element):
        same_elements = ""
        if(self.exists(element)):
            for row in self.pd_reader:
                if element in row:
                    same_elements += row
            return "Password Combinations Containing the Same Passwords\n" + same_elements
        else:
            return "Could not get all password combinations because password does not exist"


    # gets all passwords
    def get_all_element(self, col_name):
        column = ""
        if self.find_index(0, col_name) != None:
            for p in self.pd_col_reader[col_name]:
                column += p + '\n'
            return column
        else:
            return "Column list is empty"

    # checks for duplicate passwords
    def has_duplicates(self, url):
        for i in self.pd_col_reader["URLs"]:
            if i == url:
                return True
        return False
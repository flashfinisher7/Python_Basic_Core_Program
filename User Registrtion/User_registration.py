import re
from typing import Pattern
print ("\t\t\t\tThis is User Registration problem")
#UC1
def Name_First(first_name):
    Pattern_first_name=re.compile("^[A-Z][a-z]{2,}$")
    if Pattern_first_name.fullmatch(first_name):
        return True
    else:
        return False
#UC2
def Name_Last(last_name):
    Pattern_last_name=re.compile("^[A-Z][a-z]{2,}$")
    if Pattern_last_name.fullmatch(last_name):
        return True
    else:
        return False
#UC3
def Email_Id(email_id):
    Pattern_of_email_1=re.compile("^[a-z]{3,}\@bl\.co$")
    pattern_of_email_2=re.compile("^[a-z]{3,}\.[a-z]{3,}\@bl\.co\.in$")
    if Pattern_of_email_1.fullmatch(email_id) or pattern_of_email_2.fullmatch(email_id):
        return True
    else:
        return False
#UC4
def Mobile_Number(mobile_number):
    Pattern_of_mobile=re.compile("^\+?[1-9][0-9]\s[7-9][0-9]{9}$")
    if Pattern_of_mobile.fullmatch(mobile_number):
        return True
    else:
        return False
#UC5
def User_Password(password):
    Pattern_of_password=re.compile("^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$")
    if Pattern_of_password.fullmatch(password):
        return True
    else:
        return False 
database = 'data.txt'

infile = open(database, "r")

def another_account():
    """
    Asks the user if they want to run the program again
    """
    aa=input("Is there another account you would like to create or check? (yes/no) > ").lower()
    if aa == "yes":
        bank()
    elif aa == "no":
        print("Thank you for using Kenton's Bank")
        return False
    else:
        print('Please answer with "yes" or "no"!')
        another_account()

def bank_info(passw):
    """
    Function that gives the user their bank info
    """
    with open(database,'r') as read_obj:
        for line in read_obj:
            if passw in line:
                info = line.split(',')
    print(f"Name: {info[2]}\nBalance: {info[3]}")
    

def check_password():
    """
    Function that see if the password is in the database
    """
    passw = input("Please enter your password > ")
    with open(database,'r') as infile:
        for line in infile:
            psplit = line.strip().split(',')
            if passw == psplit[1]:
                return bank_info(passw)
        print("Username is not in our system\nPlease try again!")
        return check_password()
    
def check_username():
    """
    Function that checks if the username is in the database
    """
    uname = input("Please enter your username > ")
    with open(database,'r') as infile:
        for line in infile:
            usplit = line.strip().split(',')
            if uname == usplit[0]:
                return True
        print("Username is not in our system\nPlease try again!")
        return check_username()

def create_account():
    """
    Function that creates an account
    """
    a = input("What would you like your username to be? > ")
    b = input("What would you like your password to be? > ")
    c = input("What is your full name? > ")
    d = input("How much money would you like to deposit? > ")
    new_line = (f"\n{a},{b},{c},{d}")
    outfile = open(database, 'a')
    outfile.writelines(new_line)

def create_or_sign():
    """
    Asks user if they want to sign into an account or create one
    """
    si = input("\nWould you like to create an account or sign in? (create/sign in) > ").lower()
    if si == "create":
        create_account()
    elif si == "sign in":
        return
    else:
        print('Please answer "create" or "sign in"!')
        create_or_sign()

print("Hi! Welcome to Kenton's Bank")
def bank(): 
    """
    Function that runs all the code 
    """
    user = False
    while user is False:
        create_or_sign()   
        cu = check_username()
        if cu == True:
            check_password()
        aa=another_account()
        if aa is False:
            break
        
bank()

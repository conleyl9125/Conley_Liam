cPassword="fake123"
cUser="liam123"
iUser=input("what is your username?")
iPass=input("what is your password?")

def passCheck():
    if cUser==iUser and cPassword==iPass:
        print("you are granted access")
    if cUser==iUser and cPassword!=iPass:
        print("your password is wrong")
    if cUser!=iUser and cPassword==iPass:
        print("your username is wrong")
    if cUser!=iUser and cPassword!=iPass:
        print("your username and password are incorrect")
passCheck()


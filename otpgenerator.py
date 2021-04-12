import random
print("Welcome to OTP Generator")
#random.randint will return a number between 000000 to 100000
otp=random.randint(00000,20000)

#enter username
username=input("Please enter your username:")
print("Hello!! \n How are you ", username)
print("Your otp is", otp)
password=input("Enter your OTP is - ")
#check conditions
if password==str(otp):
    print("Login Success! \n Thank you" , username , "for working with us")
else:
    password!=str(otp)
    print("Login Failed!\n Try Again")

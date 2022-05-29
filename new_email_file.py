auth_email = input("Enter your email for Authentication:- ")
filename = open("email.txt")

if(auth_email in filename.read()):

    import send_email as se
    from send_email import *

else:
    print("Email not Found!!!")
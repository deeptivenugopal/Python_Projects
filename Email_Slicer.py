#Get email as input
email = input("What is your email id: ").strip()

#Get the username
username = email[:email.index("@")]

#Get the domain name
domain = email[email.index("@")+1:]

print("Your username is {} and domain name is {}".format(username,domain))

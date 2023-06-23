email = input("Enter your email :- ")

def username_suggestion(email):
 name = email.split("@")
 print(f'The suggested username is {name[0]}')
 print(f'The domain of user email is {name[1]}')

username_suggestion(email)
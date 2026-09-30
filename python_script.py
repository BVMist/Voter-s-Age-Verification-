
#A Simple Voter Eligibility Verification System
def verify(age):
    min_voting_age = 18
    msg = f'{"You are not eligible to vote." if age<min_voting_age else "Welcome. Voting Registration Initializing..."}'
    return msg

while True:
    age = input('How old are you? ')
    try:
        age = int(age)
    except:
        print('Invalid Input.')
        continue
    print(verify(age))

import re

def validate(password):
    # At least one number, one uppercase, one special symbol and 8 to 18 Characters
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    match_re = re.compile(pattern)
    result = re.search(match_re, password)
    if result:
        print("Valid Password")
    else:
        print("Invalid Password")

# validate('XdsE83&!')

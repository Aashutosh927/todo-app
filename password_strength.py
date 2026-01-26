password = input("Enter the password: ")
result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['upper-case'] = uppercase

lowercase = False
for i in password:
    if i.islower():
        lowercase = True

result['lower-case'] = lowercase

print(result)

if all(result.values()):
    print("Strong Password")
else:f
    print("Weak Password")
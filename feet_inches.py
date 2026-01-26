from modules.converters import convert
from modules.parsers import parse

feet_inches = input("Enter feet and inches:")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small to ride the slide.")

else:
    print("Kid can ride the slide.")


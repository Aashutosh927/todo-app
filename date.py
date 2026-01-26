date = input("Enter today's date: ")
mood = input("Enter the rate of your mood you would like to give: ")
thoughts = input("Enter your thoughts: \n ")

with open(f"files/{date}.txt", "w") as file:
    file.write(mood + '\n')
    file.write(thoughts)
member = input("Enter the name: ")

file = open("files/members.txt", 'r')
existing_member = file.readlines()
file.close()

existing_member.append( member + "\n")
file = open("files/members.txt", 'w')
file.writelines(existing_member)
file.close()
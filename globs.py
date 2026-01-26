import glob
my_files = glob.glob("files/*.txt")

for filepaths in my_files:
    with open(filepaths, 'r') as file:
        print(file.read().upper())
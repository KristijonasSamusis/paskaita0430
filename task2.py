file_name = input("Enter file name.")

while True:
    with open(f"{file_name}.txt", 'a') as file:
        file.write(f"{input('Enter nre line:' )}\n")
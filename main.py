import csv
import os


# List all CSV files in the current directory
print("****************************************")
print("Available CSV files:")
for file in os.listdir():
    if file.endswith(".csv"):
        print(file)
print("****************************************")

# Prompt the user for the CSV file name
print()
csv_file = input("Enter the CSV file name (with .csv extension): ")
print()

try:
    f = open(csv_file, "x")
except FileExistsError:
    print("File already exists. Opening the file.")



def read_contacts():
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def write_contacts():
    f = open("story.txt", "w")
    f.write(input("Write something: "))
    f.write("\n")

def append_contacts():
    f = open("story.txt", "a")
    f.write(input("Write something: "))
    f.write("\n")



option = ""
while option != "4":
    print("Select an option: \n1. Read \n2. Write \n3. Append \n4. Select Different Contact Book \n5. Exit")
    option = input(">> ")

    if option == "1":
        read_contacts()

    elif option == "2":
        write_contacts()

    elif option == "3":
        append_contacts()

    elif option == "4":

        print("****************************************")
        print("Available CSV files:")
        for file in os.listdir():
            if file.endswith(".csv"):
                print(file)  
        print("****************************************")

        print()
        csv_file = input("Enter the CSV file name (with .csv extension): ")
        print()

    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
    
    input("Press enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

        
f.close()



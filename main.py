import csv
import os

def list_csv_files():
    """List all CSV files in the current directory."""
    print("****************************************")
    print("Available CSV files (Phone Books):")
    for file in os.listdir():
        if file.endswith(".csv"):
            print(file)
    print("****************************************")

def get_csv_file():
    """Prompt the user for the CSV file name and ensure it has a .csv extension."""
    csv_file = input("Enter the CSV file name (with .csv extension): ")
    if not csv_file.endswith(".csv"):
        csv_file += ".csv"
    return csv_file

def create_csv_file(csv_file):
    """Create a new CSV file with headers if it does not exist."""
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone Number"])
            print("File created successfully.")
    else:
        print("File already exists. Opening the file.")

def read_contacts(csv_file):
    """Read and display contacts from the CSV file."""
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def write_contacts(csv_file):
    """Write a new contact to the CSV file."""
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        writer.writerow([name, phone])

def append_contacts(csv_file):
    """Append a new contact to the CSV file."""
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        writer.writerow([name, phone])

# Main program starts here
list_csv_files()  # List all available CSV files
csv_file = get_csv_file()  # Get the CSV file name from the user
create_csv_file(csv_file)  # Create the CSV file if it does not exist

option = ""
while option != "5":
    # Display menu options
    print("Select an option: \n1. Read \n2. Write \n3. Append \n4. Select Different Contact Book \n5. Exit")
    option = input(">> ")

    if option == "1":
        read_contacts(csv_file)  # Read contacts from the CSV file
    elif option == "2":
        write_contacts(csv_file)  # Write a new contact to the CSV file
    elif option == "3":
        append_contacts(csv_file)  # Append a new contact to the CSV file
    elif option == "4":
        list_csv_files()  # List all available CSV files
        csv_file = get_csv_file()  # Get the CSV file name from the user
        create_csv_file(csv_file)  # Create the CSV file if it does not exist
    elif option == "5":
        print("Goodbye!")  # Exit the program
        break
    else:
        print("Invalid option")  # Handle invalid menu option
    
    input("Press enter to continue...")  # Wait for user input before clearing the screen
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

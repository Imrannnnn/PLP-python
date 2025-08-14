"""File Read & Write Challenge 🖋️: Create a program that reads a file and 
writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if 
it doesn’t exist or can’t be read."""

try: 
    with open('imran.txt', 'r') as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    print("File is not found")




try:
    with open("management.txt" 'w') as file:
        file.write("This is a full managment file for all staff and client")
except Exception as e:
    print(f"There's an error reading this file {e}")



#Error Handling Lab 
filename = input("Enter name of file please")

try:
    with open(filename, 'r', encoding='utf8') as file:
        show = file.read()
        print(show)

except FileNotFoundError:
    print("File is not found")


try:
    with open(filename, 'w') as file:
        file.write("Hello Nasiru Imran")
    
except Exception as e:
    print("could not writeFile")
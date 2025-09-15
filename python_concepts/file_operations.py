file1 = "test1.txt"
fileptr = open(file1, 'w')  # Open file in write mode
fileptr.write("Hello, World!\n")  # Write to file
fileptr.write("This is a test file.\n")
#fileptr.close()  # Close the file
# Append mode  
fileptr = open(file1, 'a')  # Open file in append mode
fileptr.write("Appending a new line.\n")  # Append to file
fileptr.close()  # Close the file
# Read mode
fileptr = open(file1, 'r')  # Open file in read mode
content = fileptr.read()  # Read the entire file
print(content)  # Print file content
fileptr.close()  # Close the file
# Read line by line
fileptr = open(file1, 'r')  # Open file in read mode
for line in fileptr:
    print(line.strip())  # Print each line without extra newline
fileptr.close()  # Close the file

# Using 'with' statement for file operations
# File is automatically closed after the block
with open(file1, 'r') as fileptr:
    content = fileptr.read()
    print("Using 'with' statement:")
    print(content)

# Writing multiple lines using writelines()
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("test2.txt", 'w') as fileptr:
    fileptr.writelines(lines)   
with open("test2.txt", 'r') as fileptr:
    content = fileptr.read()
    print("Content of test2.txt:")
    print(content)

# Handling file not found error
try:
    with open("non_existent_file.txt", 'r') as fileptr:
        content = fileptr.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.") 

'''# Handling permission error
try:
    with open("/root/protected_file.txt", 'r') as fileptr:
        content = fileptr.read()
        print(content)
except PermissionError:
    print("Error: Permission denied.")

# Handling other IO errors
try:
    with open("/invalid_path/file.txt", 'r') as fileptr:
        content = fileptr.read()
        print(content)
except IOError as e:
    print(f"IOError: {e}")

# General exception handling
try:
    with open("another_non_existent_file.txt", 'r') as fileptr:
        content = fileptr.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")

# Always ensure files are closed properly
fileptr = None
try:
    fileptr = open("yet_another_non_existent_file.txt", 'r')
    content = fileptr.read()
    print(content)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if fileptr:
        fileptr.close()
'''
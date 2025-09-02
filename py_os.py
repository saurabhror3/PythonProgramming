import os

# Step 1: Create a new directory named TestDirectory
directory_name = "TestDirectory"
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")

# Step 2: Create a new file named testfile.txt and write a message
file_path = os.path.join(directory_name, "testfile.txt")
with open(file_path, "w") as file:
    file.write("Hello, this is a test file.")
print(f"File 'testfile.txt' created and written to.")

# Step 3: List all files and directories in TestDirectory
print(f"\nContents of '{directory_name}':")
contents = os.listdir(directory_name)
for item in contents:
    print("-", item)

# Step 4: Rename testfile.txt to renamedfile.txt
new_file_path = os.path.join(directory_name, "renamedfile.txt")
os.rename(file_path, new_file_path)
print("\nFile renamed to 'renamedfile.txt'.")

# Step 5: Delete renamedfile.txt and the TestDirectory
os.remove(new_file_path)
print("File 'renamedfile.txt' deleted.")

os.rmdir(directory_name)
print(f"Directory '{directory_name}' deleted.")

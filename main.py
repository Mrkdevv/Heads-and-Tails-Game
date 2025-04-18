import os


print("WELCOME TO FILTER YOUR PC PROGRAM".upper())
print("Choose what filtration you want in your disk C:\n")

print("1. Filter by file extension (e.g. .txt, .jpg, .pdf)")
print("2. Filter by file size (e.g. files greater than 1MB)")
print("3. Filter by folder or file name")
print("4. Show all files and folders")
print("5. Exit")

try:
    User_choice = int(input("\nEnter your variant: "))
except ValueError:
    print("Please enter number!")
except Exception as e:
    print(f"Error! {e}")



def choice_one():
    extension = input("Enter extension (e.g. .txt): ")
    print(f"Filtering by {extension}...")

    for root,dirs,files in os.walk("C:\\"):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root,file))
def choice_two():
    size = int(input("Min size in bytes (e.g. 1000000 for 1MB): "))
    print(f"Filtering files > {size} bytes...")

def choice_three():
    name = input("Enter a name of the file | folder: ")
    print(f"Filtering by name containing '{name}'...")

def choice_four():
    print("Showing all files in C:\\ ...")

def choice_five():
    print("Exiting...")










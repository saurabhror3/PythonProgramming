class CustomFileException(Exception):
    """Custom exception for file related operations"""
    pass

content = ""
f = None
try :
    f = open('input.txt', 'r')
    print("The content of the file is displayed below : ")
    content = f.read()
    print(content)
except FileNotFoundError as e:
    raise CustomFileException(f"Failed to open file. Original error: {e}")
finally :
    if f is not None:
        f.close()
    print("File is closed")

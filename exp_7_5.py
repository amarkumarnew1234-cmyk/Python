'''5. Create multiple suitable exceptions for a file handling program.  '''
try:
    filename=input("Enter file name: ")
    file=open(filename,"r")

    numbers=file.readlines()
    file.close()

    total=0
    for num in numbers:
        total+=int(num.strip())

    print("Sum of numbers:",total)

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

except ValueError:
    print("Error: File contains non-integer data")

except Exception as e:
    print("Unexpected Error:",e)
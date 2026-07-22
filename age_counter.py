try:
    age= int(input("Enter the age:"))
    print("Age:", age)
except ValueError:
    print("Invalid input")

finally:
    if age%2 == 0:
        print("Age is even")
    else:
        print("Age is odd")


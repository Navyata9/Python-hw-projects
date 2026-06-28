def shutdown(user):
    if user== "yes":
        print("shutting down system")
    elif user== "no":
        print("abort shutdown")
    else:
        print("sorry")

choice= input("Do you want to shutdown (yes/no):")

shutdown(choice)
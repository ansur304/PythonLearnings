print("Hello, Welcome to Car Game! ")
options = '''Available Options 
help  - to get available Options
start - to start Car
stop  - to stop the car
exit  - Exit the Game'''
while True:
    option = input("Enter your option >> ").lower()
    if option == "help":
        print(options)
    elif option == "start":
        print("Car has started! Cheers")
    elif option == "stop":
        print("Car is stopped!")
    elif option == "exit":
        print("Exiting the Game")
        break
    else:
        print("I do not understand the option")


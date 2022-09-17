from calls import Local, National, International

option = 0 
extra = 0 # Extra fare 
bill = 100 # Monthly fare
calls = 0 # Amount of calls made in a month
localCalls = 0 # Amount of local calls made in a month
nationals = 0 # Amount of national calls made in a month
internationals = 0 # Amount of international calls made in a month
totalMinutes = 0 # Amount of minutes called in a month
minutes = 0

provinces = {
    # dictionary to link the provinces with a fare
    0.3 : ["cordoba", "entre rios", "la pampa", "santa fe", "san luis", "mendoza", "neuquen"],
    0.4 : ["corrientes", "santiago del estero", "rio negro", "la rioja", "san juan", "tucuman"],
    0.5 : ["chubut", "santa cruz", "tierra del fuego", "catamarca", "misiones", "chaco", "formosa", "salta", "jujuy"]
}
countries = {
    # dictionary to link the countries with a fare
    0.8 : ["uruguay", "brasil", "chile"],
    0.9 : ["paraguay", "bolivia", "peru"],
    1.0 : ["ecuador", "peru", "venezuela", "colombia"]
}

def getExtra(dic, fare1, fare2, fare3, choice):
    # Function to get the fare considering the province/country of the call
    fare = 0
    if choice in dic[fare1]:
        fare = fare1
    elif choice in dic[fare2]:
        fare = fare2
    elif choice in dic[fare3]:
        fare = fare3
    else:
        fare = 0
        print("Check if you wrote it correctly please")
    return fare



while option != 3:
    try: 
        print("What do you want to do? ")
        print("1. Register a phone call")
        print("2. View bills")
        print("3. Exit")
        option = int(input("Please choose an option: "))

        if option == 1:
            call = ""
            while call != "a" and call != "b" and call != "c":
                print("Which type of call do you want to register?")
                print("a. Local")
                print("b. National")
                print("c. International (South America)")
                call = input("Please select one option: ")

                if call == "a":
                    minutes = int(input("Write the duration of the call: "))
                    workingDay = ""
                    while workingDay != "y" and workingDay != "n":
                        # Ask if it is a working day to get the fare
                        workingDay = input("Is it a working day? (y/n): ").lower()
                        if workingDay == "y":
                            time = ""
                            while time != "y" and time != "n":
                                # Ask if it is between 08 and 20hs to get the fare
                                time = input("Is it between 08:00 and 20:00? (y/n): ").lower()
                                if time == "y":
                                    extra = 0.2
                                elif time == "n":
                                    extra = 0.1
                                else:
                                    print("Invalid option")
                        elif workingDay == "n":
                            extra = 0.1
                        else:
                            print("Invalid option")
                    local = Local(minutes, extra) # Instance the Local class
                    print(local) # Show the information of that call
                    bill += local.getBill(minutes, extra) # Get the bill for that call
                    calls += 1
                    localCalls += 1
                    totalMinutes += minutes
                    extra = 0 # Reset value
                    

                elif call == "b":
                    minutes = int(input("Write the duration of the call: "))
                    while extra == 0:
                        province = input("Choose a province: ").lower()
                        extra = getExtra(provinces, 0.3, 0.4, 0.5, province)
                    national = National(minutes, extra, province) # Instance the National class
                    print(national) # Show the information of that call
                    bill += national.getBill(minutes, extra) # Get the bill for that call
                    calls += 1
                    nationals += 1
                    totalMinutes += minutes
                    extra = 0 # Reset value


                elif call == "c":
                    minutes = int(input("Write the duration of the call: "))
                    while extra == 0:
                        country = input("Choose the country: ")
                        extra = getExtra(countries, 0.8, 0.9, 1.0, country)
                    international = International(minutes, extra, country) # Instance the International class
                    print(international) # Show the information of that call
                    bill += international.getBill(minutes, extra) # Get the bill for that call
                    calls += 1
                    internationals += 1
                    totalMinutes += minutes
                    extra = 0 # Reset value
 

                else:
                    print("Please select a valid option")
                
                

        elif option == 2:
            # Show bill
            print("*** This is your bill ***")
            print(f"Total calls made: {localCalls + nationals + internationals}")
            print(f"Locals: {localCalls} \nNationals: {nationals} \nInternationals: {internationals}")
            print(f"Total minutes: {totalMinutes}")
            print(f"To pay: ${bill}")
            

        elif option != 1 and option != 2 and option != 3:
            print("Please enter a valid option")


    except Exception as e: 
        # Capture the exception and show the error
        print(f"An error ocurred: {e}.\nThe option must be a number") 
        option = None  

print("Closing...")
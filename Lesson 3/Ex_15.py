def euroToSwissFranc():
    conversion_rate = 0.95905482
    euroAmount = int(input("Enter the euro you have: "))
    print(f"You will get {euroAmount*conversion_rate} Swiss Francs")

euroToSwissFranc()
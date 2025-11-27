def convert_temp():
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    choice = input("Select option: ")
    temp = float(input("Enter temperature value: "))
    if choice == "1":
        print("Fahrenheit:", (temp * 9/5) + 32)
        print("Kelvin:", temp + 273.15)
    elif choice == "2":
        print("Celsius:", (temp - 32) * 5/9)
        print("Kelvin:", ((temp - 32) * 5/9) + 273.15)
    elif choice == "3":
        print("Celsius:", temp - 273.15)
        print("Fahrenheit:", (temp - 273.15) * 9/5 + 32)
    else:
        print("Invalid choice")
convert_temp()

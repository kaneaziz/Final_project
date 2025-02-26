def get_user_input():
    """
    Collects user input for daily screen time and profile selection.
    """
    print("\nWelcome to the Digital Detox Tracker!")
    print("Please select your profile:")
    print("1. Student")
    print("2. Working Professional")
    print("3. Retired/Unemployed")
    while True:
        try:
            profile_choice = int(input("Choose a number (1-3): "))
            if profile_choice not in [1, 2, 3]:
                print("Invalid choice. Please choose a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    while True:
        try:
            total_time = float(input("What is your total daily screen time (in hours)? "))
            if total_time < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    return total_time

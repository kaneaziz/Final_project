#Import the functions from the separate files
from User_Input import get_user_input
from History import save_user_history, show_history
from Analysis import compare_to_average, analyze_health_impact
from Wellbeing import digital_wellbeing_score
from Activities import user_interests_and_plan, screen_time_projection

def main():
    """
    Runs the Digital Detox Tracker by calling various models from other files.
    """

    total_time = get_user_input() #Step 1: Get the input of the user
    save_user_history(total_time) #Step 2: Save the history of the screen time
    compare_to_average(total_time) #Step 3: Compares the user's screen time to that of the average user (globally)
    analyze_health_impact(total_time) #Step 4: Analyzes the health impact
    digital_wellbeing_score(total_time) #Step 5: Calculate's the digital wellbeing score according to screen time

    # Ask how many hours the user wants to reduce
    while True:
        try:
            reduce_hours = float(input("How many hours per day do you want to reduce? "))
            if reduce_hours < 0 or reduce_hours > total_time:
                print("Please enter a valid number of hours that you can realistically reduce.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    # Call to generate custom plan based on interests
    user_interests_and_plan(reduce_hours)

    # Call to show what could have been achieved with the saved time
    screen_time_projection(reduce_hours)

    # Show previous history and trends
    show_history()

    print("\nDigital Detox Tracker Complete! Stay mindful of your screen time!")

if __name__ == "__main__":
    main()

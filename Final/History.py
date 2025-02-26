import datetime

def save_user_history(total_time):
    """
    Saves user screen time history to a log file.
    """
    with open("history_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Screen Time: {total_time:.1f} hours\n")

def show_history():
    """
    Displays previous screen time history if the user wants to see it.
    Additionally, it calculates weekly and monthly screen time trends
    to provide insights on digital usage over time.
    """
    if input("Would you like to see your screen time history? (yes/no): ").strip().lower() == "yes":
        try:
            with open("history_log.txt", "r") as file:
                lines = file.readlines()

                if not lines:
                    print("\n No history found. Start tracking your screen time today!")
                    return  # Exit function if there is no history

                print("\n Your Recent Screen Time Records:")
                screen_times = []  # Stores extracted screen time values

                # Extract screen time data
                for line in lines:
                    try:
                        screen_time = float(line.strip().split("Screen Time: ")[-1].split(" hours")[0])
                        screen_times.append(screen_time)
                    except (IndexError, ValueError):
                        continue  # Skip any improperly formatted lines

                #  If there is enough data, perform analysis
                if len(screen_times) >= 7:
                    last_week = screen_times[-7:]  # Last 7 records
                    avg_weekly = sum(last_week) / len(last_week)
                    print("\n **Weekly Screen Time Trend:**")
                    print(f"Your average screen time in the last week: **{avg_weekly:.1f} hours/day**")

                    # Provide analysis on weekly trends
                    if avg_weekly > 8:
                        print(" Your weekly screen time is very high. Try reducing unnecessary usage.")
                    elif avg_weekly > 5:
                        print(" Your weekly screen time is moderate. Keep making mindful choices!")
                    else:
                        print(" Excellent! You’ve maintained a balanced screen time this week.")

                if len(screen_times) >= 30:
                    last_month = screen_times[-30:]  # Last 30 records
                    avg_monthly = sum(last_month) / len(last_month)
                    print("\n **Monthly Screen Time Trend:**")
                    print(f"Your average screen time in the last month: **{avg_monthly:.1f} hours/day**")

                    # Provide analysis on monthly trends
                    if avg_monthly > 8:
                        print(" Long-term high screen time detected. Consider setting screen-free goals.")
                    elif avg_monthly > 5:
                        print(" Your monthly screen time is fairly balanced, but minor reductions can help.")
                    else:
                        print(" Well done! You've maintained a healthy digital routine over the past month!")

                # Show full history (last 10 entries for readability)
                print("\n **Your Last 10 Screen Time Logs:**")
                for line in lines[-10:]:  # Display last 10 records only
                    print(line.strip())

        except FileNotFoundError:
            print("\n⚠ No history file found. Your screen time tracking starts now!")

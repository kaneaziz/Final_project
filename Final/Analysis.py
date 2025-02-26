import random

def compare_to_average(total_time):
    """
    Compares the user's screen time with global averages.
    """
    if input(
            "Would you like to see how your screen time compares to the average user? (yes/no): ").strip().lower() == "yes":
        average_time = 6.97
        print("\nSocial Media Comparison to the Average User:")
        diff = total_time - average_time
        if diff > 0:
            print(f"You spend {diff:.1f} hours more than the average user!")
        elif diff < 0:
            print(f"You spend {abs(diff):.1f} hours less than the average user!")
        else:
            print("Your screen time is exactly at the global average.")
        print(f"\nYour Total Screen Time: {total_time:.1f} hours/day")
        print(f"Global Average Screen Time: {average_time:.1f} hours/day")

def analyze_health_impact(total_time):
    """
    Analyzes the impact of screen time on health and provides warnings with suggested solutions.
    """
    if input("Would you like to see how screen time impacts your health? (yes/no): ").strip().lower() == "yes":
        print("\nTime Impact on Health:")
        if total_time <= 2:
            print("Your screen time is well-balanced. Keep maintaining a healthy digital habit!")
        elif total_time <= 5:
            print("Your screen time is moderate, but reducing it slightly can help improve focus and sleep.")
        elif total_time <= 8:
            print("Your screen time is high! This can contribute to eye strain and reduced physical activity.")
        elif total_time <= 12:
            print("Excessive screen time can lead to serious health issues, including anxiety and poor posture.")
        else:
            print("Severe screen overuse detected! Consider an urgent digital detox to regain balance in life.")

        health_tips = [
            "Try the 20-20-20 rule: Every 20 minutes, take a 20-second break and look 20 feet away to reduce eye strain.",
            "Consider taking short walks every hour to improve circulation and reduce prolonged screen exposure.",
            "Use blue light filters on your screens to reduce eye strain and improve sleep quality.",
            "Reduce screen brightness and adjust contrast settings to minimize strain on your eyes.",
            "Engage in a non-screen activity like stretching or deep breathing exercises for a few minutes each hour."
        ]
        print(random.choice(health_tips))

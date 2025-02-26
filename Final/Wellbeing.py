def digital_wellbeing_score(total_time):
    """
    Calculates a digital well-being score based on screen time usage and explains the rating.
    """
    if input("Would you like to calculate your Digital Well-being Score? (yes/no): ").strip().lower() == "yes":
        score = max(100 - (total_time * 5), 0)
        print(f"Your Digital Well-being Score: {score}/100")
        if score >= 80:
            print("Great! Your screen time is well-managed and balanced.")
        elif score >= 50:
            print("Moderate screen usage. Consider minor adjustments for improved well-being.")
        else:
            print("High screen time detected! Take action to minimize its negative effects.")

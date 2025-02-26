import random

def user_interests_and_plan(reduce_hours):
    """
    Allows the user to select multiple interests and generates a personalized plan based on their reduced screen time.
    """
    print("\nWhat type of activities do you enjoy?")
    interests = {
        1: "Fitness & Sports",
        2: "Learning & Reading",
        3: "Creativity & Hobbies",
        4: "Relaxation & Mental Well-being"
    }

    for key, value in interests.items():
        print(f"{key}. {value}")

    while True:
        try:
            user_selection = input("Choose one or multiple numbers (1-4) separated by spaces or commas: ").strip()
            selected_numbers = list(map(int, user_selection.replace(",", " ").split()))
            if not all(num in interests for num in selected_numbers):
                print("Invalid choice. Please select from 1-4.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter numbers only.")

    print("\nBased on your interests and your goal to reduce screen time, here's a customized plan for you:")

    suggestions = {
        1: [
            "Go for a 30-minute morning run to start your day.",
            "Join a local sports club or attend a fitness class.",
            "Try bodyweight exercises or yoga at home to stay active.",
            "Set a step goal and take walks outdoors to refresh your mind."
        ],
        2: [
            "Spend an hour reading a book or learning something new online.",
            "Take an online course on a subject that interests you.",
            "Write in a journal or start creative writing to reflect on your thoughts.",
            "Practice a new language by dedicating time daily to language apps."
        ],
        3: [
            "Dedicate time to painting, playing an instrument, or other hobbies.",
            "Try a DIY project or start a creative challenge (writing, drawing, etc.).",
            "Explore new recipes and cook something different.",
            "Engage in photography or video editing to enhance your skills."
        ],
        4: [
            "Practice mindfulness or meditation for mental well-being.",
            "Take a warm bath, light candles, and play calming music for relaxation.",
            "Spend time in nature and disconnect from digital distractions.",
            "Have meaningful conversations with family or friends without distractions."
        ]
    }

    for num in selected_numbers:
        chosen_category = interests[num]
        selected_suggestions = random.sample(suggestions[num], min(2, len(suggestions[num])))
        print(f"\nFor {chosen_category}, you could:")
        for suggestion in selected_suggestions:
            print(f"- {suggestion}")

    print("\nUse your reduced screen time to implement these activities and build healthier habits!")

def screen_time_projection(reduce_hours):
    """
    Displays what users could have achieved with their reduced screen time.
    """
    if input("Would you like to see what you could have achieved with this time spent on your phone? (yes/no): ").strip().lower() == "yes":
        print("\nScreen Time Projection: What You Could Have Done Instead")

        # Weekly achievements
        print(f"\nIn a week ({reduce_hours * 7:.1f} hours saved):")
        week_options = [
            "You could learn the basics of video editing or a simple coding language.",
            "You could complete a short online course on personal finance or productivity.",
            "You could improve flexibility by doing daily yoga or stretching exercises."
        ]
        for suggestion in week_options:
            print(f"- {suggestion}")

        # Monthly achievements
        print(f"\nIn a month ({reduce_hours * 30:.1f} hours saved):")
        month_options = [
            "You could become proficient in a professional tool like Excel or PowerPoint.",
            "You could develop a new hobby such as painting, photography, or creative writing.",
            "You could train for a 5K run or build strength with a home workout program."
        ]
        for suggestion in month_options:
            print(f"- {suggestion}")

        # Yearly achievements
        print(f"\nIn a year ({reduce_hours * 365 / 24:.1f} days saved):")
        year_options = [
            "You could reach conversational fluency in a new language.",
            "You could become intermediate in playing an instrument like piano or guitar.",
            "You could write and self-publish a book or start a blog on a topic you're passionate about."
        ]
        for suggestion in year_options:
            print(f"- {suggestion}")

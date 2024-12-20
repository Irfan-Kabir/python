import random
import time
import msvcrt
import json

USER_DATA_FILE = "users.txt"

vocabulary = {
  "Abate": ["Lessen", "Increase", "Abolish", "Rebel"],
"Cacophony": ["Harsh noise", "Harmony", "Melody", "Silence"],
"Ebullient": ["Enthusiastic", "Sad", "Angry", "Lazy"],
"Ephemeral": ["Short-lived", "Permanent", "Endless", "Lengthy"],
"Garrulous": ["Talkative", "Quiet", "Reserved", "Shy"],
"Iconoclast": ["Rebel", "Follower", "Supporter", "Traditionalist"],
"Loquacious": ["Talkative", "Silent", "Dull", "Reserved"],
"Obfuscate": ["Confuse", "Clarify", "Simplify", "Explain"],
"Perfunctory": ["Routine", "Enthusiastic", "Dedicated", "Exceptional"],
"Sagacious": ["Wise", "Foolish", "Naive", "Ignorant"],
"Alacrity": ["Eagerness", "Reluctance", "Delay", "Disinterest"],
"Belligerent": ["Hostile", "Peaceful", "Calm", "Submissive"],
"Candid": ["Honest", "Deceptive", "Hidden", "Indifferent"],
"Debilitate": ["Weaken", "Strengthen", "Fortify", "Enhance"],
"Enervate": ["Drain", "Revitalize", "Fortify", "Strengthen"],
"Frivolous": ["Trivial", "Serious", "Important", "Substantial"],
"Germane": ["Relevant", "Irrelevant", "Inappropriate", "Unrelated"],
"Hapless": ["Unfortunate", "Fortunate", "Happy", "Joyful"],
"Irascible": ["Irritable", "Calm", "Patient", "Content"],
"Jocular": ["Funny", "Serious", "Grumpy", "Melancholy"],
"Keen": ["Eager", "Indifferent", "Disinterested", "Unconcerned"],
"Lethargic": ["Lazy", "Energetic", "Active", "Dynamic"],
"Munificent": ["Generous", "Stingy", "Greedy", "Selfish"],
"Nefarious": ["Wicked", "Good", "Benevolent", "Kind"],
"Obsequious": ["Subservient", "Independent", "Rebellious", "Assertive"],
"Pernicious": ["Harmful", "Beneficial", "Safe", "Helpful"],
"Querulous": ["Complaining", "Content", "Grateful", "Satisfied"],
"Redundant": ["Unnecessary", "Essential", "Important", "Required"],
"Sycophant": ["Flatterer", "Leader", "Indifferent", "Independent"],
"Tenuous": ["Weak", "Strong", "Stable", "Steady"],
"Ubiquitous": ["Omnipresent", "Rare", "Uncommon", "Scarce"],
"Venerable": ["Respected", "Disrespected", "Ignored", "Insulted"],
"Wary": ["Cautious", "Careless", "Reckless", "Indifferent"],
"Xenophobic": ["Fearful of strangers", "Open-minded", "Welcoming", "Friendly"],
"Yen": ["Desire", "Disinterest", "Indifference", "Apathy"],
"Zealous": ["Enthusiastic", "Indifferent", "Complacent", "Lazy"],
"Acerbic": ["Sharp", "Mild", "Soft", "Kind"],
"Benevolent": ["Kind", "Malicious", "Hostile", "Spiteful"],
"Cognizant": ["Aware", "Oblivious", "Ignorant", "Unaware"],
"Disparate": ["Different", "Similar", "Same", "Identical"],
"Ephemeral": ["Short-lived", "Everlasting", "Perpetual", "Enduring"],
"Fastidious": ["Particular", "Indifferent", "Careless", "Unconcerned"],
"Garrulous": ["Talkative", "Silent", "Reserved", "Quiet"],
"Harangue": ["Lecture", "Compliment", "Silence", "Agreement"],
"Indolent": ["Laziness", "Active", "Productive", "Diligent"],
"Juxtapose": ["Compare", "Separate", "Distinguish", "Separate"],
"Knavish": ["Dishonest", "Honest", "Truthful", "Faithful"],
"Luminous": ["Bright", "Dark", "Dim", "Gloomy"],
"Malevolent": ["Evil", "Benevolent", "Kind", "Helpful"],
"Nefarious": ["Wicked", "Good", "Honest", "Kind"],
"Obfuscate": ["Confuse", "Clarify", "Illuminate", "Explain"],
"Palliate": ["Alleviate", "Exacerbate", "Worsen", "Strengthen"],
"Querulous": ["Complaining", "Satisfied", "Content", "Happy"],
"Recalcitrant": ["Uncooperative", "Cooperative", "Obedient", "Submissive"],
"Sardonic": ["Sarcastic", "Sincere", "Serious", "Respectful"],
"Tantamount": ["Equivalent", "Opposite", "Contradictory", "Unrelated"],
"Ubiquitous": ["Everywhere", "Rare", "Uncommon", "Infrequent"],
"Vex": ["Annoy", "Delight", "Please", "Comfort"],
"Wistful": ["Longing", "Content", "Indifferent", "Happy"],
"Xenial": ["Friendly", "Unwelcoming", "Hostile", "Antagonistic"],
"Yearn": ["Desire", "Ignore", "Disregard", "Neglect"],
"Zealous": ["Enthusiastic", "Unconcerned", "Indifferent", "Complacent"],
"Abrupt": ["Sudden", "Gradual", "Steady", "Continuous"],
"Benevolent": ["Generous", "Malevolent", "Selfish", "Greedy"],
"Cacophony": ["Loud noise", "Silence", "Melody", "Harmony"],
"Dilapidated": ["Ruined", "New", "Fresh", "Renovated"],
"Ebullient": ["Excited", "Calm", "Saddened", "Bored"],
"Facetious": ["Joking", "Serious", "Melancholy", "Sad"],
"Garrulous": ["Talkative", "Quiet", "Reserved", "Shy"],
"Harbinger": ["Forecaster", "Obscure", "Random", "Surprise"],
"Impetuous": ["Impulsive", "Careful", "Thoughtful", "Cautious"],
"Juxtapose": ["Compare", "Separate", "Distinguish", "Separate"],
"Knavish": ["Dishonest", "Honest", "Truthful", "Faithful"],
"Loquacious": ["Talkative", "Silent", "Dull", "Reserved"],
"Munificent": ["Generous", "Stingy", "Greedy", "Selfish"],
"Nefarious": ["Wicked", "Good", "Benevolent", "Kind"],
"Obfuscate": ["Confuse", "Clarify", "Simplify", "Explain"]
}


def load_user_data():
    
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def register_user(users):
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try a different one.")
        return users, None
    password = input("Enter a password: ")
    users[username] = {"password": password, "history": []}
    save_user_data(users)
    print("Registration successful!")
    return users, username


def login_user(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    print("Invalid credentials. Try again.")
    return None


def delete_account(users, username):
    confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
    if confirm == "yes":
        users.pop(username, None)
        save_user_data(users)
        print("Account deleted successfully!")
        return True
    print("Account deletion canceled.")
    return False


def admin_panel(users):
    while True:
        print("\nAdmin Panel:")
        print("1. View all users")
        print("2. Remove a user")
        print("3. Exit admin panel")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nRegistered Users:")
            for user in users.keys():
                print(user)
        elif choice == "2":
            user_to_remove = input("Enter the username to remove: ")
            if user_to_remove in users:
                users.pop(user_to_remove)
                save_user_data(users)
                print(f"User '{user_to_remove}' removed successfully.")
            else:
                print("User not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


def get_user_input(timeout):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if msvcrt.kbhit():
            char = msvcrt.getche().decode("utf-8")
            if char == "\r":
                print()
                return None
            elif char.isdigit():
                return char
    return None


def start_quiz(difficulty, username=None, users=None):
    total_questions = 10
    points = 0
    time_limit = {"easy": 20, "medium": 15, "hard": 10}[difficulty]

    questions = random.sample(list(vocabulary.keys()), total_questions)
    for i, word in enumerate(questions):
        options = vocabulary[word]
        correct_answer = options[0]
        shuffled_options = random.sample(options, len(options))

        print(f"\nQuestion {i + 1}: What is the meaning of '{word}'?")
        for idx, option in enumerate(shuffled_options):
            print(f"{idx + 1}. {option}")

        print(f"You have {time_limit} seconds to answer...")
        start_time = time.time()
        user_input = None

        while time.time() - start_time < time_limit:
            user_input = get_user_input(time_limit - (time.time() - start_time))
            if user_input is None:
                continue
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                chosen_option = shuffled_options[int(user_input) - 1]
                if chosen_option == correct_answer:
                    print("\nCorrect! Well done.")
                    points += 1
                else:
                    print(f"\nWrong! The correct answer was: {correct_answer}")
                break
            else:
                print("\nInvalid choice! Try again within the time.")
        else:
            print(f"\nTime's up! The correct answer was: {correct_answer}")

    print(f"\nQuiz over! You scored {points}/{total_questions}.")
    if username and users is not None:
        users[username]["history"].append({"score": points, "questions": total_questions})
        save_user_data(users)


def main():
    users = load_user_data()
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Play as Guest")
        print("4. Admin Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            users, _ = register_user(users)
        elif choice == "2":
            username = login_user(users)
            if username:
                while True:
                    print("\nUser Menu:")
                    print("1. Play Quiz")
                    print("2. View History")
                    print("3. Delete Account")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
                        if difficulty in ["easy", "medium", "hard"]:
                            start_quiz(difficulty, username, users)
                        else:
                            print("Invalid difficulty choice.")
                    elif user_choice == "2":
                        print(f"\nHistory for {username}:")
                        for entry in users[username]["history"]:
                            print(f"Score: {entry['score']} / {entry['questions']}")
                    elif user_choice == "3":
                        if delete_account(users, username):
                            break
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
            if difficulty in ["easy", "medium", "hard"]:
                start_quiz(difficulty)
            else:
                print("Invalid difficulty choice.")
        elif choice == "4":
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123": 
                admin_panel(users)
            else:
                print("Invalid admin password.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

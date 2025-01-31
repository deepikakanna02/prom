def get_user_data(user_id):
    """Collect gender and answers from a user."""
    print(f"User {user_id}:")
    gender = input("Enter your gender (male/female): ").strip().lower()
    while gender not in ['male', 'female']:
        gender = input("Invalid input. Please enter 'male' or 'female': ").strip().lower()

    questions = [
        "How do you prefer to spend your weekends?",
        "When faced with a challenge, how do you typically respond?",
        "Which of these best describes your communication style?",
        "What is your approach to decision-making?",
        "What motivates you the most in a partnership or team?"
    ]

    options_list = [
        ["a) Exploring new places or trying new activities.", "b) Relaxing at home with a book or movie.",
         "c) Socializing with friends or attending events.", "d) Catching up on personal projects or hobbies."],
        ["a) Analyze the situation and create a plan.", "b) Seek advice or collaborate with others.",
         "c) Take action immediately, trusting instincts.", "d) Reflect and wait for the right moment."],
        ["a) Direct and straightforward.", "b) Empathetic and understanding.",
         "c) Logical and fact-based.", "d) Creative and expressive."],
        ["a) Follow a logical and step-by-step process.", "b) Rely on intuition and feelings.",
         "c) Seek input from others before deciding.", "d) Make quick decisions and adapt as needed."],
        ["a) Shared goals and mutual understanding.", "b) Clear communication and honesty.",
         "c) Fun and spontaneity in the relationship.", "d) Growth and learning opportunities."]
    ]

    answers = []
    for i, question in enumerate(questions):
        print(f"Q{i+1}: {question}")
        for option in options_list[i]:
            print(option)
        choice = input("Your choice (a-d): ").strip().lower()
        while choice not in ['a', 'b', 'c', 'd']:
            choice = input("Invalid choice. Please enter a valid option (a-d): ").strip().lower()
        answers.append(choice)

    return gender, answers


def find_best_pairs(user_data):
    """Find the best matching pairs between males and females."""
    males = [(i, data) for i, data in enumerate(user_data) if data[0] == 'male']
    females = [(i, data) for i, data in enumerate(user_data) if data[0] == 'female']

    paired_users = set()
    results = []

    for male_id, male_data in males:
        if male_id in paired_users:
            continue

        best_match = None
        max_matches = -1
        for female_id, female_data in females:
            if female_id in paired_users:
                continue

            matches = sum(1 for a, b in zip(male_data[1], female_data[1]) if a == b)
            if matches > max_matches:
                max_matches = matches
                best_match = female_id

        if best_match is not None:
            paired_users.update([male_id, best_match])
            results.append((male_id + 1, best_match + 1, max_matches))

    # Find unpaired users
    unpaired_males = [male_id + 1 for male_id, _ in males if male_id not in paired_users]
    unpaired_females = [female_id + 1 for female_id, _ in females if female_id not in paired_users]

    return results, unpaired_males, unpaired_females


def main():
    print("Welcome to the Gender-based MCQ Matching Game!")
    user_data = []
    user_id = 1

    while True:
        add_user = input(f"Do you want to add User {user_id}? (yes/no): ").strip().lower()
        if add_user == 'no':
            break
        if add_user == 'yes':
            user_data.append(get_user_data(user_id))
            user_id += 1
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nFinding the best pairs...")
    best_pairs, unpaired_males, unpaired_females = find_best_pairs(user_data)

    print("\nResults:")
    for male, female, matches in best_pairs:
        print(f"User {male} (male) matched with User {female} (female) on {matches}/5 answers.")

    if unpaired_males or unpaired_females:
        print("\nUnpaired Users:")
        for male in unpaired_males:
            print(f"User {male} (male) could not be paired.")
        for female in unpaired_females:
            print(f"User {female} (female) could not be paired.")


if __name__ == "__main__":
    main()
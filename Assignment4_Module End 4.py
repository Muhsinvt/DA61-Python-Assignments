# Module End Assignment 4: Survey Feedback Analyzer

# =========================================================
# Step 1: Preloaded Feedbacks (Given Data)
# =========================================================
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# =========================================================
# Step 2: Add More Feedbacks
# =========================================================
print("--- Step 2: Add More Feedbacks ---")
count = int(input("How many more feedbacks do you want to add? "))

for i in range(count):
    print("\nFeedback", i + 1)
    name = input("Enter Name: ")
    feedback = input("Enter Feedback: ")

    # Keep asking until a valid rating (1 to 5) is entered
    rating = int(input("Enter Rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Invalid rating! Please enter a number between 1 and 5.")
        rating = int(input("Enter Rating (1-5): "))

    # S_No continues from the last number (11, 12, ...)
    new_sno = feedback_data['S_No'][-1] + 1

    feedback_data['S_No'].append(new_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nTotal feedbacks now:", len(feedback_data['S_No']))

# =========================================================
# Step 3: Text Cleaning
# =========================================================
def clean_text(text):
    # Remove punctuation
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
    # split() removes leading/trailing spaces and multiple spaces;
    # ' '.join() puts the words back with a single space
    text = ' '.join(text.split())
    # Convert to lowercase
    return text.lower()


cleaned = []
for fb in feedback_data['Feedback']:
    cleaned.append(clean_text(fb))
feedback_data['Feedback'] = cleaned

print("\n--- Step 3: Cleaned Feedbacks ---")
for sno, fb in zip(feedback_data['S_No'], feedback_data['Feedback']):
    print(sno, ":", fb)

# =========================================================
# Step 4: Word Count Insights
# =========================================================
def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        if word in fb.split():   # whole-word match, case-insensitive
            count = count + 1
    return count


print("\n--- Step 4: Word Count Insights ---")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

# =========================================================
# Step 5: Final Summary & Insights
# =========================================================
print("\n--- Step 5: Final Summary & Insights ---")

# a. Final cleaned feedback_data
print("\nFinal cleaned feedback_data:")
for key in feedback_data:
    print(key, ":", feedback_data[key])

# b. Average rating
average = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage Rating:", round(average, 2))

# c. Longest feedback (by word count)
longest_index = 0
for i in range(len(feedback_data['Feedback'])):
    if len(feedback_data['Feedback'][i].split()) > len(feedback_data['Feedback'][longest_index].split()):
        longest_index = i

print("\nLongest Feedback:")
print("Name:", feedback_data['Name'][longest_index])
print("Feedback:", feedback_data['Feedback'][longest_index])
print("Word Count:", len(feedback_data['Feedback'][longest_index].split()))

# d. Unique words across all feedbacks
unique_words = set()
for fb in feedback_data['Feedback']:
    for w in fb.split():
        unique_words.add(w)

unique_words = sorted(unique_words)
print("\nUnique words (" + str(len(unique_words)) + "):")
print(unique_words)

# e. (Optional) Sort feedbacks by rating, highest to lowest
print("\nFeedbacks sorted by Rating (highest to lowest):")
combined = zip(feedback_data['S_No'], feedback_data['Name'],
               feedback_data['Feedback'], feedback_data['Rating'])
sorted_feedbacks = sorted(combined, key=lambda x: x[3], reverse=True)

for sno, name, fb, rating in sorted_feedbacks:
    print(sno, "|", name, "|", rating, "|", fb)
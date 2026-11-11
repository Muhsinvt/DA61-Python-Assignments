# Python Assignment 2: Data Structures - List, Dictionary, Set & Conditional Statements

# =========================================================
# LIST
# =========================================================

# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Arjun", "Meera", "Rahul", "Divya", "Kiran"]
print("age_list:", age_list)
print("name_list:", name_list)

# 2. List Operations / Modifications
print("\n--- List Operations ---")

# a. Append "Yazhini" to name_list
name_list.append("Yazhini")
print("a.", name_list)

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print("b.", age_list)

# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")
print("c.", name_list)

# d. Pop the last element from age_list
popped = age_list.pop()
print("d. Popped:", popped, "| age_list now:", age_list)

# e. Extend age_list with [29, 30, 26]
age_list.extend([29, 30, 26])
print("e.", age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("f.", age_list)

# g. Max, Min and Sum of ages
print("g. Max age:", max(age_list))
print("   Min age:", min(age_list))
print("   Sum of ages:", sum(age_list))

# 3. Accessing List Elements
print("\n--- Accessing List Elements ---")
print("a. First element:", name_list[0])
print("b. Last element:", name_list[-1])
print("c. Index 2 to 4:", name_list[2:5])
print("d. Reverse order:", name_list[::-1])

# =========================================================
# DICTIONARY
# =========================================================
print("\n--- Dictionary ---")

# a. Create the dictionary
student_marks = {"Arjun": 78, "Meera": 92, "Rahul": 65, "Divya": 88, "Kiran": 71}
print("a.", student_marks)

# b. Access a specific student's mark
print("b. Meera's mark:", student_marks["Meera"])

# c. Add Janani with 80
student_marks["Janani"] = 80
print("c.", student_marks)

# d. Update an older student's mark to 82
student_marks["Rahul"] = 82
print("d.", student_marks)

# e. keys(), values(), items()
print("e. Keys:", student_marks.keys())
print("   Values:", student_marks.values())
print("   Items:", student_marks.items())

# =========================================================
# SETS
# =========================================================
print("\n--- Sets ---")

# a. Create my_set
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print("a.", my_set)
# Explanation: The list has 8 values, but the set shows only 5 ('a','e','i','o','u').
# A set stores only UNIQUE values, so duplicate 'a' and 'i' are removed automatically.
# Sets are also UNORDERED, so the printed order may differ from the input order.

# b. Attempt to change my_set[4]
try:
    my_set[4] = 's'
except TypeError as e:
    print("b. Error:", e)
# Explanation: This gives TypeError: 'set' object does not support item assignment.
# Sets are unordered, so elements have NO index positions. You cannot access or
# change an element using my_set[4]. Use add() / remove() instead, e.g. my_set.add('s').

# c. Create set1 and set2
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print("c. set1:", set1)
print("   set2:", set2)

# d. Union and Intersection
print("d. Union:", set1 | set2)          # or set1.union(set2)
print("   Intersection:", set1 & set2)   # or set1.intersection(set2)

# =========================================================
# OPERATORS & CONDITIONAL STATEMENTS - Performance Category
# =========================================================
print("\n--- Performance Category Program ---")

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a value between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
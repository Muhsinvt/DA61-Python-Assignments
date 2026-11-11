# Python Assignment 1: Data Structures - Strings & Tuples

# ---------------------------------------------------------
# 1. String Concatenation
# ---------------------------------------------------------
string1 = "Hello "
string2 = input("Enter your Name: ")

greeting = string1 + string2
print(greeting)                      # Hello Zara

string3 = ", welcome to Python programming"
full_string = greeting + string3
print(full_string)                   # Hello Zara, welcome to Python programming

# ---------------------------------------------------------
# 2. String Slicing and Indexing (uses full_string from above)
# ---------------------------------------------------------
print("\n--- String Slicing and Indexing ---")
print("a. First character:", full_string[0])
print("b. Last character:", full_string[-1])
print("c. First 5 characters:", full_string[:5])
print("d. Last 11 characters:", full_string[-11:])
print("e. Reversed string:", full_string[::-1])

# "Python programming" is always the last 18 characters,
# so "Python" sits between index -18 and -12, whatever name is entered.
print("f. Word 'Python':", full_string[-18:-12])

# ---------------------------------------------------------
# 3. String Methods
# ---------------------------------------------------------
print("\n--- String Methods ---")
strM = "Python beginner tutorial"

upper_str = strM.upper()
print("a. Uppercase:", upper_str)

lower_str = strM.lower()
print("b. Lowercase:", lower_str)

original = upper_str.capitalize()
print("c. Capitalize (back to original):", original)

print("d. Count of 't':", strM.count("t"))

print("e. Replace:", strM.replace("Python", "Machine Learning"))

# ---------------------------------------------------------
# 4. Tuples (Creation, Modification and Access)
# ---------------------------------------------------------
print("\n--- Tuples ---")
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t_combine = t1 + t2
print("a. Combined tuple:", t_combine)

print("b. Repeated 3 times:", t_combine * 3)

print("c. 3rd element:", t_combine[2])

print("d. First three elements:", t_combine[:3])

print("e. Last three elements:", t_combine[-3:])
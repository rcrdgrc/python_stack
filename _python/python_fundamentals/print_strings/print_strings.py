first_name = "Zen"
last_name = "Coder"
age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")
print(first_name)
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

# f-string
# does not work in vs code

# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# Built-In string methods

x = "hello world"
print(x.title())
# output:
"Hello World"

# string.upper(): returns a copy of the string with all the characters in uppercase.
print(x.upper())

# string.lower(): returns a copy of the string with all the characters in lowercase.
print(x.lower())

# string.count(substring): returns number of occurrences of substring in string.
print(x.count("e"))

# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
print(x.split(" "))

# string.find(substring): returns the index of the start of the first occurrence of substring within string.
print(x.find("h"))

# string.isalnum(): returns boolean depending on whether the string's length is > 0 and 
# all characters are alphanumeric (letters and numbers only). Strings that include spaces and 
# punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), 
# .islower(), .isupper(), and so on. All return booleans.
print(x.isalnum())

# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# print(x.join(list))

# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
print(x.endswith("d"))
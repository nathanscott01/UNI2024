import random
import string

# Define the length of the texts and the common substring
text_length = 5000
common_substring = "commonsubstring20"
common_length = len(common_substring)


# Generate a random string of uppercase letters for the first file
def generate_random_uppercase_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


# Generate a random string of lowercase letters and digits, excluding certain characters for the second file
def generate_random_lowercase_digits_string(length, exclude):
    allowed_chars = ''.join(set(string.ascii_lowercase + string.digits) - set(exclude))
    return ''.join(random.choices(allowed_chars, k=length))


# Generate the two strings
s1_prefix = generate_random_uppercase_string(text_length - common_length)
s2_prefix = generate_random_lowercase_digits_string(text_length - common_length, common_substring)

# Insert the common substring at a random position
s1_insert_pos = random.randint(0, text_length - common_length)
s2_insert_pos = random.randint(0, text_length - common_length)

s1 = s1_prefix[:s1_insert_pos] + common_substring + s1_prefix[s1_insert_pos:]
s2 = s2_prefix[:s2_insert_pos] + common_substring + s2_prefix[s2_insert_pos:]

# Output the generated strings
print("String 1: \n", s1)
print("String 2: \n", s2)

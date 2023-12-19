def count_letters_at_odd_indices(input_string):
    input_string = "".join(input_string.split()).lower()
    letter_counts = {}
    for i in range(1, len(input_string), 2):
        letter = input_string[i]
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

# Example usage:
input_str = input("user enter the str:")
result = count_letters_at_odd_indices(input_str)

if result:
    print("Letter counts at odd indices (case-insensitive and excluding spaces):")
    for letter, count in result.items():
        print(f"{letter}: Count = {count}")
else:
    print("No letters found at odd indices.")

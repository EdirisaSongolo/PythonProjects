# Find the number of times each character appears in the string
designated_string = "photosynthesis"
string_list = list(designated_string)
unique_characters = sorted(set(string_list))

print(string_list)
print(unique_characters)

for string_character in unique_characters:
    character_instance = 0
    for character in string_list:
        if (string_character is character):
            character_instance += 1
    print(f'{string_character} appears {character_instance} time(s) in the string')

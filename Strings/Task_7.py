user_input = input("Enter a word to have the vowels counted: ")
user_input = user_input.lower()
vowel_a, vowel_e, vowel_i,vowel_o, vowel_u = 'a', 'e', 'i', 'o', 'u'
num_vowel = user_input.count(vowel_a) + user_input.count(vowel_e) + user_input.count(vowel_i) + user_input.count(vowel_o) + user_input.count(vowel_u)
print(f'')
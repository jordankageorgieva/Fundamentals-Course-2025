text_with_vowels = input()
text_no_vowels = [let for let in text_with_vowels if let.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(text_no_vowels))
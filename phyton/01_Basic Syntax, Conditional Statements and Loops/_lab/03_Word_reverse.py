word = input()

reverse_word = ""

def reverse(input):
    if len(input) <= 1:
        return  input
    return reverse(input[1:]) + input[0]

reverse_word = reverse(word)
print(reverse_word)
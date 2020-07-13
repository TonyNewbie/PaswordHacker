first_word = input()
second_word = input()
result = ''
for letter_first, letter_second in zip(first_word, second_word):
    result += letter_first + letter_second
print(result)

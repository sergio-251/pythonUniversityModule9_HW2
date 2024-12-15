# Списковые, словарные сборки

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(el) for el in first_strings if len(el) > 5]
second_result = [(word_1, word_2) for word_1 in first_strings for word_2 in second_strings if len(word_1) == len(word_2)]
third_result = {i: len(i) for i in first_strings + second_strings if not len(i) % 2}

print(first_result)
print(second_result)
print(third_result)
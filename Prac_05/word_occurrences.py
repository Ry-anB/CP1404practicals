"""
CP1404 - Practical 05 - Word Occurrences
Estimate: 15 minutes
Actual:   13 minutes
"""

words_to_occurrences = {}
longest_word_length = 0
user_entered_string = input("Enter a string: ")
for word in user_entered_string.split():
    if word in words_to_occurrences:
        words_to_occurrences[word] += 1
    else:
        words_to_occurrences[word] = 1
        if len(word) > longest_word_length:
            longest_word_length = len(word)
for key in sorted(words_to_occurrences):
    print(f"{key:{longest_word_length}} : {words_to_occurrences[key]}")

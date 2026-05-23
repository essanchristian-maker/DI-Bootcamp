# Challenge 1 : Sorting

words = input("Enter words (comma-separated): ").split(",")

sorted_words = ",".join(sorted([word.strip() for word in words]))

print(sorted_words)




# Challenge 2 : Le mot le plus long

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


# Tests
print(longest_word("Margaret's toy is a pretty doll."))
# → Margaret's

print(longest_word("A thing of beauty is a joy forever."))
# → forever.

print(longest_word("Forgetfulness is by all means powerless!"))
# → Forgetfulness
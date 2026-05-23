# Challenge 1 : Sorting

words = input("Enter words (comma-separated): ").split(",")

sorted_words = ",".join(sorted([word.strip() for word in words]))

print(sorted_words)
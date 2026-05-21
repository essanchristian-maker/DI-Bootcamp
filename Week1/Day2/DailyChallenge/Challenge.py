#Defi 1

# 1. User Input
word = input("Enter a word: ")

# 2. Creating the dictionary
index_dict = {}

for index, char in enumerate(word):

    # If the character is already a key, append the index to its list
    if char in index_dict:
        index_dict[char].append(index)

    # If not, create a new key with a list containing the index
    else:
        index_dict[char] = [index]

# 3. Display the result
print(index_dict)





#Defi 2

# 1. Store Data
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# 2. Data Cleaning
wallet = int(wallet.replace("$", "").replace(",", ""))

# 3. Determining Affordable Items
basket = []

for item, price in items_purchase.items():

    # Clean the price the same way
    price = int(price.replace("$", "").replace(",", ""))

    # If we can afford it, add to basket and update wallet
    if price <= wallet:
        basket.append(item)
        wallet -= price

# 4. Print the result
if basket == []:
    print("Nothing")
else:
    print(sorted(basket))
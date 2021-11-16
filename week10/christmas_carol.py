# A story of ghosts of Python

# Opening the eBook in read-only mode
my_file = open("christmas_carol.txt", "r")

# Dictionary tracking occurrences of words
my_dict = {}

# Go through every line of text in the file
for line in my_file:
    #print(line)
    list_of_words = line.split(" ")
    #print(list_of_words)
    for individual_word in list_of_words:
        # Strip every word off punctuation/spaces
        individual_word = individual_word.strip("\n .,;:-\"")
        individual_word = individual_word.lower()
        #print(individual_word, end=" ")

        # If the current word is already a key in the dictionary
        if  individual_word in my_dict:
            # Increase the count
            my_dict[individual_word] += 1
        else:
            # Otherwise if it's not yet in the dictionary
            # Initialise it to 1
            my_dict[individual_word] = 1

# print(my_dict)
my_file.close()

# Extract the values from the dictionary 
# And sort them by most common first

# 1 Convert the dictionary into a list of tuples
# Every tuple will be (key, value)
item_list = [(k, v) for k, v in my_dict.items()]

# 2 Sort the list by v
item_list.sort(key=lambda x:x[1], reverse=True)

# Print the 100 most frequent words
result_file = open("results.csv", "w")

for counter in range(100):
    current_pair = item_list[counter]
    result_file.write(current_pair[0] + "," + str(current_pair[1]) + "\n")

result_file.close()
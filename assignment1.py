import string

# Open the file for reading
with open("sample.txt", "r") as f:
    # Read the file contents
    text = f.read()

# Remove punctuation and convert to lowercase
text = text.translate(str.maketrans("", "", string.punctuation)).lower()

# Split the text into words
words = text.split()

# Count the frequency of each word
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the words by frequency (descending order)
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Open a new file for writing the report
with open("report.txt", "w") as f:
    # Write the header
    f.write("Word Frequency Report\n\n")
    f.write("Word\t\tFrequency\n")

    # Write each word and its frequency
    for word, freq in sorted_words:
        f.write(f"{word}\t\t{freq}\n")

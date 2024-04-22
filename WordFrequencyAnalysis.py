import re
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize



# Read the contents of the file
file = open(r'paragraphs.txt', 'r')
text = file.read()
# Close the file after we're done reading
file.close()

# Tokenize the text in list
words = word_tokenize(text)

# Remove punctuation and split the text into words
words = re.findall(r'\b\w+\b', text.lower())

# Get list of stopwords
stopwords = set(stopwords.words('english'))

# Convert the word tokens into lowercase and remove stopwords
filtered_text = [w.lower() for w in words if w.lower() not in stopwords]


# Use the method Counter to count the frequency of each word
counts = Counter(filtered_text).most_common()

# Print the word frequencies
for word, freq in counts:
    print(f"{word}: {freq}")
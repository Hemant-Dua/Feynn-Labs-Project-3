import nltk
from nltk.corpus import stopwords

# Download required resources (comment out if already downloaded)
nltk.download("punkt")
nltk.download("stopwords")

# Define stopwords (common words to exclude) and exclamation threshold
stop_words = stopwords.words("english")
exclamation_threshold = 0.05


def check_fake_news(text):
    """
    This function performs basic checks for indicators of fake news using NLTK.
    """
    indicators = 0

    # Tokenize the text (split into words)
    words = nltk.word_tokenize(text)

    # Filter out stop words
    filtered_words = [word.lower() for word in words if word not in stop_words]

    # Check for excessive capitalization
    if any(word.isupper() for word in filtered_words):
        indicators += 1

    # Check for excessive exclamation points
    if (
        len([w for w in filtered_words if w == "!"]) / len(filtered_words)
        > exclamation_threshold
    ):
        indicators += 1

    # Add more checks here using NLTK functionalities (e.g., named entity recognition)

    # Return a basic risk classification based on indicators
    if indicators == 0:
        return "Low Risk"
    elif indicators == 1:
        return "Medium Risk - Consider checking source credibility"
    else:
        return "High Risk - Be cautious of this information"


# Example Usage
text = [
    "BREAKING NEWS! Scientists discover cure for cancer!! You won't believe this!",
    "Scientists make significant progress in cancer research, offering new hope for treatment.",
    "Local bakery wins award for their delicious cupcakes! Congratulations!",
    "The city council is holding a meeting to discuss public transport improvements. Residents are encouraged to attend.",
    "SHOCKING DISCOVERY! You won't believe this cure for baldness! Click here to find out!",
    "Elections rigged! System is corrupt! Share this message to expose the truth!!",
    "BREAKING NEWS: Our country is under imminent threat! Prepare for the worst!",
]


for i in text:
    print(check_fake_news(i))  # Output: High Risk - Be cautious of this information

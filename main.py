
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample News Data
data = {
    "news": [
        "Government launches new education policy",
        "Scientists discover water on Mars",
        "Aliens have taken over the White House",
        "Man becomes invisible after eating banana"
    ],
    "label": [0, 0, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["news"])

# Labels
y = df["label"]

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Take news from user
user_news = input("Enter News: ")

# Convert input text
user_news_vector = vectorizer.transform([user_news])

# Predict
prediction = model.predict(user_news_vector)

# Display Result
if prediction[0] == 0:
    print("Real News")
else:
    print("Fake News")

# Fake News Detection Using Machine Learning

## Project Overview

Fake News Detection is a Python-based Machine Learning project that predicts whether a given news statement is Real News or Fake News.

The project uses Natural Language Processing (NLP), TF-IDF Vectorization, and Logistic Regression for text classification.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Machine Learning
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression

## Features

- Accepts news text from the user.
- Converts text into numerical features using TF-IDF.
- Uses Logistic Regression for classification.
- Predicts Real News or Fake News.
- Displays the prediction in the terminal.

## Project Structure

```text
Fake-News-Detection/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. Sample news data is collected.
2. Pandas creates a DataFrame.
3. TF-IDF converts text into numerical features.
4. Logistic Regression trains on the sample data.
5. The user enters a news statement.
6. The model predicts the result.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Fake-News-Detection
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Project

```bash
python main.py
```

## Sample Output

```text
Enter News: Aliens have taken over the White House

Fake News
```

## Machine Learning Algorithm

**TF-IDF Vectorizer:** Converts news text into numerical features.

**Logistic Regression:** Performs binary classification to predict Real News or Fake News.

## Future Improvements

- Use a large and reliable news dataset.
- Improve model performance.
- Add model evaluation metrics.
- Develop a web-based user interface.
- Improve text preprocessing.

## Limitations

This project currently uses only four sample news statements for demonstration. Therefore, its predictions are not reliable for verifying real-world news.

## Author

**Aaruhi Bharti**

Machine Learning | Python | Computer Science

## License

Created for educational purposes.

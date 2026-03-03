from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pandas as pd

# Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[['label', 'text']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Preprocess
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
# CountVectorizer does tokenization and vectorization
vectorizer = CountVectorizer()
# .fit_transform() learns the vocabulary and creates the document-term matrix
X_train_vec = vectorizer.fit_transform(X_train)
#.transform() uses the learned vocabulary to create the document-term matrix for test data
X_test_vec = vectorizer.transform(X_test)

# Naive Bayes
nb = MultinomialNB()
nb.fit(X_train_vec, y_train)
nb_preds = nb.predict(X_test_vec)

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_vec, y_train)
lr_preds = lr.predict(X_test_vec)

# Results
print("Naive Bayes:\n", classification_report(y_test, nb_preds))
print("Logistic Regression:\n", classification_report(y_test, lr_preds))
import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# csv_path = r"D:\project\spam\spam.csv" 
df = pd.read_csv(r'D:\project\spam\spam.csv', encoding='latin-1')
df = df.rename(columns={df.columns[0]: "label", df.columns[1]: "text"})
df = df[["label", "text"]]
df["label"] = df["label"].str.strip().str.lower()
df = df.dropna().drop_duplicates()

print("Dataset loaded:", df.shape, "rows")
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=2, max_df=0.9)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
])
pipeline.fit(X_train, y_train)
print("Model training completed")
y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n Accuracy: {acc:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nModel saved as sms_spam_model.joblib")
dump(pipeline.named_steps['clf'], "sms_spam_model.joblib")
dump(pipeline.named_steps['tfidf'], "vectorizer.joblib")

print("\nModel and vectorizer saved successfully!")

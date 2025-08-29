import joblib

# Load the trained model and vectorizer
model = joblib.load("sms_spam_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

print("📩 SMS Spam Detector")
print("Type a message to check if it's Spam or Ham.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter a message: ")
    if user_input.lower() == "exit":
        print("Exiting... 👋")
        break
    
    # Transform the input
    input_vector = vectorizer.transform([user_input])
    
    # Predict
    prediction = model.predict(input_vector)[0]
    
    # User-friendly output
    if prediction == "ham":
        print("✅ Ham (Safe message)\n")
    else:
        print("🚨 Spam (Suspicious message!)\n")

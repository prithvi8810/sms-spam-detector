SMS Spam Detector 📩
What is the Project? 🚀
The SMS Spam Detector is a machine learning tool that classifies SMS messages as spam (unwanted) or ham (legitimate). Built with Python, it leverages Logistic Regression and TF-IDF vectorization to analyze text and detect spam with high accuracy.
Project Overview 📊
This project trains a model on a labeled dataset of SMS messages, such as the SMS Spam Collection dataset, to distinguish spam from legitimate messages. Key components include:

train_model.py: 📝 Loads and preprocesses data (removing duplicates, handling missing values), trains a Logistic Regression model with TF-IDF features, and saves the model and vectorizer.
spam_detector.py: 💻 Provides a command-line interface (CLI) for real-time spam/ham predictions on user inputs.
requirements.txt: 📋 Lists dependencies (pandas, scikit-learn, joblib).

The model achieves ~98% accuracy on standard datasets, using robust text preprocessing and balanced classification techniques.
Real-Life Use 🌐
The SMS Spam Detector has practical applications, including:

Mobile Messaging Apps: 📱 Filters out spam texts (e.g., promotions, phishing) for a better user experience.
Telecom Services: 🛡️ Blocks fraudulent SMS to protect customers.
Email and Chat Platforms: 📧 Adapts to detect spam in emails or instant messages.
Cybersecurity: 🔒 Identifies phishing attempts or malicious links in text communications.
Personal Productivity: ✅ Helps users prioritize legitimate messages and reduce distractions.

Use by Example 💡

Train the Model 🧠:

Download the dataset (e.g., spam.csv) and place it in the data/ folder.
Run the training script:python train_model.py


Example Output:Dataset loaded: (5572, 2) rows
Model training completed
Accuracy: 0.9821
Classification Report:
              precision    recall  f1-score   support
       ham       0.99      0.99      0.99       966
      spam       0.93      0.93      0.93       149
   accuracy                           0.98      1115
  macro avg       0.96      0.96      0.96      1115
 weighted avg       0.98      0.98      0.98      1115
Model and vectorizer saved successfully! ✅




Run the Spam Detector 🔍:

Use the CLI to classify messages:python spam_detector.py


Example Interaction:📩 SMS Spam Detector
Type a message to check if it's Spam or Ham.
Type 'exit' to quit.

Enter a message: Win a free iPhone now! Click here.
🚨 Spam (Suspicious message!)

Enter a message: Hey, let's meet at 6 PM.
✅ Ham (Safe message)

Enter a message: exit
Exiting... 👋





import joblib
import pandas as pd

# Load the saved model
model = joblib.load("model/sentiment_model.pkl")

print("✅ Model loaded successfully!")
print("Type 'exit' at any point to stop.\n")

while True:
    title = input("📝 Enter review title: ")
    if title.lower() == "exit":
        print("Exiting...")
        break

    text = input("📝 Enter review text: ")
    if text.lower() == "exit":
        print("Exiting...")
        break

    # Compute review length
    review_length = len(text)

    # Create a DataFrame from input
    user_input = pd.DataFrame([{
        "review_title": title,
        "review_text": text,
        "review_length": review_length
    }])

    # Predict sentiment
    prediction = model.predict(user_input)[0]
    print(f"🔎 Predicted sentiment: {prediction}\n" + "-" * 40)



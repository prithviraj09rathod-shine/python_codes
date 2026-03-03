import pandas as pd

data = {
    "v1": ["ham", "spam", "ham", "spam", "ham"],
    "v2": [
        "Hey, are we still meeting today?",
        "WINNER!! You have won a $1000 Walmart gift card. Go to http://bit.ly/123456",
        "I'll call you later.",
        "URGENT! Your mobile number has won £2000 cash!",
        "Can you send me the report?"
    ]
}

df = pd.DataFrame(data)
df.to_csv("spam1.csv", index=False, encoding='utf-8')
print("spam1.csv created successfully.")
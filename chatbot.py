import re
import json
import os

DATA_FILE = "chatbot_data.json"

# Default FAQ information
default_faqs = {
    "hours": {
        "keywords": ["hours", "timing", "open", "close"],
        "answer": "Our business hours are Monday to Saturday, 9 AM to 6 PM."
    },
    "products": {
        "keywords": ["product", "products", "items", "sell"],
        "answer": "We offer electronics, accessories and daily-use products."
    },
    "price": {
        "keywords": ["price", "cost", "payment", "charges"],
        "answer": "Our prices depend on the product. Please contact our sales team."
    },
    "delivery": {
        "keywords": ["delivery", "shipping", "deliver"],
        "answer": "Standard delivery usually takes 3-5 business days."
    },
    "return": {
        "keywords": ["return", "refund", "exchange"],
        "answer": "Products can be returned within 7 days of delivery."
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "support"],
        "answer": "You can contact our support team at support@example.com."
    }
}


def load_faqs():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump(default_faqs, file, indent=4)

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def get_response(message, faqs):
    message = message.lower().strip()

    # Match FAQ keywords using regular expressions
    for category, details in faqs.items():
        for keyword in details["keywords"]:
            pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

            if re.search(pattern, message):
                return details["answer"]

    return "Sorry, I didn't understand that. Please ask about our hours, products, prices, delivery, returns or contact details."


def chatbot():
    faqs = load_faqs()

    print("\n================================")
    print("       WELCOME TO FAQ BOT")
    print("================================")
    print("Hello! I'm your virtual assistant.")
    
    name = input("May I know your name? ").strip()

    if not name:
        name = "there"

    print(f"\nNice to meet you, {name}!")
    print("You can ask me questions about our services.")
    print("Type 'bye', 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_message = input(f"{name}: ").strip()

        if not user_message:
            print("Bot: Please enter a question.")
            continue

        if re.fullmatch(r"(bye|exit|quit)", user_message, re.IGNORECASE):
            print(f"Bot: Goodbye, {name}! Have a wonderful day!")
            break

        response = get_response(user_message, faqs)
        print("Bot:", response)


if __name__ == "__main__":
    chatbot()
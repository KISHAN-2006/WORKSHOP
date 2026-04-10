from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

def get_response(user_input):
    user_input = (user_input or "").lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Welcome to Grand Stay Hotel 😊 How can I assist you today?"

    # General help
    if any(word in user_input for word in ["help", "options", "what can you do"]):
        return "You can ask about rooms, prices, booking, food, facilities, location, and more."

    # Rooms
    if any(word in user_input for word in ["room", "rooms", "stay"]):
        return "We offer Single, Double, Deluxe, AC, Non-AC, and Family rooms."

    if any(word in user_input for word in ["family", "group"]):
        return "Yes, we have spacious family rooms available."

    if "ac" in user_input:
        return "All AC rooms are fully air-conditioned for comfort."

    if "non ac" in user_input:
        return "We also provide budget-friendly Non-AC rooms."

    # Pricing
    if any(word in user_input for word in ["price", "cost", "rate", "charges"]):
        return "Our prices start from ₹1000 per night depending on room type."

    # Booking
    if any(word in user_input for word in ["book", "booking", "reserve"]):
        return "You can book online or directly at our reception desk."

    if any(word in user_input for word in ["cancel", "cancellation"]):
        return "Bookings can be cancelled up to 24 hours before check-in."

    # Food
    if any(word in user_input for word in ["food", "restaurant", "eat", "dining"]):
        return "We have a 24/7 restaurant with veg and non-veg options."

    if any(word in user_input for word in ["breakfast", "lunch", "dinner"]):
        return "All meals are available. Breakfast is complimentary."

    # Facilities
    if any(word in user_input for word in ["wifi", "internet"]):
        return "Free high-speed WiFi is available."

    if "parking" in user_input:
        return "We provide free parking for all guests."

    if "gym" in user_input:
        return "Yes, we have a fully equipped gym."

    if any(word in user_input for word in ["pool", "swimming"]):
        return "We have a clean and well-maintained swimming pool."

    if "laundry" in user_input:
        return "Laundry service is available."

    if any(word in user_input for word in ["clean", "housekeeping"]):
        return "Daily housekeeping ensures clean and comfortable rooms."

    # Timings
    if any(word in user_input for word in ["check in", "checkin"]):
        return "Check-in time is 12 PM."

    if any(word in user_input for word in ["check out", "checkout"]):
        return "Check-out time is 11 AM."

    # Location
    if any(word in user_input for word in ["location", "where", "address"]):
        return "We are located near the city center for easy access."

    if "airport" in user_input:
        return "The airport is about 10 km from our hotel."

    if any(word in user_input for word in ["station", "railway"]):
        return "The railway station is just 5 km away."

    # Payment
    if any(word in user_input for word in ["payment", "pay", "upi", "card"]):
        return "We accept UPI, credit/debit cards, and net banking."

    # Extra services
    if any(word in user_input for word in ["extra bed", "additional bed"]):
        return "Extra beds are available for ₹500."

    if "kids" in user_input:
        return "Kids below 5 years stay free."

    if "pets" in user_input:
        return "Sorry, pets are not allowed."

    # Offers
    if any(word in user_input for word in ["offer", "discount", "deal"]):
        return "We have seasonal offers and discounts available."

    # Contact
    if any(word in user_input for word in ["contact", "phone", "number"]):
        return "You can contact us at +91 9876543210."

    # Manager / complaint
    if any(word in user_input for word in ["complaint", "issue", "problem"]):
        return "Please contact our reception, we will assist you immediately."

    # Fallback (VERY IMPORTANT 🔥)
    return "I'm here to help 😊 You can ask about rooms, prices, booking, food, or facilities."

@app.route("/")
def home():
    return send_from_directory(".", "website.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = get_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
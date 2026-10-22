
import json
import os

FEEDBACK_FILE = "feedback.json"


# Step 1: User submits a request
def get_request():
    return input("What do you want the agent to do? ")


# Step 2: Agent generates a response
def generate_response(request, feedback_data):
    request_lower = request.lower()

    # Use previously saved feedback when relevant
    if "email" in request_lower:
        response = (
            "Subject: Request for Information\n\n"
            "Dear Sir/Madam,\n\n"
            "I hope you are doing well. I am writing "
            "to request some information.\n\n"
            "Thank you for your time.\n"
            "Best regards"
        )

    elif "study" in request_lower:
        response = (
            "Study Plan:\n"
            "1. Choose a topic.\n"
            "2. Study for 45 minutes.\n"
            "3. Take a 10-minute break.\n"
            "4. Practice questions.\n"
            "5. Review the topic."
        )

    else:
        response = (
            f"You asked: {request}\n"
            "Please provide more details for a specific response."
        )

    # Apply the latest saved preference for future responses
    preference = feedback_data.get("preferences", {}).get(
        "style", ""
    )

    if preference == "short":
        response = "\n".join(response.splitlines()[:4])

    elif preference == "detailed":
        response += (
            "\n\nAdditional suggestion: Review the result "
            "and add any details needed for your situation."
        )

    return response


# Load feedback saved from earlier sessions
def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read feedback. Starting fresh.")

    return {"history": [], "preferences": {}}


# Step 3: User provides feedback
def get_feedback():
    print("\nWas this response useful?")
    print("1. Yes")
    print("2. No")
    print("3. I prefer shorter responses")
    print("4. I prefer more detailed responses")

    choice = input("Choose 1, 2, 3, or 4: ").strip()

    if choice == "1":
        return "positive", None

    elif choice == "2":
        comment = input("What should be improved? ")
        return "negative", comment

    elif choice == "3":
        return "preference", "short"

    elif choice == "4":
        return "preference", "detailed"

    else:
        print("Invalid choice. Feedback not recorded.")
        return None, None


# Step 4: Record useful feedback
def save_feedback(data, request, response, feedback, detail):
    if feedback is None:
        return

    if feedback == "preference":
        data["preferences"]["style"] = detail

    data["history"].append({
        "request": request,
        "response": response,
        "feedback": feedback,
        "detail": detail
    })

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Feedback saved successfully.")


# Step 5: Use feedback in future responses
def main():
    print("=== FEEDBACK-BASED AGENT ===")

    feedback_data = load_feedback()
    request = get_request()

    response = generate_response(request, feedback_data)

    print("\nAgent response:")
    print(response)

    feedback, detail = get_feedback()

    save_feedback(
        feedback_data, request, response, feedback, detail
    )

    print("\nFeedback history:", len(feedback_data["history"]))
    print("Agent session completed.")


if __name__ == "__main__":
    main()

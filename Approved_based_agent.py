
# Authorization-Based Agent
# Python only - no API key required

# Step 1: User requests an action
def receive_request():
    print("=== AUTHORIZATION-BASED AGENT ===")
    request = input("What action do you want the agent to perform? ")
    return request


# Step 2: Agent prepares the action
def prepare_action(request):
    request = request.lower()

    if "email" in request:
        action = "Prepare an email draft"
        details = "Create a professional email draft."

    elif "study" in request:
        action = "Prepare a study plan"
        details = "Create a simple study plan."

    elif "calculate" in request or "add" in request:
        action = "Add two numbers"
        details = "Calculate the sum of two numbers."

    else:
        action = "Display the requested text"
        details = request

    return action, details


# Step 3: Agent requests authorization
def request_authorization(action, details):
    print("\n=== ACTION PREVIEW ===")
    print("Action:", action)
    print("Details:", details)

    while True:
        choice = input(
            "\nAuthorize this action? (yes/no): "
        ).strip().lower()

        if choice in ("yes", "y"):
            return True

        elif choice in ("no", "n"):
            return False

        else:
            print("Please enter yes or no.")


# Step 4: Execute only if authorized
def execute_action(action, details):
    if action == "Prepare an email draft":
        return (
            "Subject: Request for Information\n\n"
            "Dear Sir/Madam,\n\n"
            "I hope you are doing well. I am writing "
            "to request further information.\n\n"
            "Thank you for your time.\n\n"
            "Best regards"
        )

    elif action == "Prepare a study plan":
        return (
            "1. Choose a topic.\n"
            "2. Study for 45 minutes.\n"
            "3. Take a short break.\n"
            "4. Practice questions.\n"
            "5. Review the topic."
        )

    elif action == "Add two numbers":
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            return f"Sum = {first + second}"
        except ValueError:
            return "Execution failed: invalid number."

    else:
        return f"Requested text: {details}"


# Main workflow
def main():
    request = receive_request()

    action, details = prepare_action(request)

    authorized = request_authorization(action, details)

    if authorized:
        print("\nAuthorization granted.")
        result = execute_action(action, details)
        status = "EXECUTED"
    else:
        result = "Action was not executed."
        status = "DENIED"

    # Step 5: Agent reports the outcome
    print("\n=== AGENT OUTCOME ===")
    print("Status:", status)
    print("Result:", result)


if __name__ == "__main__":
    main()

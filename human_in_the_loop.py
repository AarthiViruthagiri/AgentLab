
# Step 1: User submits a request

print("=== MY AI AGENT ===")

user_request = input("Enter your task: ")

# Step 2: Agent performs the task

def ai_agent(task):
    task = task.lower()

    if "email" in task:
        result = """
Subject: Job Application Status

Dear HR Team,

I hope you are doing well.

I would like to kindly enquire about the
status of my job application.

Thank you for your time and consideration.

Best regards,
Applicant
"""
    elif "summary" in task:
        result = "Please provide text to summarize in a future version."
    else:
        result = "Task received: " + task

    return result


result = ai_agent(user_request)

print("\n=== AI AGENT RESULT ===")
print(result)

# Step 3: Human reviews the result

while True:
    print("\n1. Approve")
    print("2. Edit")
    print("3. Reject")
    
    choice = input("Choose an option: ")

    if choice == "1":
        print("\nApproved by human.")
        print("Step 4: Agent completed the task.")
        break

    elif choice == "2":
        result = input("Enter your edited result: ")
        print("\nEdited result:")
        print(result)

    elif choice == "3":
        print("\nResult rejected.")
        print("Task not completed.")
        break

    else:
        print("Invalid choice. Try again.")

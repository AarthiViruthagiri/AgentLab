
# Simple Supervised AI Agent
# No API key and no external libraries

def create_plan(task):
    task = task.lower()

    if "email" in task:
        return [
            "Understand the email request",
            "Prepare an email draft",
            "Check the email draft"
        ]

    elif "study" in task:
        return [
            "Identify the study goal",
            "Prepare a study plan",
            "Review the study plan"
        ]

    else:
        return [
            "Understand the task",
            "Prepare a suggested solution",
            "Review the solution"
        ]


# Step 1: Agent receives a task
task = input("Enter your task: ")

# Step 2: Agent makes decisions
plan = create_plan(task)

print("\nAgent created a plan.")

# Step 3: Human monitors agent activity
for step in plan:
    print("\nAgent is working on:", step)

    while True:
        print("\n1. No issue - Continue")
        print("2. Intervene - Correct")
        print("3. Pause the agent")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Human approved. Agent continues.")
            break

        elif choice == "2":
            correction = input("Enter your correction: ")
            print("Correction received:", correction)
            print("Agent updated its next action.")
            break

        elif choice == "3":
            print("Agent paused.")
            resume = input("Resume the agent? (yes/no): ")

            if resume.lower() == "yes":
                print("Agent resumed.")
                continue
            else:
                print("Task stopped by human.")
                exit()

        else:
            print("Invalid choice. Try again.")

# Step 4: Finish under supervision
print("\nAgent finished the task under supervision!")

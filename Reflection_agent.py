
# Self-Critic Agent
# Python only - no API key required

MAX_RETRIES = 3


# Step 1: Receive a task
def receive_task():
    return input("Enter your task: ").strip()


# Step 2: Generate an initial solution
def generate_solution(task, attempt):
    task_lower = task.lower()

    if "email" in task_lower:
        solution = (
            "Subject: Request for Information\n\n"
            "Dear Sir/Madam,\n\n"
            "I hope you are doing well. I am writing "
            "to request information regarding my enquiry.\n\n"
            "Thank you for your time.\n"
            "Best regards"
        )

    elif "study" in task_lower:
        solution = (
            "1. Choose a topic.\n"
            "2. Study for 45 minutes.\n"
            "3. Take a 10-minute break.\n"
            "4. Practice questions.\n"
            "5. Review the topic."
        )

    else:
        solution = f"Proposed solution for your task: {task}"

    # Example of revision after a failed evaluation
    if attempt > 1:
        solution += "\n\nImprovement: The solution has been reviewed again."

    return solution


# Step 3: Critic evaluates the solution
def critic(solution):
    if not solution.strip():
        return False, "The solution is empty."

    if len(solution.strip()) < 20:
        return False, "The solution needs more detail."

    if "email" in solution.lower():
        if "subject:" not in solution.lower():
            return False, "The email needs a subject."
        if "dear" not in solution.lower():
            return False, "The email needs a greeting."

    return True, "The solution passed the basic checks."


# Step 4: Revise and retry within a limit
def main():
    task = receive_task()

    if not task:
        print("Error: Please enter a task.")
        return

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\nAttempt {attempt} of {MAX_RETRIES}")

        solution = generate_solution(task, attempt)

        print("\nGenerated solution:")
        print(solution)

        passed, reason = critic(solution)

        print("\nCritic evaluation:", reason)

        if passed:
            print("\n=== VALIDATED RESULT ===")
            print(solution)
            print("\nAgent completed successfully.")
            return

        print("Critic requested a revision.")

    print("\nAgent could not validate the result.")
    print("Please review the task manually.")


if __name__ == "__main__":
    main()


# Simple Autonomous Agent
# Python only - no API key required

import datetime
import json

# Step 1: Receive a task or event
def receive_task():
    task = input("Enter your task: ")
    return task


# Step 2: Analyze the situation
def analyze_task(task):
    task = task.lower()

    if "email" in task:
        return "email"

    elif "study" in task:
        return "study"

    elif "calculate" in task or "add" in task:
        return "calculate"

    else:
        return "general"


# Step 3: Select an action
def select_action(task, task_type):
    if task_type == "email":
        return "Create a professional email draft"

    elif task_type == "study":
        return "Create a study plan"

    elif task_type == "calculate":
        return "Ask for two numbers and add them"

    else:
        return "Provide a basic task summary"


# Step 4: Execute automatically
def execute_action(task, task_type):
    if task_type == "email":
        return (
            "Subject: Request for Information\n\n"
            "Dear Sir/Madam,\n\n"
            "I hope you are doing well. I am writing "
            "to request further information regarding "
            "my enquiry.\n\n"
            "Thank you for your time.\n\n"
            "Best regards"
        )

    elif task_type == "study":
        return (
            "Study Plan:\n"
            "1. Identify the topic.\n"
            "2. Study for 45 minutes.\n"
            "3. Take a 10-minute break.\n"
            "4. Practice questions.\n"
            "5. Review what you learned."
        )

    elif task_type == "calculate":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return f"Result: {a + b}"
        except ValueError:
            return "Error: Please enter valid numbers."

    else:
        return f"Task received and analyzed: {task}"


# Step 5: Record the outcome
def record_outcome(task, action, result):
    record = {
        "time": datetime.datetime.now().isoformat(
            timespec="seconds"
        ),
        "task": task,
        "action": action,
        "result": result
    }

    with open("agent_log.jsonl", "a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")

    print("\nOutcome saved to agent_log.jsonl")


# Main agent workflow
def main():
    print("=== AUTONOMOUS AI AGENT ===")

    task = receive_task()

    task_type = analyze_task(task)
    print("\nSituation analyzed:", task_type)

    action = select_action(task, task_type)
    print("Selected action:", action)

    result = execute_action(task, task_type)
    print("\n=== EXECUTION RESULT ===")
    print(result)

    record_outcome(task, action, result)

    print("\nAgent completed its workflow.")


if __name__ == "__main__":
    main()

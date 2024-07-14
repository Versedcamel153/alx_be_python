task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = "that requires immediate attention today!"

match priority:
    case "high" | _ if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task {message}")
    case "high":
        print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "low" | _ if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task {message}")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium" | _ if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task {message} ")
    case "medium":
        print(f"Note:'{task}' is a medium priority task. Consider completing it when you have free time.")


"""
Saving Helper Program
Version 1.3.0
Created by: Torion, Sumaylo, Domingo

Description:
A budgeting tool that helps students track their monthly allowance,
expenses, and saving goals.
"""

def calculate_budget(allowance, expenses):
    """Returns the remaining balance after expenses."""
    return allowance - expenses


def check_saving_goal(difference, goal):
    """Checks if the user reached their saving goal."""
    if difference >= goal:
        return True
    return False


def display_report(name, grade, status, allowance, expenses, difference, goal):
    """Displays formatted budgeting report."""
    print("\n======================================")
    print("         SAVING HELPER REPORT         ")
    print("======================================")
    print(f"Name         : {name}")
    print(f"Grade Level  : {grade}")
    print(f"Status       : {status}")
    print(f"Allowance    : ₱{allowance:.2f}")
    print(f"Expenses     : ₱{expenses:.2f}")
    print("--------------------------------------")

    if difference > 0:
        print(f"Remaining    : ₱{difference:.2f}")
    elif difference == 0:
        print("Remaining    : ₱0.00 (Exact budget used)")
    else:
        print(f"Over Budget  : ₱{abs(difference):.2f}")

    print("--------------------------------------")

    if difference >= 0:
        if check_saving_goal(difference, goal):
            print(f"Saving Goal  : Achieved! 🎉 (Goal was ₱{goal:.2f})")
        else:
            print(f"Saving Goal  : Not achieved. (Goal was ₱{goal:.2f})")

    print("======================================\n")


def main():
    print("======================================")
    print("        === Saving Helper ===        ")
    print("======================================")

    while True:
        try:
            name = input("Enter name: ")
            grade = input("Enter grade level: ")
            status = input("Enter dormer or city scholar: ")

            allowance = float(input("Enter monthly allowance (₱): ").replace("₱", ""))
            expenses = float(input("Enter monthly expenses (₱): ").replace("₱", ""))
            goal = float(input("Enter your saving goal (₱): ").replace("₱", ""))

            if allowance < 0 or expenses < 0 or goal < 0:
                print("Values cannot be negative. Please try again.\n")
                continue

            difference = calculate_budget(allowance, expenses)

            display_report(name, grade, status, allowance, expenses, difference, goal)

        except ValueError:
            print("Invalid input. Please enter numbers only for money values.\n")
            continue

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nThank you for using Saving Helper!")


if __name__ == "__main__":
    main()

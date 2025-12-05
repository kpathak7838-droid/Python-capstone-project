# -------------------------------------------------------
# Project: Household Electricity Use Summary Dashboard
# Name: Kajal Pathak
# Date: 05.12.25
# -------------------------------------------------------

import csv

# This list will store all electricity readings from all files
all_data = []

# -------------------------------
# Task 1: Menu + Welcome Message
# -------------------------------
def show_menu():
    print("\n=== ELECTRICITY USE DASHBOARD ===")
    print("1. Load electricity data")
    print("2. View usage analysis")
    print("3. Show usage trend (text graph)")
    print("4. Export summary")
    print("5. Exit")

print("Welcome to the Electricity Use Dashboard!")


# -------------------------------
# Task 2: Load CSV Files
# -------------------------------
def load_data():
    global all_data
    all_data = []  # clear old data

    n = int(input("How many CSV files do you want to load? (2–3): "))

    for i in range(n):
        filename = input(f"Enter CSV file #{i+1} name: ")

        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    day = row["date"]
                    units = float(row["units"])
                    all_data.append([day, units])
            print(f"Loaded: {filename}")
        except:
            print("Error loading file!")

    print("All files loaded successfully!")


# -------------------------------
# Task 3: Usage Calculations
# -------------------------------
def show_analysis():
    if not all_data:
        print("No data loaded!")
        return

    total = sum(x[1] for x in all_data)
    avg = total / len(all_data)

    # Find min & max
    min_day = min(all_data, key=lambda x: x[1])
    max_day = max(all_data, key=lambda x: x[1])

    print("\n--- USAGE ANALYSIS ---")
    print("Total electricity used:", total)
    print("Average daily usage:", round(avg, 2))
    print("Minimum usage:", min_day[1], "on", min_day[0])
    print("Maximum usage:", max_day[1], "on", max_day[0])


# -------------------------------
# Task 4: Usage Trend (Text Graph)
# -------------------------------
def show_trend():
    if not all_data:
        print("No data loaded!")
        return

    print("\n--- ELECTRICITY USAGE TREND ---")
    print("(Each * represents units used)")

    for day, units in all_data:
        stars = "*" * int(units / 2)   # simple bar
        print(f"{day}: {stars}")


# -------------------------------
# Task 5: Export Summary
# -------------------------------
def export_summary():
    if not all_data:
        print("No data loaded!")
        return

    with open("electricity_summary_output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "units"])
        writer.writerows(all_data)

    print("Summary exported as electricity_summary_output.csv")


# -------------------------------
# Task 6: Menu Loop
# -------------------------------
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        load_data()
    elif choice == "2":
        show_analysis()
    elif choice == "3":
        show_trend()
    elif choice == "4":
        export_summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

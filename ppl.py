def generate_workout_plan(one_rep_maxes, num_weeks):
    # Calculate the starting weight for each lift based on the 1 rep max
    weights = {
        "bench press": one_rep_maxes["bench press"] * 0.65,
        "deadlift": one_rep_maxes["deadlift"] * 0.75,
        "squat": one_rep_maxes["squat"] * 0.75,
        "overhead press": one_rep_maxes["overhead press"] * 0.65,
        "rows": one_rep_maxes["rows"] * 0.65,
        "lat pulldowns": one_rep_maxes["lat pulldowns"] * 0.65,
    }

    # Calculate the number of sets and reps for each lift
    sets_and_reps = {
        "bench press": (4, 6),
        "deadlift": (4, 6),
        "squat": (4, 6),
        "overhead press": (4, 6),
        "rows": (4, 6),
        "lat pulldowns": (4, 6),
    }

    # Calculate the rest time between sets (in seconds)
    rest_time = {
        "bench press": 60,
        "deadlift": 120,
        "squat": 90,
        "overhead press": 60,
        "rows": 60,
        "lat pulldowns": 60,
    }

    # Create a list to store the workout plan
    workout_plan = []

    # Generate the workout plan for each week
    for week in range(num_weeks):
        # Create a dictionary to store the workouts for the week
        week_plan = {}
        week_plan["week"] = week + 1
        week_plan["workouts"] = []

        # Generate the push workout
        push_workout = {}
        push_workout["day"] = "Push"
        push_workout["lifts"] = []
        for lift in ["bench press", "overhead press"]:
            sets, reps = sets_and_reps[lift]
            weight = weights[lift]
            rest = rest_time[lift]
            push_workout["lifts"].append((lift, sets, reps, weight, rest))

        # Generate the pull workout
        pull_workout = {}
        pull_workout["day"] = "Pull"
        pull_workout["lifts"] = []
        for lift in ["rows", "lat pulldowns"]:
            sets, reps = sets_and_reps[lift]
            weight = weights[lift]
            rest = rest_time[lift]
            pull_workout["lifts"].append((lift, sets, reps, weight, rest))

        # Generate the leg workout
        leg_workout = {}
        leg_workout["day"] = "Leg"
        leg_workout["lifts"] = []
        for lift in ["squat", "deadlift"]:
            sets, reps = sets_and_reps[lift]
            weight = weights[lift]
            rest = rest_time[lift]
            leg_workout["lifts"].append((lift, sets, reps, weight, rest))

        # Add the workouts to the week plan
        week_plan["workouts"].append(push_workout)
        week_plan["workouts"].append(pull_workout)
        week_plan["workouts"].append(leg_workout)

        # Add the week plan to the workout plan
        workout_plan.append(week_plan)


def export_to_excel(workout_plan):
    # Create a new Excel workbook
    wb = openpyxl.Workbook()

    # Activate the first sheet
    sheet = wb.active

    # Add the header row
    sheet.cell(row=1, column=1).value = "Day"
    sheet.cell(row=1, column=2).value = "Lift"
    sheet.cell(row=1, column=3).value = "Sets"
    sheet.cell(row=1, column=4).value = "Reps"
    sheet.cell(row=1, column=5).value = "Weight (lbs)"
    sheet.cell(row=1, column=6).value = "Rest (seconds)"

    # Add the workout plan to the sheet
    for row, workout in enumerate(workout_plan, start=2):
        for lift in workout["lifts"]:
            sheet.cell(row=row, column=1).value = workout["day"]
            sheet.cell(row=row, column=2).value = lift[0]
            sheet.cell(row=row, column=3).value = lift[1]
            sheet.cell(row=row, column=4).value = lift[2]
            sheet.cell(row=row, column=5).value = lift[3]
            sheet.cell(row=row, column=6).value = lift[4]
            row += 1

    # Save the workbook
    wb.save("workout_plan.xlsx")

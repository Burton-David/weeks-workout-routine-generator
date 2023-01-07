def generate_tut_workout(muscles, tut, sets_and_reps):
    # Create a list to store the workout
    workout = []

    # Choose the exercises for each muscle group
    exercises = {
        "chest": ["bench press", "incline press"],
        "back": ["rows", "lat pulldowns"],
        "legs": ["squat", "leg press"],
        "shoulders": ["overhead press", "lateral raises"],
        "arms": ["bicep curls", "tricep dips"],
    }

    # Generate the workout
    for muscle in muscles:
        # Choose the exercises for the muscle group
        muscle_exercises = exercises[muscle]

        # Calculate the rest time between sets (in seconds)
        rest_time = tut[muscle] / sets_and_reps[muscle][0]

        # Add the exercises to the workout
        for exercise in muscle_exercises:
            sets, reps = sets_and_reps[muscle]
            workout.append((exercise, sets, reps, tut[muscle], rest_time))

    return workout


# Example usage:
muscles = ["chest", "back", "legs"]
tut = {
    "chest": 60,
    "back": 60,
    "legs": 60,
}
sets_and_reps = {
    "chest": (4, 8),
    "back": (4, 8),
    "legs": (4, 8),
}
workout = generate_tut_workout(muscles, tut, sets_and_reps)
print(workout)


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

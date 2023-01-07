def generate_5310(one_rep_maxes):
    # Calculate the weights for each set
    weights = {
        "bench press": [one_rep_maxes["bench press"] * 0.65,
                        one_rep_maxes["bench press"] * 0.7,
                        one_rep_maxes["bench press"] * 0.75,
                        one_rep_maxes["bench press"] * 0.8,
                        one_rep_maxes["bench press"] * 0.85,
                        ],
        "deadlift": [one_rep_maxes["deadlift"] * 0.65,
                     one_rep_maxes["deadlift"] * 0.7,
                     one_rep_maxes["deadlift"] * 0.75,
                     one_rep_maxes["deadlift"] * 0.8,
                     one_rep_maxes["deadlift"] * 0.85,
                     ],
        "squat": [one_rep_maxes["squat"] * 0.65,
                  one_rep_maxes["squat"] * 0.7,
                  one_rep_maxes["squat"] * 0.75,
                  one_rep_maxes["squat"] * 0.8,
                  one_rep_maxes["squat"] * 0.85,
                  ],
    }

    # Create a list to store the 5/3/1 routine
    routine = []

    # Generate the 5/3/1 routine
    for exercise in ["bench press", "deadlift", "squat"]:
        routine.append((exercise, weights[exercise][0], 5))
        routine.append((exercise, weights[exercise][1], 3))
        routine.append((exercise, weights[exercise][2], 5))
        routine.append((exercise, weights[exercise][3], 3))
        routine.append((exercise, weights[exercise][4], 1))

    return routine


def export_to_excel(routine):
    # Create a workbook and add a worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Add the headers
    worksheet.append(["Exercise", "Weight", "Reps"])

    # Add the routine
    for exercise, weight, reps in routine:
        worksheet.append([exercise, weight, reps])

    # Save the workbook
    workbook.save("5-3-1.xlsx")

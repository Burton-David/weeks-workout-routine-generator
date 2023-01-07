# weeks-workout-routine-generator
## How to Use
* Install the required libraries: openpyxl
* Choose 1 of the python files,they will all generate a unique type of workout described below.
* Update the one_rep_maxes dictionary with your personal 1 rep max values for each lift.
* Set the number of weeks for the workout plan in the num_weeks variable.
* Run the program using the Python interpreter: python workout_plan_generator.py
* The final workout plan will be printed to the console and also exported to an Excel file named workout_plan.xlsx.
## Version1 is a generic routine using 1rm
## PPL
This program generates a progressive overload workout plan for a push/pull/leg training split. The workouts are spaced out appropriately for recovery, and all the lifts include the weight in lbs to use based on the user's 1 rep max. Rest times are also included in the plan.
### Customization
You can customize the program by modifying the following variables:

* weights: The starting weight for each lift based on the 1 rep max
* sets_and_reps: The number of sets and reps for each lift
* rest_time: The rest time between sets (in seconds)
You can also modify the formula used to increase the weights on each subsequent week. The current formula increases the weights by 5% on each subsequent week.
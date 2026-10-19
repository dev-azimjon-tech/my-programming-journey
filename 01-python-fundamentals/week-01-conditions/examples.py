"""Examples for Week 1: conditions and Boolean logic.

Run this file, predict the output, then change the values and run it again.
"""


# A simple if/else decision.
temperature = 18

if temperature < 0:
    print("Water may freeze.")
else:
    print("Water is not below freezing.")


# Several mutually exclusive branches.
score = 82

if score >= 90:
    level = "excellent"
elif score >= 70:
    level = "good"
else:
    level = "needs practice"

print(f"Result: {level}")


# Combining conditions with and/or.
age = 17
has_permission = True

can_join_event = age >= 16 and has_permission
print(f"Can join event: {can_join_event}")


# Using not to invert a Boolean value.
is_raining = False

if not is_raining:
    print("You can go for a walk without an umbrella.")

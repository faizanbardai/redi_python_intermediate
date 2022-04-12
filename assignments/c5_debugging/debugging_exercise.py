# Exercise using the PyCharm Debugger
#
# 1. First read the code and try to understand what the intention of the program is.
# 2. Then try to find the any mistakes in the code. For the 3 patients we expect
#    the following BMI scores:
#       1. Patient - BMI of 21.605
#       2. Patient - BMI of 22.160
#       3. Patient - BMI of 51.903
#
#    Use this given results as check if you have fixed the program correctly.
# 3. Try to make use of the PyCharm Debugger to find


# We want to calculate the body mass index for these 3 patients.
# From each patient we have stored their weight (in kilogram) and height (in meters) in a tuple.

patients = [(70, 1.8), (80, 1.9), (150, 1.7)]


def calculate_bmi(patient):
    # See here https://en.wikipedia.org/wiki/Body_mass_index#History
    # for the formula to calculate the body mass index given the weight (in kilogram)
    # and height (in meters).
    weight, height = patient
    bmi = weight / (height ** 2)
    return bmi

# problem 1: not running through all the patients
# problem 2: patient index is hard-coded
# problem 3: wrong param order
# problem 4: print bmi to 3 decimal places
# suggestion: improve code


for patient in patients:
    bmi = calculate_bmi(patient)
    print("Patient's BMI is: %0.3f" % bmi)

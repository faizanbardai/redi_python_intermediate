# 1. Download the file exercise2.txt from Google Classroom
# 2. Calculate the number of lines in the file.
# 3. Append the Number of lines at the End of the File.

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'exercise2.txt'

number_of_lines = 0

with open(path, 'r') as file:
    for line in file.readlines():
        number_of_lines += 1

with open(path, 'a') as file:
    file.write('Number of lines : ' + str(number_of_lines))

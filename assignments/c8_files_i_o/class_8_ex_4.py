# 1. Download the file exercise2.txt from Google Classroom
# 2. Calculate the number of lines in the file.
# 3. Append the Number of lines at the End of the File.

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'exercise2.txt'


with open(path, 'r+') as file:
    number_of_lines = len(file.readlines())

    file.write('Number of lines : ' + str(number_of_lines))

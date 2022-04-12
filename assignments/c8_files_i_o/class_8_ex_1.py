# 1. Create an empty txt file and name it exercise1.txt (pay attention to where you save it)
# 2. Ask the user to write 2 lines of text (line1 and line2)
# 3. In your Python script, write those lines to the file

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'exercise1.txt'

line1 = input('Please write line 1: ')
line2 = input('Please write line 2: ')

with open(path, 'w') as file:
    file.write(line1)
    file.write('\n')
    file.write(line2)

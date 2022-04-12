"""
Exercise: Add logging statements to check how much time "my_slow_function" requires!

- Add log statements to the code below
- Looking at the log messages: How much time does the function require?
- Is the time constant for each run?
- What happens if you go from 1_000_000 to 10_000_000?
"""

import logging

logging.basicConfig(
  # TODO: Add the time to the format!
  format='%(name)s %(levelname)-8s %(message)s',
  level=logging.INFO,
)

logger = logging.getLogger(__name__)

def my_slow_function():
  result = 0
  for i in range(1_000_000):
    result += i*i
  return result


# TOOD: Add a log statement here
result = my_slow_function()
# TOOD: Add a log statement here
print(result)
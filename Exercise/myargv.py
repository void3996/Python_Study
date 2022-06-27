import numbers
import sys
from unittest import result

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)
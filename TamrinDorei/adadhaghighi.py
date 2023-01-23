
import re
def real_numbers(numbers):
    main_list = []
    for item in numbers:
        if re.match(r'^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$', item):
            main_list.append("LEGAL")
        else:
            main_list.append("ILLEGAL")
    return main_list


print(real_numbers(['1.5e+2', '3.', '1.1.1', '1+e5']))
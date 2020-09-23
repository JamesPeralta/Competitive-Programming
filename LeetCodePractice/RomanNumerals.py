roman_nums = {"I": 1, "II": 2, "III": 3, "IV": 4,
              "V": 5, "VI": 6, "VII": 7, "VIII": 8,
              "IX": 9, "X": 10, "XX": 20, "XXX": 30,
              "XL": 40, "L": 50}

rev_roman_nums = inv_map = {v: k for k, v in roman_nums.items()}


def build_roman_num(number):
    ten_multiple = (number // 10) * 10
    remainder = number - ten_multiple

    if remainder == 0:
        return rev_roman_nums[ten_multiple]
    else:
        return rev_roman_nums[ten_multiple] + rev_roman_nums[remainder]


def generate_roman_nums_map():
    for num in range(11, 50):
        roman_string = build_roman_num(num)
        if roman_string not in roman_nums:
            roman_nums[roman_string] = num


def sort_by_roman_value(name):
    return roman_nums[name.split(" ")[1]]


def extract_name(name):
    return name.split(" ")[0]


def sort_roman(names):
    # Generate roman_nums
    generate_roman_nums_map()

    possible_names = [[] for _ in range(1, 51)]
    names = sorted(names, key=extract_name)

    index = 0
    bucket = -1
    last_name = None
    # Perform bucket sort where each matching name first name
    # goes into the same bucket
    while index < len(names):
        if extract_name(names[index]) != last_name:
            bucket += 1
            possible_names[bucket].append(names[index])
            last_name = extract_name(names[index])
        else:
            possible_names[bucket].append(names[index])

        index += 1

    # Go through each bucket and sort it by their roman numeral
    output = []
    for conflicts in possible_names:
        output += sorted(conflicts, key=sort_by_roman_value)

    return output


# arr = ["Louis IX", "Louis VIII"]
# arr = ["Philip II", "Philippe I"]
# arr = ["David IX", "Mary XIII", "Mary XV", "Mary XX", "Steven XVI", "Steven XL"]
arr = ['Louis V', 'Louis VI', 'Louis X', 'Peter I']
print(sort_roman(arr))

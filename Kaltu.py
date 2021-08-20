# 1
# Define a function that receive a string as argument and prints it backwards. For example, the
# string “Automation” gets printed as: “noitamotuA”

def backwards(string: str) -> str:
    return string[::-1]


print(backwards('Automation'))

# 2
# Define a function that takes a list of strings and prints them, one per line, in a rectangular frame.
#  ["Hello", "World", "in", "a", "frame"]


def add_frame(str_list: list) -> None:
    biggest_str = max(str_list, key=len)
    print('*' * (len(biggest_str) + 4))
    for string in str_list:
        print(f'* {string}' + ' ' * (len(biggest_str)-len(string)) + ' *')
    print('*' * (len(biggest_str) + 4))


add_frame(["Hello", "World", "in", "a", "frame"])

# 3
# Define a function that receive a list with numbers and strings and return a list only with the
# numbers without duplicates.
to_be_used = [1, 3, 67, "1", "62", "Foo", "3", 5, 1, 3, False, 1.3]


def remove_duplicates(lst: list) -> list:
    only_numbers = set()
    for item in lst:
        if (isinstance(item, int) or isinstance(item, float)) \
                and not isinstance(item, bool):
            only_numbers.add(item)
    return list(only_numbers)


print(remove_duplicates(to_be_used))

# 4
# Define a function that receive as a single argument a list of strings like the below variable and
# return a dictionary that contains as keys “Video”, “Audio”, “Other” and as values a list with the
# entries specific for that key.
results = ["Entry One.mp4", "Entry Two.wav", "Entry Three.jpg", "Entry Four.mng",
"Entry Five.png", "Entry Six.csv"]


def group(lst: list) -> dict:
    result = {'Video': [], 'Audio': [], 'Other': []}
    for item in lst:
        if item.split('.')[1] in ['mp4', 'mov', 'wmv', 'avi']:
            result['Video'].append(item)
        elif item.split('.')[1] in ['mp3', 'wav', 'aac']:
            result['Audio'].append(item)
        else:
            result['Other'].append(item)
    return result


print(group(results))

# 5
# Find out how many rabbits are after N years knowing the following
# n_years = input
# number_rabbits = input
# rabbits_births_number = input
# *Each rabbit can give birth only within the first two years
# *Rabbits live only four years


# run for n_years, rabbits die after y years.
n_years, number_rabbits, rabbits_birth_number = input(
    "Enter years to run, the number of rabbits, and the rabbits birth number separated by a space ").split()
n_years, number_rabbits, rabbits_birth_number = int(n_years), int(number_rabbits), int(rabbits_birth_number)

generations = [1, 1]  # Seed the sequence with the 1 pair, then in their reproductive year.


def fib(i, j):
    count = 2
    while count < i:
        if count < j:
            # recurrence relation before rabbits start dying (fib seq Fn = Fn-2 + Fn-1)
            generations.append(generations[-2] + generations[-1])
        elif count == j or count == j+1:
            # base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            print ("in base cases for newborns (1st+2nd gen. deaths)")
            generations.append((generations[-2] + generations[-1]) - 1)  # Fn = Fn-2 + Fn-1 - 1
        else:
            # the recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)]))
        count += 1
    return generations[-1]


print(fib(n_years, 4))
print("Here's how the total population looks by generation: \n" + str(generations))

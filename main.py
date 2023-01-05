import colorama
from colorama import Fore
import pandas as pd

# Initialing the variables
CAST = []
NEW_CAST = []
temp_list = []

# Display
print(Fore.LIGHTCYAN_EX + "\x1B[4mCPSC 535 Advance Algorithm\x1B[0m\n")
print(Fore.LIGHTMAGENTA_EX + "\x1B[4mPROJECT - ITS A SMALL WORLD\x1B[0m")
print(Fore.LIGHTWHITE_EX+"---------------------------\n")

print(Fore.LIGHTBLUE_EX + "\x1B[4m\033[1;3mInput Variables:\033[0m\x1B[0m")
print(Fore.LIGHTBLUE_EX + "----------------")
print(Fore.LIGHTWHITE_EX + "Reading the input from the csv file.\n")

print(Fore.LIGHTYELLOW_EX + "\x1B[4m\033[1;3mOutput:\033[0m\x1B[0m")
print(Fore.LIGHTYELLOW_EX + "-------")

# Reading data from the CSV file
file1 = pd.read_csv("Datafile4.csv")

# To count the number of columns in the excel-sheet
count_of_columns = 0
for column in file1:
    count_of_columns += 1

# Adding the data to the list from the file
for i in file1:
    CAST.append(file1[i].tolist())

# To remove "nan" from the retrieved list from the excel-sheet
NEW_CAST = [list(filter(lambda word: word == word, inner_list)) for inner_list in CAST]

# Initiating the temporary lists for cast0 and cast1
temp_cast_list0 = NEW_CAST[0]
temp_cast_list1 = NEW_CAST[1]


# Case 1:
def simple_case_1():
    for element_in_zero in temp_cast_list0:
        for element_in_one in temp_cast_list1:
            if element_in_zero == element_in_one:
                return "Shortest Connection = 1, Actor/Actress = " + "".join(element_in_zero)


# Case 2:
def simple_case_2():
    for item0 in temp_cast_list0:
        for i in range(2, len(NEW_CAST)):
            for j in NEW_CAST[i]:
                if item0 in NEW_CAST[i]:
                    for item1 in temp_cast_list1:
                        if item1 == j:
                            return "Shortest Connection = 2, ", NEW_CAST[i]


# Calling the required functions
result_1 = simple_case_1()
result_2 = simple_case_2()

# Printing the results
if result_1 is not None:
    print(result_1)
elif result_2 is not None:
    print(result_2)
else:
    print("Shortest Connection > 2 or no connection")

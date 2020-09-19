"""This file converts a csv file's data so that any selected collumn
is converted into a string. The primary use for this is to make excel
spreadsheets better for data anaylsis"""

# File that is read from
filename = ('data.txt')
# File that is written to
filename_2 = ('data_2.txt')

# Contains the column number that will be converted to strings
convert_column_num = []

# counter for while loop for convert_column_num
i = 1
# counter for...
j = 0

# bool so that first line in a csv is completely converted to strings
# make False to turn this feature off
first_time = True

# For the number of columns
column_num = input("Enter the number of columns: ")

# Input Validation
while type(column_num) != int:
    try:
        column_num = int(column_num)
    except ValueError:
        try:
            column_num = input("Invalid input! Enter a new number here: ")
        except ValueError:
            continue

# Erases file before starting
with open(filename_2, 'w') as f_2:
    f_2.write('')

# For the list that is used to determine what columns
# are converted to strings
with open(filename) as f:
    while i < column_num + 1:
        column_choice = input(f'Do you want column number {i} to have quotations y or n: ')
        if column_choice == 'y' or column_choice == 'n':
            if column_choice == 'y':
                convert_column_num.append(i - 1)
                i += 1
            else:
                i += 1
                continue
        else:
            while column_choice != 'y' and column_choice != 'n':
                column_choice = input("Invalid input enter either y or n:")
                if column_choice == 'y':
                    convert_column_num.append(i - 1)
                    i += 1
                elif column_choice == 'n':
                    i += 1
                    continue

# changes values to the correct data type and writes them to the right file
with open(filename, 'r+') as f:
    new_words = list()
    for line in f:
        # converts first line entirely to as strings
        if first_time:
            words = line.split(',')
            for num in range(len(words)):
                new_words.insert(num, f"{words[num]}")
                #print(new_words)
            with open(filename_2, 'a') as f_2:
                for word in range(len(new_words)):
                    if word == column_num-1:
                        f_2.write(f'"{new_words[word].rstrip()}"\n')
                    else:
                        f_2.write(f'"{new_words[word]}",')
            new_words.clear()
            first_time = False
        # does every other line
        else:
            words = line.split(',')
            for num in range(len(words)):
                if num in convert_column_num:
                    # converts to string
                    new_words.insert(num, f"{words[num]}")
                else:
                    try:
                        # converts to int
                        if words[num] == 'None' or words[num] == f'None\n':
                            new_words.insert(num, f'{words[num].rstrip()}')
                        else:
                            new_words.insert(num, int(words[num]))
                    # Input validation
                    except ValueError:
                        print("\nError: Column numbers entered incorrectly.!")
                        print("Make sure to enter column numbers correctly.")
                        exit()

                # writes the values to the file
                with open(filename_2, 'a') as f_2:
                    for word in range(len(new_words)):
                        if type(new_words[word]) == int:
                            if j == column_num-1:
                                f_2.write(f"{new_words[word]}\n")
                                j = 0
                            else:
                                f_2.write(f"{new_words[word]},")
                                j += 1
                        else:
                            if j == column_num-1:
                                f_2.write(f'"{new_words[word]}"\n')
                                j = 0
                            else:
                                f_2.write(f'"{new_words[word]}",')
                                j += 1

                new_words.clear()





    # f.write('stuff)
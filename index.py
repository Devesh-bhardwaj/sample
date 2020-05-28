listl1 = [int, float, 12, 3, 4, 11, 6, 7]

for item in listl1:
    if str(item).isnumeric() and item > 6:
        print(item,' Is greater then 6')
    elif item != str(item).isnumeric():
        print('item is not a number')
    else:
        print('number is less then six')

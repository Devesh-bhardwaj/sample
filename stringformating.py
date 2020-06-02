import datetime as dt

my_date = dt.datetime(2020, 7, 2, 12, 45, 55)

sentence = '{: %B %d,%Y}'.format(my_date)

print(sentence)


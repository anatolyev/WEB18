from random import shuffle

lst = ['Иннокентий+Михаил',
       'Роман',
       'Никита+Дарья',
       'Никита+Егор',
       'Давид',
        'Егор']

shuffle(lst)

print(*lst, sep="\n")


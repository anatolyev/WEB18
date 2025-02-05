from zipfile import ZipFile

with ZipFile('archive.zip') as myzip:
    myzip.printdir()
    print()
    print(myzip.namelist())
    with myzip.open('3/Описание.txt', 'r') as f:
        print(f.read().decode('utf8'))

with ZipFile('archive.zip', 'a') as myzip:
    myzip.write('ex1.json')
    print(myzip.namelist())





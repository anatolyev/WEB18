import os


for curdir, dirs, files in os.walk('data'):
    spaces = "   " * curdir.count("/")
    print(spaces + "📁 " + str(curdir.split("/")[-1]))
    if files:
        for f in files:
            print(spaces + "   - " + f)

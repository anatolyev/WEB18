import shutil

# shutil.copy('data/3/Описание.txt', 'data/Описание - копия.txt')
# shutil.rmtree('data/3/files')
# shutil.move('data/1', 'data/3/')
shutil.make_archive('archive', 'zip', root_dir="data")



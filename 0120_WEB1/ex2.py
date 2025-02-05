import os

print(os.name)
print(dir(os))
print(os.getcwd())
# os.mkdir('files')
os.chdir('files')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
print(os.access("files", os.F_OK))
print(os.access("files", os.W_OK))
print(os.access("files", os.R_OK))
print(os.listdir())
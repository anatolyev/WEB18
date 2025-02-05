from zipfile import ZipFile

with ZipFile('archive.zip') as myzip:
    myzip.extractall(path='exctract',
                     members=None,
                     pwd=None)

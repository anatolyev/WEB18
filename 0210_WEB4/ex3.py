import argparse

parser = argparse.ArgumentParser()
parser.add_argument("integers", metavar="Целые числа", nargs='+',
                    type=str, help="Перевод двоичных чисел в десятичные")
args = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, 2)), args.integers))
print(result)
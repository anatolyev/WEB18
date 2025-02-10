import argparse

parser = argparse.ArgumentParser()
parser.add_argument("integers", metavar="Целые числа", nargs='+',
                    type=str, help="Перевод двоичных чисел в десятичные")
parser.add_argument("--base", default=2, type=int,
                    help="Основание системы счисления")
args = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, args.base)), args.integers))
print(result)
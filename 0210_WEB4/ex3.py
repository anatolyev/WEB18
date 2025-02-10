import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("integers", metavar="Целые числа", nargs='+',
                    type=str, help="Перевод двоичных чисел в десятичные")
parser.add_argument("--base", default=2, type=int,
                    help="Основание системы счисления")
parser.add_argument("--log", default=sys.stdout, type=argparse.FileType('a'),
                    help="Запись результата в лог-файл")
args = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, args.base)), args.integers))
args.log.write(result + '\n')
args.log.close()

#!/usr/bin/env python3.11
import sys

if len(sys.argv) > 1:
    print(f"Имя файла: {sys.argv[0]}\n"
          f"Первый аргум: {sys.argv[1]}\n"
          f"Последний аргум: {sys.argv[-1]}\n")
else:
    print(f"В файле: {sys.argv[0]} нет переданных аргументов\n")

import sys

if len(sys.argv) > 1:
    a = sys.argv[1:]
    print(sum([int(i) for i in a]))
    print(sum([int(i) for i in a]) / len(a))
else:
    print("No argv")
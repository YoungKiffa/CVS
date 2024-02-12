import sys

n, m = map(int, input().split())

with open('exam.csv', 'w', encoding='utf-8') as file:
    file.write("Surname;Name;Result 1;Result 2;Result 3;Total\n")

    while True:
        line = sys.stdin.readline().rstrip("\n")
        if not line:
            break
        surname, name, *results = line.split()
        results = [int(result) for result in results]
        if sum(results) >= n and all(result >= m for result in results):
            file.write(f"{surname};{name};{';'.join(map(str, results))};{sum(results)}\n")

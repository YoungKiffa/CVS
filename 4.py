import sys
n, m = map(int, input().split())
with open('exam.csv', 'w', encoding='utf=8') as file:
    file.write("Фамилия;имя;результат 1;результат 2;результат 3;сумма\n")

    while True:
        line = sys.stdin.readline().rstrip("\n")
        if line == '':
            break
        surname, name, result1, result2, result3 = line.split()
        result1, result2, result3 = int(result1), int(result2), int(result3)
        total = result1 + result2 + result3
        if total >= n and result1 >= m and result2 >= m and result3 >= m:
            file.write(f"{surname};{name};{result1};{result2};{result3};{total}\n")
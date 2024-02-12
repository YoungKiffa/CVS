import sys
n, m = map(int, input().split())
with open('exam.csv', 'w', encoding='utf=8') as file:
    file.write("Фамилия;имя;результат 1;результат 2;результат 3;сумма\n")

# 求解多元方程
import numpy as np


def work():
    flag = 1
    while flag == 1:
        n = int(input("请输入你要求的未知数的个数:"))
        print("你需要%d个方程组" % n)
        number = np.zeros((n, n + 1), dtype=float)
        if input_data(n, number):
            simplify(n, number)
            if judge(n, number):
                calculate(n, number)

        print("是否需要求解新的方程组[Y/N]")
        d = input()
        if d == 'N':
            flag = 0
        elif d == 'Y':
            flag = 1
        else:
            print("输入错误!")
            exit()


def input_data(n, number):
    try:
        for i in range(0, n):
            print("请输入第%d个方程的系数(每输入一个数字后回车输入下一个):" % (i + 1))
            for j in range(0, n):
                number[i][j] = float(input())
            number[i][n] = float(input("请输入第%d个方程的常数(回车代表结束):" % (i + 1)))
    except ValueError:
        print("输入错误！请重试")
        return False

    print("输入如下:")
    print(number)
    return True


def simplify(n, number):
    begin = 0
    for i in range(n):
        figure = find_max(i, begin, n, number)
        exchange(figure, begin, number, n)
        count(n, number, begin)
        begin = begin + 1
    print("最后化简得:")
    print(number)


def calculate(n, number):
    a = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        a[i] = sum_count(n, number, a, i)/number[i][i]
    print("解得:")
    for i in range(n):
        print("x%d为%f" % (i, a[i]))


def sum_count(n, number, a, i):
    all_num = number[i][n]
    for j in range(n - 1, i, -1):
        all_num = all_num - a[j] * number[i][j]
    return all_num


def judge(n, number):
    x = 0
    for i in range(n):
        if number[n - 1][i] == 0:
            x = x + 1

    if x == n:
        print("该方程组没有解或者无穷解")
        return False
    else:
        print("该方程组有唯一解")
        return True


def find_max(i, begin, n, number):
    figure = i
    for j in range(begin, n):
        if abs(number[j][i]) > abs(number[figure][i]):
            figure = j

    return figure


def exchange(figure, begin, number, n):
    a = np.zeros((n + 1), dtype=float)
    for i in range(n + 1):
        a[i] = number[figure][i]
        number[figure][i] = number[begin][i]
        number[begin][i] = a[i]


def count(n, number, begin):
    for i in range(begin + 1, n):
        for j in range(begin + 1, n + 1):
            number[i][j] = number[i][j] - (number[i][begin] * number[begin][j])/number[begin][begin]
    for i in range(begin + 1, n):
        number[i][begin] = 0


if __name__ == '__main__':
    work()

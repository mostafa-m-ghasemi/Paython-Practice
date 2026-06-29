import functools as ft


text = "2+3+4+5+6+7+8+9"
print(sum(list(map(int, text.split("+")))))

print(ft.reduce(lambda x, y: x + y, list(map(int, text.split("+")))))

print(eval(text))
# 1. Програма-світлофор.
#   Створити програму-емулятор світлофора для авто і пішоходів.
#   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#   Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Green
#      Yellow     Green
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green
import time
print("car          people")
print("")

while True:
    for i in range(10):                           #светититься 10 секунд
        print("red          green")
        time.sleep(1)

    for i in range(5):                            #светититься 5 секунд
        print("yellow          green")
        time.sleep(1)

    for i in range(15):                           #светититься 15 секунд
        print("green          red")
        time.sleep(1)

    for i in range(5):                            #светититься 5 секунд
        print("yellow          red")
        time.sleep(1)

# Задание № 6
## Определение результатов работы простейших алгоритмов


[Ссылка на задания (Решу ЕГЭ)](https://inf-ege.sdamgia.ru/)

### **О задании**


В этом задании нас просят посчитать целочисленные точки внутри какой-то фигуры. Большинство решений приводиться в среде разработки `КУМИР`. Однако, для решения более сложных задач, где количество точек может достигать 1000, считать вручную не эффективно и долго.


1. [Есть всего один вид данного задания - посчитать точки](https://inf-ege.sdamgia.ru/test?theme=316)



### **Варианты решения**

В большинстве случаев задания не содержат больших значений для точек. Поэтому мы можем решить используя среду программирования Кумир.

У вас на компьютерах должно быть установлено данное приложение. Далее, вы можете использовать параметр `вставка` в верхней строке. Используя их просто перепишите то, что требуеться в задании и запустите программу.

На выходе вы получите фигуру, целочисленные точки которой вам требуеться посчитать. 

Алгоритмический язык программирования довольно прост и интуитивно понятен тем, кто хоть раз его видел.


Но! Как я уже упоминал ранее, существуют задания, где количество точек такое большое, что решить первым спопсобом просто невозможно или долго. 

В [коде](/tasks/task6/task6.py) вы можете увидеть много коментариев. Это не просто так. Дело в том, что код получился довольно мудреным, но это не делает его более сложным, чем другие.

Для решения этим способом нам обязательно потребуеться модуль turtle. Он встроен в python, а это значит, что он обязательно будет на экзамане.

> from turtle import *

Теперь можно начать подготовку:

1. Зададим используемые цвета.
   > color("blue", "red")
    
    Первый цвет может быть любым, а второй обязательно красный. Дело в том, что в будущем мы будем сравнивать цвет заливки с некоторым значением.
2. Теперь зададим скорость, скоторой будет двигаться наша черепашка
   > speed(0)

   Ставя скорость в значение 0, мы как бы указываем, что скорость должна быть максимальной.
3. Зададим масштаб
   > m = 50
   В целом, масштаб даже и не нужен, но лучше его использовать для наглядности.
4. Начнем заливку и программу
   > begin_fill() <br>
   > ваша программа
5. После завершения написания программы останавливаем заливку
   > end_fill()
6. Создадим канвас для работы с графическими эллементами фигуры и счетчик для точек
   > canvas = getcanvas() <br>
   > count_points = 0
7. теперь нам нужно пробежаться по всем точкам в нашем диапозоне( незабываем про масштаб) и проверить, не находиться ли эта точка (c координатами `x` и `y`) в канвасе.
   ```python
   for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        # записываем в переменную значение пересечения фигуры в скобках и нашего канваса
        item = canvas.find_overlapping(x, y, x, y)
        # проверяем пересечения
        if len(item) == 1 and item[0] == 5:
            count_point += 1
    ```

    Логика проста - если пересечение есть, то длина нашего `item` будет 1. Это доказывает, что есть одно пересечение. И цвет пересечения соответсвует коду 5 (красный). Это для того, чтобы обводка не считалась.

8. Теперь мы можем вывести полученное количество точек и радоваться

Данное решение сработает так же и с маленьким количеством точек. Однако здесь мало просто заучить код, важно его понять, уметь применять и редактировать по заданию.

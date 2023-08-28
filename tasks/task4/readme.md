# Задание № 4
## Кодирование и декодирование инфомации


[Ссылка на задания (Решу ЕГЭ)](https://inf-ege.sdamgia.ru/)

### **О задании**

В 4-ом задании нам требуеться знать что такое условие [Фано](https://ru.wikipedia.org/wiki/%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5_%D0%A4%D0%B0%D0%BD%D0%BE), как строить бинарные деревья и уметь правильно подбирать значения.

Это задание программно не решаеться. Это связано с тем, что большинство цепочек для старта нам уже даны.


Задание разделяеться на два типа:
1. [Выбор кода при неиспользуемых сигналах](https://inf-ege.sdamgia.ru/test?theme=369)
2. [Передача информации. Выбор кода](https://inf-ege.sdamgia.ru/test?theme=232)

Решение обоих типовпроисходит схожими способами.


### **Варианты решения**

Как я уже упомянул ранее решение с помощью кода на данный момент непридумали...

Так что нам придеться перебирать варманты вручную. Для примера возьмем задачу:

![image](/other/example-4.png)

Как мы видим у нас уже есть некоторые буквы:
1. A - 010
2. Б - 011
3. Г - 100
   
Слово `МАГИЯ` необходимо закодировать по условию Фано. И найти минимальное количество двоичных знаков. 

Построим бинарное дерево для того, что у нас уже есть:

![image](/other/image-4-1.png)


Красным отмечены коды для букв, если после последовательности стоит буква, то это значит, что дальше мы идти не можем (по условию Фано).

Подберем коды для оставшихся букв так, чтобы они были минимальными.

Можно подумать, что такой вариант подойдет:

![image](/other/image-4-2.png)

Его длина состовляет 13 двоичных символов.

**Но это неправильно!** 

По условию у нас кодируются буквы: *А, Б, Г, И, М, Р, Я*, а по этому решнию мы не сможем закодировать букву **Р**, а это значит, что верное решение будет:

![image](/other/image-4-3.png)

При таком раскаладе минимальной длиной двоичного сообщения будет:

М(3) + А(3) + Г(3) + И(2) + Я(3)

3 + 3 + 3 + 2 + 3 = 14

**Ответ: 14**.


К сожелению данное задание не решаеться программно (по крайней мере такое решение еще не придумали). Но само задание не очень сложно, самое главное - это очень внимательно читать условие и правильно понимать как работает условие Фано.
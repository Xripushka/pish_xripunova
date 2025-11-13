#1задача
data = "Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия"
students=data.split("; ")
for student in students:
    student_data=student.split(", ")
    name=student_data[0]
    age=student_data[1]
    facultet=student_data[2]
    
    print("Имя:", name)
    print("Возраст:", age)
    print("Факульттет:", facultet)

#2задача
text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"
mails=text.split(': ')[1].split(', ')
print("|".join(mails))

#3задача
sentence = "Python is a powerful and easy-to-learn programming language."
words=sentence.split(' ')
print("Количество слов:", len(words))

#4задача
s = "aaabbbcccaaadddd"
#нет решения

#5задача
import re
text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."
number=re.findall(r'\d+',text)
print(number)

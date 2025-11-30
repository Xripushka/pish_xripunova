import argparse

#словарь с названиями месяцев для красивого вывода
MONTH_NAMES = {
    1: "январь",
    2: "февраль", 
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}
def years_stats(line_datas):
    "Вычисляет статистику температуры за весь год"
    if not line_datas:
        print("Нет данных для обработки")
        return None
    
    #инициализируем переменные для подсчета статистики
    temp_sum=0
    temp_count=0
    temp_min=None
    temp_max=None

    #обрабатывает каждую строку данных
    for line_data in line_datas:
        try:
            line_temp=int(line_data[5]) #температура в 6м элементе (отсчет с 0)
            temp_sum += line_temp
            temp_count += 1
            #обновляем макс и мин температуры
            if temp_min is None or line_temp<temp_min:
                temp_min=line_temp
            if temp_max is None or line_temp>temp_max:
                temp_max=line_temp
        except (ValueError, IndexError):
            continue #пропускаем строки с ошибками
    
    #вычисляем среднюю температуру
    temp_middle=temp_sum / temp_count

    return {
        "middle": temp_middle,
        "min": temp_min,
        "max": temp_max,
        "count": temp_count
    }

def month_stats(line_datas, month):
    "Вычисляет статистику температуры за конкретный месяц"
    if not line_datas:
        print("Нет данных для обработки")
        return None
    
    temp_sum = 0
    temp_count = 0
    temp_min = None
    temp_max = None

    #обрабатываем данные за указанный месяц
    for line_data in line_datas:
        try:
            data_month = int(line_data[1]) #месяц во 2м элементе (отсче с 0)
            if data_month == month:
                line_temp = int(line_data[5])
                
                temp_sum += line_temp
                temp_count += 1
                #обновляем макс и мин температуры
                if temp_min is None or line_temp < temp_min:
                    temp_min = line_temp
                if temp_max is None or line_temp > temp_max:
                    temp_max = line_temp
        except (IndexError, ValueError):
            continue         
    
    #если нет данных за указанный месяц, то возвращаем None
    if temp_count==0:
        return None
    
    #средняя температура за год
    temp_middle = temp_sum / temp_count

    return {
        "middle": temp_middle,
        "min": temp_min,
        "max": temp_max,
        "count": temp_count
    }
def all_months_stats(line_datas):
    "Вычисляет статистику температуры по всем месяцам отдельно"
    months_data = {}
    #собираем статистику для каждого месяца от 1 до 12
    for month in range(1, 13):
        stats = month_stats(line_datas, month)
        if stats: #если есть данные, то добавляем
            months_data[month] = stats
    return months_data

#добавляем агрументы командной строки
parser = argparse.ArgumentParser(
    description="Приложение для вычисления статистики температуры из CSV-файла."
)

parser.add_argument(
    "-f",
    "--file",
    help="Входной CSV-файл",
    required=True
)

parser.add_argument(
    "-m",
    "--month",
    type=int,
    help="Номер месяца (1..12) для вывода статистики только по нему",
    required=False
)

args = parser.parse_args()

#используем переданное имя файла
filename=args.file

#чтение файла и проверка на ошибки
line_datas=[] #создали список для хранения данных
try:    
    with open(filename, "r") as file:
        lines=file.readlines() #читаем все строки файла
        i=0
        for line in lines:
            i+=1
            line_data=line.strip().split(";") 
            if len(line_data)>=6: #проверяем, что в строке 6 элементов
                line_datas.append(line_data) #сохраняем данные для статистики
                try:
                    year=line_data[0]
                    month=line_data[1]
                    day=line_data[2]
                    min_=line_data[3]
                    hour=line_data[4]
                    temp=line_data[5]
                    (int(year), int(month), int(day), int(min_), int(hour), int(temp))
                except:
                    print ("Нашел ошибку в строке N", i)
            else:
                print("Нашел ошибку в строке N", i, "- недостаточно данных")
            
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден в текущей директории.")
    exit()
     
if args.month:
    # Если указан месяц в аргументах командной строки
    if 1<= args.month<=12:
        stats=month_stats(line_datas, args.month)
        if stats:
            print(f"\n--==Статистика температуры за {MONTH_NAMES[args.month]}==--")
            print(f"Средняя температура: {stats['middle']:.2f}°C")
            print(f"Минимальная температура: {stats['min']:}°C") 
            print(f"Максимальная температура: {stats['max']:}°C")
            print(f"Количество измерений: {stats['count']}")
        else:
            print(f"Нет данных для месяца {args.month}")      
    else:
        print("Ошибка: номер месяца от 1 до 12")
else:
    #если месяц не указан в аргументах командной строки, то спрашиваем у пользователя
    print("Выберите тип статистики:")
    print("1 - Статистика за весь год")
    print("2 - Статистика по всем месяцам")
            
    choice = input("Введите номер выбора (1 или 2): ").strip()
    
    if choice =="1":
    # Статистика за год
        year_stat = years_stats(line_datas)
        if year_stat:
            print(f"\n--==СТАТИСТИКА ЗА ВЕСЬ ГОД==--:")
            print(f"  Средняя температура: {year_stat['middle']:.2f}°C")
            print(f"  Минимальная температура: {year_stat['min']}°C")
            print(f"  Максимальная температура: {year_stat['max']}°C")
            print(f"  Всего измерений: {year_stat['count']}")
        else:
            print("Нет данных для расчета статистики за год")
        
    elif choice == "2":
    # Статистика по месяцам
        print(f"\n--==СТАТИСТИКА ПО МЕСЯЦАМ==--:")
        months_stat = all_months_stats(line_datas)
        if month_stats:
            for month in sorted(months_stat.keys()):
                stats = months_stat[month]
                print(f"  {MONTH_NAMES[month]}: средняя {stats['middle']:.2f}°C, мин {stats['min']:}°C, макс {stats['max']:f}°C, измерений: {stats['count']}")
        else:
            print("Нет данных для расчета статистики по месяцам")
    else:
        print("Неверный выбор. Должно быть 1 или 2.")
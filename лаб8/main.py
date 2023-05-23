import csv
from datetime import datetime
import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)
#date = '6 Апрель 2017 14:00'
date = input("Введите дату\n")

date = datetime.strptime(date, '%d %B %Y %H:%M')

with open("2 - 2.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    header = next(file_reader)
    
    end_index = header.index('Завершено')
    status_index = header.index('Состояние')
    
    try:
        score_index = header.index('Оценка/10,00')
        ratio = 1
    except ValueError:
        score_index = header.index('Оценка/100,00')
        ratio = 10
    
    succes_count = 0
    eight_to_ten_count = 0
    for row in file_reader:
        if(row[status_index] == 'Завершено'):
            succes_count += 1
            end_date = datetime.strptime(row[end_index], '%d %B %Y %H:%M')
            if(int(row[score_index].split(',')[0]) >= 8 * ratio and date < end_date):
                eight_to_ten_count += 1
                
    print("Общее число завершённых работ: " + str(succes_count))
    print("Число работ, завершённых после заданной даты, с оценкой 8-10: " + str(eight_to_ten_count))
    print("Процентное соотношение: " + str(eight_to_ten_count / succes_count * 100) + "%")
            
            

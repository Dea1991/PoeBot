import os
import datetime


class GetTime:
    time_now = str(datetime.datetime.now())
    year = time_now[0:4]
    day = time_now[8:10]
    month = time_now[5:7]
    hour = time_now[11:13]
    minutes = time_now[14:16]
    sec = time_now[17:19]


year = GetTime.year
day = GetTime.day
month = GetTime.month
hour = GetTime.hour
minutes = GetTime.minutes
sec = GetTime.sec
way_new = 'C:/HistoryPoe/'
name_txt = way_new + day + '.' + month + '(' + hour + '.' + minutes + '.' + sec + ')' + '.txt'
# new_txt = open(name_txt, mode='w')

# нужно написать часть кода для копирования лога и создание нового

trade_text_ru = 'Здравствуйте, хочу купить у вас'
trade_text_en = 'Hi, I would like to buy your'
data = year + '/' + month + '/' + day
minutes_check = int(minutes) - 61
log_old = 'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt' # я тут поменял на клиент1

# это кусок поиска лога по дате
#    if split_line[0] == data:
#        if int(split_line[1][0:2]) >= int(hour) - 2:
#            if int(split_line[1][3:5]) >= minutes_check:

def read_lines_from_big_file(path):
    with open(path, encoding='utf-8') as fp:
        for line in fp:
            parts = line.split()
            yield parts


party_member = 0

for split_line in read_lines_from_big_file(log_old):
    if trade_text_ru in " ".join(split_line) or trade_text_en in " ".join(split_line):
        with open('trade_list.txt', "r", encoding='utf-8') as trade_open1:
            trade_id1 = split_line[2]
            trade_id2 = split_line[3]
            trade_read1 = trade_open1.read()
            if trade_id1 in trade_read1 and trade_id2 in trade_read1:
                print("-")
                continue
            else:
                with open('trade_list.txt', "a", encoding='utf-8') as trade_add1:
                    trade_add1.write(str(split_line) + '\n')

                # функция добавить в пати
                print("найден новый трейд")

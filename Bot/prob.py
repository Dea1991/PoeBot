import os
import datetime


time_now = str(datetime.datetime.now())
year = time_now[0:4]
day = time_now[8:10]
month = time_now[5:7]
hour = time_now[11:13]
minutes = time_now[14:16]
sec = time_now[17:19]
way_new = 'C:/HistoryPoe/'
name_txt = way_new + day + '.' + month + '(' + hour + '.' + minutes + '.' + sec + ')' + '.txt'
# new_txt = open(name_txt, mode='w')
trade_thx_ru = ['Здравствуйте,', 'хочу', 'купить', 'у', 'вас']
data = year + '/' + month + '/' + day
minutes_check = int(minutes) - 61
log_old = 'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt'

# with open('trade_list.txt', "a", encoding='utf-8') as trade_add1:
def read_lines_from_big_file(path):
    with open(path, encoding='utf-8') as fp:
        for line in fp:
            parts = line.split()
            yield parts


for split_line in read_lines_from_big_file(log_old):
    if split_line[0] == data:
        if int(split_line[1][0:2]) >= int(hour) - 2:
            if int(split_line[1][3:5]) >= minutes_check:
                if split_line[10:15] == trade_thx_ru:
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





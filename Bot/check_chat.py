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
#new_txt = open(name_txt, mode='w')

log_old = 'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt'


def read_lines_from_big_file(path):
    with open(path, encoding='utf-8') as fp:
        for line in fp:
            parts = line.split()
            yield parts


count = 0
data = year + '/' + month + '/' + day

for split_line in read_lines_from_big_file(log_old):
    count += 1
    print(split_line)
    if split_line[0] == data:
        print('+')



#print(q)
# a = open(x, mode='w')


# read = x.read()
# os.remove(path)
# print(len(read))

import os
import datetime

t = str(datetime.datetime.now())
x = t[8:10] + 'x' + t[5:7] + ';' + t[11:13] + 'x' + t[14:16] + 'x' + t[17:19] + '.txt'
x = 'C:/History/' + x
print(x)
path_old = 'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt'

z = open(path_old)
q = z.readlines(353)
print(q)
# a = open(x, mode='w')


# read = x.read()
# os.remove(path)
# print(len(read))

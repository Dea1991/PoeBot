path = 'C:/HistoryPoe/03.10(23.26.43).txt'
count = 0
nick = 'Здравствуйте,'
price1 = 'за'
coordinates1 = '(секция'



def read_lines_from_big_file(path):
    with open(path, encoding='utf-8') as fp:
        for line in fp:
            parts = line.split()
            yield parts


for split_line in read_lines_from_big_file(path): # nick
    for i in split_line:
        count += 1
        if nick in i:
            count = count - 2
            nick_trade = split_line[count][1:-3]
            print('Nick: ', nick_trade)

count = 0
txt = 0
y = "'в',"

for split_line in read_lines_from_big_file(path): # price
    for i in split_line:
        if price1 in i:
            count = count + 1
            price_trade = split_line[count]
            while txt != 1:
                count += 1
                price_trade = price_trade[1:-2] + ' ' + split_line[count][1:-2]
                if split_line[count] == y:
                    txt = 1
                    break
                print('Price: ', price_trade)
        else:
            count += 1

count = 0
txt = 0
z = "'позиция:',"

for split_line in read_lines_from_big_file(path): # coordinates
    for i in split_line:
        if coordinates1 in i:
            g = 0
            count = count + 1
            coordinates_trade = split_line[count]
            while txt != 1:
                count += 1
                n = -1
                g += 1
                coordinates_trade = split_line[count]
                if g == 1:
                    coordinates_trade = coordinates_trade[1:-1]
                print(len(split_line[count]), split_line[count])
                if len(split_line[count]) <= 6:
                    n = -1
                if g > 1:
                    coordinates_trade = coordinates_trade + ' ' + split_line[count][1:n]

                print(coordinates_trade)
                if split_line[count] == z:
                    txt = 1
                    print('coordin ', coordinates_trade)
                    break

        else:
            count += 1








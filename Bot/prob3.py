n = 0

class Trade:
    nick = None
    price = None
    item = None
    section = None
    x = None
    y = None
    tab = None
    txt = None

    def __init__(self, count, trade_txt):
        self.count = count
        self.trade_txt = trade_txt
        global n
        n += 1

log_old = 'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client2.txt'


def read_lines_from_big_file(path):
    with open(path, encoding='utf-8') as fp:
        for line in fp:
            parts = line.split()
            yield parts


for split_line in read_lines_from_big_file(log_old):
    Trade.txt = split_line.copy()

txt = Trade.txt


class TradeParsingList:
    def __init__(self):
        pass

    def return_nick(self):
        global txt, nick
        count = 0
        word1 = 'Здравствуйте,'
        for i in txt:
            count += 1
            if word1 in i:
                count = count - 2
                nick = txt[count][0:-2]
                print('Nick: ', nick)
        return nick

    def return_price(self):
        global txt
        count = 0
        word1 = 'за'
        word2 = 'в'
        word3 = 'лиге'
        price = ''
        for i in txt:
            count += 1
            if word1 in i:
                break
        for j in range(0, 5):
            if txt[count + j] != word2:
                price = price + txt[count + j] + " "
            elif txt[count + j] == word2 and txt[count + j + 1] == word3:
                break
        print('Price: ', price)
        return price

    def return_item(self):
        global txt
        count = 0
        item = ''
        word1 = 'вас'
        word2 = 'за'
        for i in txt:
            count += 1
            if word1 in i:
                break
        for j in range(0, 5):
            if txt[count + j] != word2:
                item = item + txt[count + j] + " "
            elif txt[count + j] == word2:
                break
        print('Item: ', item)
        return item

    def return_tab(self):
        global txt
        count = 0
        tab = ''
        word1 = '(секция'
        word2 = 'позиция:'
        for i in txt:
            count += 1
            if word1 in i:
                break
        for j in range(0, 5):
            if txt[count + j] != word2:
                tab = tab + txt[count + j] + " "
            elif txt[count + j] == word2:
                break
        tab = tab[0:-2]
        print('Tab: ', tab)
        return tab

    def return_x(self):
        global txt
        count = 0
        x = ''
        word1 = 'позиция:'
        word2 = 'столбец,'
        for i in txt:
            count += 1
            if word1 in i:
                break
        x = txt[count]
        print('x: ', x)
        return x

    def return_y(self):
        global txt
        count = 0
        y = ''
        word1 = 'позиция:'
        word2 = 'столбец'
        for i in txt:
            count += 1
            if word2 in i:
                y = txt[count]
        print('y: ', y)
        return y














count_trade = 1
name_trade = 'trade' + str(count_trade) + '.txt'


with open('trade_list.txt', "r", encoding='utf-8') as trade_open1:
    trade_read1 = trade_open1.read()
    with open(name_trade, "w", encoding='utf-8') as trade_now_open:
        trade_now_open.write(str(split_line) + '\n')

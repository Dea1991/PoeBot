print(trade_id1, trade_id2)
                        print(type(trade_id1))
                        print(trade_read1)
                        print(type(trade_read1))
                        if trade_id1 in trade_read1 and trade_id2 in trade_read1:
                            print("+")
                        else:
                            print("-")
                            with open('trade_list.txt', "a", encoding='utf-8') as trade_add1:
                                trade_add1.write(str(split_line) + '\n')
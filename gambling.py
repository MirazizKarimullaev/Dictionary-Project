def addict(quarters,one,two,three):
    money = quarters
    play = 0
    one_win = one
    two_win = two
    three_win = three
    slot = 1 #we could make this an input to decide what slot she starts at
    while True:
        if slot == 1 and money > 0:
            money = money - 1
            one_win +=1
            win = one_win % 35
            if win == 0:
                money +=30 
            play +=1
            slot = 2
        print(money)
        if slot == 2 and money > 0:
            money = money - 1
            two_win +=1
            win = two_win % 100
            if win == 0:
                money +=60
            play +=1
            slot = 3
        print(money)
        if slot == 3 and money > 0:
            money = money - 1
            three_win +=1
            win = three_win % 10
            if win == 0:
                money +=9 
            play +=1
            slot = 1
        print(money)
        if money == 0:
            print(f"Martha plays {play} times before going broke")
            break
addict(1,34,99,9)
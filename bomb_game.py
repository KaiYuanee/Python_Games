import random
import os
import time
print('歡迎遊玩「炸彈遊戲」!')
time.sleep(1)
while True:
    try:
        option = int(input('請選擇炸彈設定模式或查看遊戲規則(輸入0為遊戲規則說明、1為開始遊戲、2為離開遊戲):'))
        if option == 0:
            print('正在進入遊戲規則說明介面...')
            time.sleep(1)
            os.system('cls')
            print('遊戲規則說明如下:')
            print('本遊戲可遊玩人數為1人(含)以上。')
            print('遊戲開始前，由系統或一位玩家從1~1000(含1和1000)之中的一個自然數作為炸彈。')
            print('若為玩家設定炸彈，該玩家不能讓其他玩家得知該數字，且不能進行接下來的遊戲。')
            print('遊戲開始時，玩家們輪流輸入數字。每輸入一個數，系統會將範圍縮小。重複上述動作直至炸彈被碰到(碰觸炸彈的條件:玩家輸入的數字為炸彈)。')
            print('碰到炸彈的玩家為輸家，並且沒有贏家。')
            print('當範圍縮小至只剩下炸彈，則所有人皆為贏家。')
            print()
            back = input('按下[enter]鍵跳出遊戲規則說明介面')
            print('正在回到輸入模式介面...')
            time.sleep(1)
            os.system('cls')
        elif option == 1:
            while True:
                try:
                    setway = input('請輸入炸彈設定模式(0為自動、1為手動、exit為跳出遊戲):')
                    if (int(setway)==0)or(int(setway)==1):
                        if int(setway) == 0:
                            boom = random.randint(1, 1000)
                            print('炸彈自動設置完畢')
                            time.sleep(1)
                        elif int(setway) == 1:
                            boom = int(input('請輸入一個整數作為炸彈，其範圍介於1~1000(含1和1000):'))
                            if 1 <= boom <= 1000:
                                print('炸彈手動設置完畢')
                                time.sleep(1)
                            else:
                                print('錯誤:輸入的數字超出範圍，請重新輸入!')
                                time.sleep(1)
                        os.system('cls')
                        print('遊戲開始')
                        time.sleep(1)
                        min, max = 1, 1000
                        while True:
                            try:
                                n = -1
                                while (n != boom)and(min != max):
                                    n = int(input(f'請輸入介於{min}~{max}之間的整數(含{min}和{max}):'))
                                    if (n != boom)and(min != max):
                                        if min <= n <= max:
                                            if n < boom:
                                                min = n+1
                                            else:
                                                max = n-1
                                            if min != max:
                                                print('此數為安全數字，輪到下一位玩家')
                                                time.sleep(1)
                                        else:
                                            print('錯誤:輸入的數字超出範圍，請該玩家重新輸入數字!')
                                            time.sleep(1)
                                        print()
                                if (min == max):
                                    print(f'恭喜所有玩家，沒有人碰到炸彈!(炸彈是{boom})')
                                else:
                                    print(f'{boom}是炸彈，你輸了!')
                                time.sleep(1)
                                print('遊戲結束')
                                time.sleep(2)
                                os.system('cls')
                                break
                            except:
                                print('錯誤:輸入含有非法字元，請重新輸入!')
                    else:
                        print('錯誤:輸入的數字超出範圍，請重新輸入!')
                except:
                    if setway == 'exit':
                        print('正在回到選擇功能介面...')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print('錯誤:輸入含有非法字元，請重新輸入')
                        time.sleep(1)
        elif option == 2:
            print('感謝你的使用!正在離開系統...')
            time.sleep(1)
            os.system('cls')
            break
        else:
            print('錯誤:輸入的數字超出範圍，請該玩家重新輸入數字!')
            time.sleep(1)
    except:
        print('錯誤:輸入含有非法字元，請重新輸入!')
        time.sleep(1)

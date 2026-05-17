#スイカ割りゲームを作ろう. 
import random
import math

BOARD_SIZE = 5 #わけのわからない数字(マジックナンバー)を避けるために，名前を付ける

#ver.1
#suika_x = random.randrange(0,BOARD_SIZE)
#suika_y = random.randrange(0,BOARD_SIZE)

#player_x = random.randrange(0,BOARD_SIZE)
#player_y = random.randrange(0,BOARD_SIZE)

#ver.2 タプルにすることで簡単にする．
#suika_pos =(random.randrange(0,BOARD_SIZE),random.randrange(0,BOARD_SIZE))
#player_pos = (random.randrange(0,BOARD_SIZE),random.randrange(0,BOARD_SIZE))

#ver.3 関数を定義することで，同じ作業を簡単にできる．
def generate_position(size):
    x = random.randrange(0,size)
    y = random.randrange(0,size)
    return (x,y)

def calc_distance(pos1,pos2):
    return math.sqrt((pos1[0] - pos2[0])**2+(pos1[1] -pos2[1])**2)

def move_position(direction,pos):
    current_x, current_y = pos
    if direction == "n":
        current_y += -1
    elif direction == "s":
        current_y += 1
    elif direction == "w":
        current_x += -1
    elif direction == "e":
        current_x += 1
    else:
        print("もう一度入力してください．")

    current_x = max(0,min(current_x, BOARD_SIZE-1))
    current_y = max(0,min(current_y, BOARD_SIZE-1))
    return (current_x, current_y)

def suika_wari():
    suika_pos = generate_position(BOARD_SIZE)
    player_pos = generate_position(BOARD_SIZE)
    
    while suika_pos == player_pos:
        player_pos = generate_position(BOARD_SIZE)
        
    while suika_pos != player_pos:
        #距離を表示
        print(f"スイカまでの距離{calc_distance(suika_pos,player_pos)}")
        #入力に応じてプレーヤーを移動
        c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動：")
        player_pos = move_position(c,player_pos)
    print("スイカを割れました!")

suika_wari()

#主となる関数suika_wari()と，主となる関数が利用する補助的な関数generate_position()，calc_distance()， move_position() を組み合わせて全体を構成する手法は，プログラムの開発でもっとも基礎的で重要なテクニックである．
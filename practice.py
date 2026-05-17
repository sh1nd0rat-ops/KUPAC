#スイカ割りゲームを作ろう. ]
import random
suika_x = random.randrange(0,5)
suika_y = random.randrange(0,5)

player_x = random.randrange(0,5)
player_y = random.randrange(0,5)

while suika_x != player_x or suika_y != player_y:
    distance = {(player_x - player_y)^2+(player_y -player_y)^2}^{1/2}
    print(distance)
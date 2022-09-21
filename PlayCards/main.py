from DumbPlayer import DumbPlayer
from Game import Game
from Player import Player
from SmartPlayer import Smart_Player

# 我們有4個玩家。
John = Smart_Player('John', 0.65)
Jenny = DumbPlayer('Jenny')
Jan = Smart_Player('Jan', 0.25)
Jones = Player('Jones')

# 紀錄大家的勝場數。
winner_list = [0, 0, 0, 0]

# 這是一個玩1000場比賽的主程式。
for i in range(1000):
    g = Game(John, Jenny, Jan, Jones)
    g.runThirteenRounds() 
    if John in g.match_winner : 
        winner_list[0] += 1 
    if Jenny in g.match_winner: 
        winner_list[1] += 1 
    if Jan in g.match_winner: 
        winner_list[2] += 1 
    if Jones in g.match_winner: 
        winner_list[3] += 1 

# 把大家的勝場數，印在電腦上。
# Smart_Player 完全實力輾壓，勝率超過90%。
print('John, Jenny, Jan, Jones')
print(winner_list)
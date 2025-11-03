import random
from collections import Counter
import plane

def lotto_draw():
    balls = set(random.sample(range(1, 41), 6))
    bonus = random.choice([n for n in range(1, 41) if n not in balls])
    balls.add(bonus)
    return balls, bonus

def random_tickets(count):
    tix = []
    while len(tix) < count:
        line = set(random.sample(range(1, 41), 6))
        if line not in tix:
            tix.append(line)
    return tix


tickets = [plane.fano(1,8), 
           plane.fano(9,17), 
           plane.fano(18,31), 
           plane.fano(32,40)]

tickets_alt = [plane.fano(1,14), plane.fano(15,28), plane.fano(29,42)]

tix_alt_alt = [[[1, 2, 3, 4, 9, 10], [1, 2, 7, 8, 11, 12], [1, 2, 5, 6, 13, 14], [3, 4, 5, 6, 11, 12],
                [3, 4, 7, 8, 13, 14], [5, 6, 7, 8, 9, 10], [9, 10, 11, 12, 13, 14]], 
                [[15, 16, 17, 18, 23, 24], [15, 16, 21, 22, 25, 26], [15, 16, 19, 20, 27, 28], [17, 18, 19, 20, 25, 26], 
                [17, 18, 21, 22, 27, 28], [19, 20, 21, 22, 23, 24], [23, 24, 25, 26, 27, 28]], 
                [[29, 30, 31, 32, 37, 38], [29, 30, 35, 36, 39, 40], [29, 30, 33, 34, 35, 36], [31, 32, 33, 34, 39, 40], 
                [31, 32, 35, 36, 39, 40], [33, 34, 35, 36, 37, 38], [35, 36, 37, 38, 39, 40]]]

match_counts = Counter()
rand_counts = Counter()
total_draws = 20000
wins, rand_wins = 0, 0
total_balls, rand_total_balls = {}, {}

draw_max = 0
best_draw_ticket = []
best_draw_counter = 0
best_draw_numbers = []
best_draw_bonus = False
best_draw_bb_number = None

rand_max = 0
best_rand_draw_ticket = []
best_rand_draw_counter = 0
best_rand_draw_numbers = []
best_rand_draw_bonus = False
best_rand_bb_number = None

for i in range(total_draws):
    draw, bonus = lotto_draw()
    temp_tb, rand_tb = [], []
    rand_control = random_tickets(16)

    for rt in rand_control:
        matches = len(set(rt) & draw)
        bb = bonus in rt
        if matches >= 3:
            rand_counts[matches] += 1
            rand_tb.append([matches, bb])
            if matches > rand_max:
                best_rand_draw_ticket = rt
                best_rand_draw_numbers = draw
                rand_max = matches
                best_rand_draw_counter = i+1
                if bb:
                    best_rand_draw_bonus = True
                    best_rand_bb_number = bonus
                else:
                    best_rand_draw_bonus = False
                    best_rand_bb_number = None


    for ticket in tix_alt_alt:
        for line in ticket:
            matches = len(set(line) & draw)
            bb = bonus in line
            if matches >= 3:
                match_counts[matches] += 1
                temp_tb.append([matches, bb])
                if matches > draw_max:
                    best_draw_ticket = line
                    best_draw_numbers = draw
                    draw_max = matches
                    best_draw_counter = i+1
                    if bb:
                        best_draw_bonus = True
                        best_draw_bb_number = bonus
                    else:
                        best_draw_bonus = False
                        best_draw_bb_number = None

    if temp_tb:
        wins += 1
        total_balls[i+1] = temp_tb
    
    if rand_tb:
        rand_wins += 1
        rand_total_balls[i+1] = rand_tb

# for t in tickets_alt:
#     for i in t:
#         print(i)  
    

print(f"\nTotal wins over {total_draws} tickets: {wins}, {round(wins/total_draws*100,1)}%")
print(f"Largest win: {max(total_balls.items(), key=lambda x: x[1])}, draw: {best_draw_numbers}, ticket: {best_draw_ticket}, bonus ball: {best_draw_bonus}, ({best_draw_bb_number})")
print(f"Match counts total: {match_counts}")
print()
print(f"Random wins: {rand_wins}, {round(rand_wins/total_draws*100, 2)}%")
print(f"Largest random win: {max(rand_total_balls.items(), key=lambda x: x[1])}, draw: {best_rand_draw_numbers}, ticket: {best_rand_draw_ticket}, bonus ball: {best_rand_draw_bonus}, ({best_rand_bb_number})")
print(f"Random counts total: {rand_counts}")
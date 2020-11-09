
# HackerRank AI
# Statistics and Machine Learning
# Markov's Snakes And Ladders
# Problem code: https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem

import random

n_games = 5000  # number of simulated games

n = int(input())


def find_move(p, prob):
    i = 1
    while i <= len(prob):
        if (p > sum(prob[:i - 1])) & (p <= sum(prob[:i])):
            move = i
            break
        else:
            i += 1
    return move


for i in range(n):
    prob = list(map(float, input().split(',')))
    n_ladders, n_snakes = map(int, input().split(','))
    ladder_pair = input().split()
    ladders = {}
    for ld in ladder_pair:
        head, tail = map(int, ld.split(","))
        ladders[head] = tail

    snake_pair = input().split()
    snakes = {}
    for sn in snake_pair:
        head, tail = map(int, sn.split(","))
        snakes[head] = tail
    # position = 0
    # rolls = 0
    totalCnt = 0
    totalRolls = 0
    # start the game
    for _ in range(n_games):
        position = 1
        num_roll = 0
        while num_roll < 1000:
            p = random.uniform(0, 1)
            move = find_move(p, prob)
            if position + move <= 100:
                position += move
                if position in ladders:
                    position = ladders[position]
                elif position in snakes:
                    position = snakes[position]
            num_roll += 1
            if position == 100:
                totalCnt += 1
                totalRolls += num_roll
                break

    print(round(totalRolls / totalCnt))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:09:12 2018

@author: kage
"""
import random

def hangman():
    words = ("cat", "dog", "rat", "camel", "bear", "panda")
    word = words[random.randint(0, len(words))]
    wrong = 0
    stages = ["",
              "________         ",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね : "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("\nあなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("\nあなたの負け！正解は {}。".format(word))

hangman()

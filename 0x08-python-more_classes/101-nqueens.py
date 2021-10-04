#!/usr/bin/python3
"""Dont kill the Queen"""
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
        """Board Size"""
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    """Board"""
    box = []

    """Queens"""
    for q in range(n):
        box.append([q, None])

    def queen_checker(num):
        for q in range(n):
            if num == box[q][1]:
                return True
        return False

    """2 Queens a row"""

    def wrong_way(word, num):
        if queen_checker(num):
            return False
        q = 0
        while q < word:
            if abs(box[q][1] - num) == abs(q - word):
                return False
            q += 1
        return True

    """Clear"""

    def erase_way(word):
        for q in range(word, n):
            box[q][1] = None

    """Base condition"""

    def backtrace(word):
        for num in range(n):
            erase_way(word)
            if wrong_way(word, num):
                box[word][1] = num
                if(word == n - 1):
                    print(box)
                else:
                    backtrace(word + 1)

    backtrace(0)

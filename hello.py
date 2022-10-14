'''
Created on 2022/10/14

@author: t20cs012
'''
from quick_sort import quick_sort
from rpc import Player, Judge


if __name__ == '__main__':
    # クイックソートテスト
    arr = [4,6,89,2,1]
    arr = quick_sort(arr)
    print(arr)
    
    judge = Judge()
    playerA = Player('山本')
    playerB = Player('鈴木')
    judge.start_janken(playerA, playerB)


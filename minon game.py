def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    countS = 0
    for i in range(0,n):
        if string[i] not in vowels:
            countS += n-i

    countK = 0
    for i in range(0, n):
        if string[i] in vowels:
            countK += n-i
    
    if countK > countS:
        print(f"Kevin {countK}")
    elif countK < countS:
        print(f"Stuart {countS}")
    else:
        print("Draw")
numbers = [1,2,3,4,5,6,7,8,9,"_"]
def game_status_check(l):
    k = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    no_of_blank_boxes=0
    for i in range(3):
        for j in range(3):
            if(l[i][j] == 'X'):
                k[i][0] += 1
            elif(l[i][j] == 'O'):
                k[i][1] += 1
            if(l[j][i] == 'X'):
                k[i+3][0] += 1
            elif(l[j][i] == 'O'):
                k[i+3][1]+=1
            if(l[i][j] in numbers):
                no_of_blank_boxes += 1
        if(l[i][i] == 'X'):
            k[6][0] += 1
        elif(l[i][i] == 'O'):
            k[6][1] += 1
        if(l[i][2-i] == 'X'):
            k[7][0] += 1
        elif(l[i][2-i] == 'O'):
            k[7][1] += 1

    print(k)
    for i in range(8):
        if(k[i][0] == 3):
            return ["Player-1 is the winner", i]
        elif(k[i][1] == 3):
            return ["Player-2 is the winner", i]
    
    if(no_of_blank_boxes != 0):
        return ["Can continue",-1]
    else:
        return ["Draw",-1]

def findPath(board,path,i,j,n):
    if i == n-1 and j == n-1:
        path[i][j] = 1
        return 1
    
    if board[i][j] == 1:
        if findPath(board,path,i,j+1,len(board)) == 1:
            path[i][j] = 1
            return 1
            
        if findPath(board,path,i+1,j,len(board)) == 1:
            path[i][j] = 1
            return 1  

    path[i][j] = 0
    
    return 0

board = [
    [1,1,1,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,1,1,1],
]

path = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]



findPath(board,path,0,0,len(board))
count = 0

for i in range(len(board)):
    for j in range(len(board)):
        if path[i][j]:
            count+=1
            print('[x]', end='')
            # if path[i][j] > path[i][j-1]:
            #     print('[x]', end='')
            # else:
            #     print('[x]', end='')
        else:
            print('[ ]', end='')
    print()

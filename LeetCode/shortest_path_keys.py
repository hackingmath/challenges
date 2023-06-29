"""https://leetcode.com/problems/shortest-path-to-get-all-keys/
Help from Geeks for Geeks
https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/
June 29, 2023
"""

from collections import deque

dRow,dCol = [-1,0,1,0],[0,1,0,-1]

def make_grid(gridlist):
    output = [s.split() for s in gridlist]
    print(output)
    return output

#print(make_grid(grid))
letters = "abcdefghijklmnopqrstuvwxyz"
UPPERS = [letter.upper() for letter in letters]
def isValid(grid,vis,row,col,visited):

    #print("rows,cols:",rows,cols)
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    # if (vis[row][col]):
    #     return False
    if grid[row][col] == '#': return False
    if grid[row][col] in UPPERS:
        low = grid[row][col].lower()
        if low not in visited:
            print("UP:",grid[row][col])
            return False
    return True

def BFS(grid,vis,row,col):
    q = deque()
    q.append([grid[row][col],(row,col),0,list(),set()])
    vis[row][col] = True

    while q:
        cell,(r,c),moves,visited,myletters = q.popleft()
        #x,y = cell[0],cell[1]
        #print("x,y,grid[x][y]:",x,y,grid[x][y])#,end = ' ')

        for i,spot in enumerate([(r+1,c),(r-1,c),(r,c+1),(r,c-1)]):
            adjx,adjy = spot
            if not isValid(grid,vis,adjx,adjy,myletters):
                continue
            else:
                newcell = grid[adjx][adjy]
                visited.append((adjx,adjy))

                #vis[adjx][adjy] = True
                if newcell in letters:
                    myletters.add(newcell)
                    print("myletters:",myletters)
                    if len(myletters) >= num_keys:
                        print("soln:",moves+1)
                        return
                q.append((newletter, (adjx, adjy), moves + 1, visited, myletters))
                print("(newletter,(adjx,adjy),moves+1,visited,myletters):",
                      (newletter, (adjx, adjy), moves + 1, visited, myletters))
                #print(grid[adjx][adjy])
        #print("vis:",vis)
    print("soln: -1")
    return

def shortestPathAllKeys(grid):
    i = 0;
    j = 0;
    keys = 0;
    m = len(grid);
    n = 0
    for row in grid:  # calculating pre-requisites
        n = len(row)
        j = 0
        for ch in row:
            if ch == '@':
                start = (i, j)
            if ch.islower():
                keys += 1
            j += 1
        i += 1

    que = deque()
    que.append((start, 0))
    vis = {(start, 0)}
    levels = 0

    curr_level = 1  # count
    next_level = 0  # count

    while len(que) > 0:  # travelling in bfs
        pop = que.popleft()
        curr_level -= 1
        if pop[1] == (1 << keys) - 1:
            return levels
        for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            newpo = (dir[0] + pop[0][0], dir[1] + pop[0][1])
            # print(newpo, m ,n)
            if newpo[0] >= 0 and newpo[0] < m and newpo[1] >= 0 and newpo[1] < n:
                ch = grid[newpo[0]][newpo[1]]
                if ch != '#':
                    if ord(ch) >= ord('a') and ord(ch) <= ord('f'):
                        key = pop[1] | (1 << (ord(ch) - ord('a')))
                        if ((newpo), key) not in vis:
                            que.append(((newpo), key))
                            next_level += 1
                            vis.add(((newpo), key))
                    elif ord(ch) >= ord('A') and ord(ch) <= ord('F'):
                        if (pop[1] & (1 << int(ord(ch) - ord('A')))) > 0 and ((newpo), pop[1]) not in vis:
                            que.append(((newpo), pop[1]))
                            next_level += 1
                            vis.add(((newpo), pop[1]))
                    else:
                        if ((newpo), pop[1]) not in vis:
                            que.append(((newpo), pop[1]))
                            next_level += 1
                            vis.add(((newpo), pop[1]))
        if curr_level == 0:
            levels += 1
            curr_level = next_level
            next_level = 0
    return -1

print(shortestPathAllKeys(["@...a",".###A","b.BCc"]))
# if __name__ == '__main__':
#     grid = ["@...a",".###A","b.BCc"]#["@Aa"]#["@.a..","###.#","b.A.B"],#["@..aA","..B#.","....b"]
#     rows, cols = len(grid), len(grid[0])
#     #print("rows,cols:",rows,cols)
#     num_keys = 0
#     for row in grid:
#         for c in row:
#
#             if c in letters:
#                 num_keys += 1
#     #print("num_keys:",num_keys)
#     vis = [[False for i in range(cols)] for i in range(rows)]
#     #visited = set()
#     BFS(grid,vis,0,0)


def mine_filler(n,m,map):

    playGround = [['#' for j in range(m)]for i in range(n)]

    for loc in mine_index_list:

        playGround[loc[0]-1][loc[1]-1]= '*'

    return playGround


def show_matrix(matrix):
    for row in matrix:
        str_row = ''
        for col in row :
            str_row += col + ' '
        print(str_row)        

def calculate_mine_number(n ,m,playGround):
    for i in range(n):
        for j in range(m):
            if playGround[i][j] == '#':
                sum_starts=0 
                #
                try:
                    if playGround[i][j-1]== '*' and not j == 0 : sum_starts += 1 
                except : pass 
                ##
                try:
                    if playGround[i][j+1]== '*' : sum_starts += 1 
                except : pass
                ###
                try:
                    if playGround[i-1][j]== '*' and not i == 0 : sum_starts += 1 
                except : pass
                ####
                try:
                    if playGround[i+1][j]== '*' : sum_starts += 1 
                except : pass
                #5
                try:
                    if playGround[i-1][j-1]== '*' and not i == 0 and not j ==0 : sum_starts += 1 
                except : pass
                #6
                try:
                    if playGround[i-1][j+1]== '*' and not i  == 0 : sum_starts += 1 
                except : pass
                #7
                try:
                    if playGround[i+1][j-1]== '*' and not j == 0 : sum_starts += 1 
                except : pass
                #8
                try:
                    if playGround[i+1][j+1]== '*' : sum_starts += 1 
                except : pass

                playGround[i][j] = str(sum_starts)
    show_matrix(playGround)
n , m = map(int,input().split())
k_numbers = int(input())

mine_index_list =[]
for i in range(k_numbers):
    row , col = map(int,input().split())
    mine_index_list.append([row , col])


playGround= mine_filler(n, m, mine_index_list) 
#show_matrix(playGround)



calculate_mine_number(n ,m,playGround)

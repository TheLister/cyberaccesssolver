from functions import *

# matrix indexes
# '00','01','02','03','04',
# '05','06','07','08','09',
# '10','11','12','13','14',
# '15','16','17','18','19',
# '20','21','22','23','24'

matrix = [
        '55','55','1c','1c','55',
        '1c','55','1c','1c','55',
        'bd','55','e9','bd','1c',
        '55','bd','1c','55','e9',
        'e9','1c','bd','e9','1c'
    ]

mine_v1 = ['55','1c','e9']
mine_v2 = ['bd','55','1c']
mine_v3 = ['e9','e9','1c']

# ALL KNOWN SOLUTIONS

# Solves only Minev1
# SOLUTION 1 21 20
# SOLUTION 1 21 23
# SOLUTION 4 14 12
# SOLUTION 4 24 20
# SOLUTION 4 24 23

# Solves only MineV2
# [0,10,11,21]
# [1,16 15,5]
# [1,16,18,8]
# [1,16,18,3]

# Solves only minev3
# [3,23,20,5]
# [0,20,23,8]
# [0,20,23,3]

#indexes of all matrices in a given column
column0idx = [0,5,10,15,20]
column1idx = [1,6,11,16,21]
column2idx = [2,7,12,17,22]
column3idx = [3,8,13,18,23]
column4idx = [4,9,14,19,24]

mine_v1_step1 = solve_step_1(matrix, mine_v1)

mine_v1_step2 = solve_step_2(matrix, mine_v1_step1, mine_v1)

for m2idx, m2val in enumerate(mine_v1_step2):
    for rowpeer in get_row_peers(matrix, m2val[1]):
        if rowpeer[1] == mine_v1[2]:
          print("MINEV1 SOLUTION " + str(m2val[0]) + " " + str(m2val[1]) + " " + str(rowpeer[0]))
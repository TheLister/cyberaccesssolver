
from functions import *

#define the matrix as an ordered list (should I use dictonary?)
matrix = [
        '55','55','1c','1c','55',
        '1c','55','1c','1c','55',
        'bd','55','e9','bd','1c',
        '55','bd','1c','55','e9',
        'e9','1c','bd','e9','1c'
    ]


#define the Datamine sequences as lists of strings
mine_v1 = ['55','1c','e9']
mine_v2 = ['bd','55','1c']
mine_v3 = ['e9','e9','1c']

# matrix indexes
# '00','01','02','03','04',
# '05','06','07','08','09',
# '10','11','12','13','14',
# '15','16','17','18','19',
# '20','21','22','23','24'


# find all matrix indices where the first string of any of the wanted sequence matches the top row

# add all indices where the first requested sequence is anywhere in the matrix 


# if we are not able to use the first buffer in the best way, then we will revert to wasting the first buffer in order to get the best possible result



column0idx = [0,5,10,15,20]
column1idx = [1,6,11,16,21]
column2idx = [2,7,12,17,22]
column3idx = [3,8,13,18,23]
column4idx = [4,9,14,19,24]

def solve_using_first_buffer(matrix, mine_v1, mine_v2, mine_v3):
    print("solving using first buffer")


def solve_wasting_first_buffer(matrix, mine_v1, mine_v2, mine_v3):
    print("solving wasting first buffer")

def get_row_peers(matrix, matrix_index): #returns indexes of all matrix row members minus the given
    row_peers = []
    if matrix_index >= 0 and matrix_index < 5: #row 0
      row = [0,1,2,3,4]
      row.pop(row.index(matrix_index))
      row_peers = []
      for x in row:
        row_peers.append([x,matrix[x]])
      return row_peers
    if matrix_index >= 5 and matrix_index < 10: #row 1
      row = [5,6,7,8,9]
      row.pop(row.index(matrix_index))
      row_peers = []
      for x in row:
        row_peers.append([x,matrix[x]])
      return row_peers
    if matrix_index >= 10 and matrix_index < 15: #row 2
      row = [10,11,12,13,14]
      row.pop(row.index(matrix_index))
      row_peers = []
      for x in row:
        row_peers.append([x,matrix[x]])
      return row_peers
    if matrix_index >= 15 and matrix_index < 20: #row 3
      row = [15,16,17,18,19]
      row.pop(row.index(matrix_index))
      row_peers = []
      for x in row:
        row_peers.append([x,matrix[x]])
      return row_peers
    if matrix_index >= 20 and matrix_index < 25: #row 4
      row = [20,21,22,23,24]
      row.pop(row.index(matrix_index))
      row_peers = []
      for x in row:
        row_peers.append([x,matrix[x]])
      return row_peers

def solve_step_1(matrix, mine_v1):
  mine_v1_step1 = []
  for xidx, xval in enumerate(matrix[0:5]): #range high must be last + 1
    if xval == mine_v1[0]:
        mine_v1_step1.append(xidx)
  return mine_v1_step1

def solve_step_2(matrix, mine_v1_step1, mine_v1):
    mine_v1_step2 = []
    for m1idx, m1val in enumerate(mine_v1_step1):
        if m1val == 0:
            # print("looking for second mine_v1 string in column " + str(m1val))
            for colidx in column0idx: #column0idx list of matrix indexes for current column
                #colidx is the matrix index for the current column item (0,5,10,15,20)
                if matrix[colidx] == mine_v1[1]:
                    seq1 = []
                    seq1.append(m1val)
                    seq1.append(colidx)
                    #write the sequence to the list of possible solutions
                    mine_v1_step2.append(seq1)
        if m1val == 1:
            # print("looking for second mine_v1 string in column " + str(m1val))
            for colidx in column1idx: #column0idx list of matrix indexes for current column
                #colidx is the matrix index for the current column item (0,5,10,15,20)
                if matrix[colidx] == mine_v1[1]:
                    # print("matrix " + str(colidx) + " matches second mine_v1 item")
                    #build sequence for this solution
                    seq1 = []
                    seq1.append(m1val)
                    seq1.append(colidx)
                    mine_v1_step2.append(seq1)
        if m1val == 2:
            # print("looking for second mine_v1 string in column " + str(m1val))
            for colidx in column2idx: #column0idx list of matrix indexes for current column
                #colidx is the matrix index for the current column item (0,5,10,15,20)
                if matrix[colidx] == mine_v1[1]:
                    # print("matrix " + str(colidx) + " matches second mine_v1 item")
                    #build sequence for this solution
                    seq1 = []
                    seq1.append(m1val)
                    seq1.append(colidx)
                    # print(seq1)
                    #write the sequence to the list of possible solutions
                    mine_v1_step2.append(seq1)
        if m1val == 3:
            # print("looking for second mine_v1 string in column " + str(m1val))
            for colidx in column3idx: #column0idx list of matrix indexes for current column
                #colidx is the matrix index for the current column item (0,5,10,15,20)
                if matrix[colidx] == mine_v1[1]:
                    # print("matrix " + str(colidx) + " matches second mine_v1 item")
                    #build sequence for this solution
                    seq1 = []
                    seq1.append(m1val)
                    seq1.append(colidx)
                    # print(seq1)
                    #write the sequence to the list of possible solutions
                    mine_v1_step2.append(seq1)
        if m1val == 4:
            for colidx in column4idx: #column0idx list of matrix indexes for current column
                #colidx is the matrix index for the current column item (0,5,10,15,20)
                if matrix[colidx] == mine_v1[1]:
                    #build sequence for this solution
                    seq1 = []
                    seq1.append(m1val)
                    seq1.append(colidx)
                    #write the sequence to the list of possible solutions
                    mine_v1_step2.append(seq1)
    return mine_v1_step2



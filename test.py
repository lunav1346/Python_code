score = [3, 3, 3, 1, 2, 3, 3, 1, 3, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 1, 2, 1, 3, 3, 2, 3, 3, 1, 3, 1, 3, 3, 3, 3, 3, 3, 3]
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0

s1 += score[0] + score[8] + score[16] + score[24] + score[32] + score[40]
s2 += score[1] + score[9] + score[17] + score[25] + score[33] + score[41]
s3 += score[2] + score[10] + score[18] + score[26] + score[34] + score[42]
s4 += score[3] + score[11] + score[19] + score[27] + score[35] + score[43]
s5 += score[4] + score[12] + score[20] + score[28] + score[36] + score[44]
s6 += score[5] + score[13] + score[21] + score[29] + score[37] + score[45]
s7 += score[6] + score[14] + score[22] + score[30] + score[38] + score[46]
s8 += score[7] + score[15] + score[23] + score[31] + score[39] + score[47]

print(f'{s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}')
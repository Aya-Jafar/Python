# Finding the longest common substring 
seq1 = 'GATTACCA'
seq2 = 'TAGACCA'
seq3 = 'ATACACC'
# out = ACC
sub = [seq1[i:j] for i in range(len(seq1)) for j in range(i+1,len(seq1)) if len(seq1[i:j])!= 1 ]
print(sub)

common = { i:len(i) for i in sub if i in seq2 and i in seq3 }
print(common)

max_val = max(common, key=common.get)
print(max_val)

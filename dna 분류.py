f = open("DNA.txt", "r")

# s에 DNA 내용 저장
s = f.read()

protein = ""

stop_codons = ['TAA', 'TAG', 'TGA']
Table = {
'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
'GGG': 'G'}

for i in range(len(s)//3):
    tmp = ""

    #tmp에 세 자씩 끊어 저장
    for j in range(3):
        tmp += s[i*3 + j]

    if tmp in Table:
        protein += Table[tmp]

    #만약 stop_codons에 있으면 *추가
    for k in range(3):
        if tmp == stop_codons[k]:
            protein += "*"

f1 = open("Protein.txt", "w")

for i in range(len(protein)//10):
    tmp = ""
    #tmp에 10자씩 저장
    for j in range(10):
        tmp += protein[i*10+j]
    #tmp가 10자가 되면 띄어쓰기
    tmp += " "
    f1.write(tmp)
    #30자가 되면 줄 넘김
    if (i + 1) % 3 == 0:
        f1.write("\n")

f1.close()
f.close()
a = input("kalimat: ")
kata = input("satu buah kata ya dicari: ")
hitung = 0
kalimat = a.lower()
kata_yg_dicari = kalimat.split()

for i in kata_yg_dicari:
    if i==kata:
        hitung +=1
print("Jumlah kata :",hitung)
    




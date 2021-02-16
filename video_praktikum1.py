#Nama :Tiur Septiani
#Nim :71200656
#sumber : https://brainly.co.id/tugas/24235846

''' Ari membeli buah mangga 15 kg dengan harga per kilonya Rp 5.000,00 namun karena pengemasan yang kurang rapi, 
selama banyak buah mangga yang mengalami kerusakan tekstur. 
Terpaksa Ari harus menjual rugi mangga tersebut dengan harga Rp 4.000,00 per kilonya. 
Berapa persen kerugian yang diderita Ari akibat menjual mangga tersebut? 

rumus kerugian: rugi = harga jual - harga beli 
rumus presentase kerugian: presentase rugi = kerugian/harga awal * 100

input:
1.masukan harga beli 
2.masukan harga jual (rugi)

proses:
1.mencari nilai rugi (dengan menggunakan rumus rugi)
2.mencari nilai presentase (dengan menggunakan rumus presentase rugi)

output:
presentase kerugian:
'''
harga_beli = int(input("Masukan Harga Beli: "))
harga_jual =int(input("Masukan Harga Jual: "))

nilai_rugi = harga_jual *15 - harga_beli * 15

print("nilai rugi dalam negatif: ", nilai_rugi)

rumus_presentase =nilai_rugi / (harga_beli * 15) * -100

print("presentase rugi adalah", rumus_presentase,"%")
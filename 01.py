# nama_gaji=dict()
# data = {
#     'Alpro_A':['Rizky', 'Yusak', 'Shalom', 'Tania'],
#     'Alpro_B':['Dedi', 'Karen', 'Yusak', 'Tania'],
#     'Alpro_C':['Richard', 'Rizky', 'Mikael', 'Yusak'],
#     'Alpro_D':['Michelle', 'Tania','Dedi','Karen'],
#     'Jarkom_A':['Rizky', 'Vero'],
#     'Jarkom_B':['Riel','Natanael'],
#     'Jarkom_C':['Yulius','Kevin']
# }
# for matkul in data:
#     for asdos in data[matkul]:
#         if asdos not in nama_gaji:
#             nama_gaji[asdos]=45000 
#         else:
#             nama_gaji[asdos]=nama_gaji[asdos]+45000 
# nama_gajiSort=dict(sorted(nama_gaji.items()))
# print(nama_gajiSort)

def cekKarakter(kalimat):
    kalimat=kalimat.lower()
    huruf=set()
    for karakter in kalimat:
        if karakter.isalpha():
            huruf.add(karakter)
    huruf_huruf=set('abcdefeghijklmnopqrstuvwxyz')
    if huruf== huruf_huruf:
        print('Kalimat tersebut memiliki semua huruf')
    else:
        print('Kalimat tersebut tidak memiliki semua huruf')
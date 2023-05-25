def daftar_tidak_sama(angka1, angka2, batas):
    list_angka1=set()
    list_angka2=set()
    for i in range(angka1, batas, angka1):
            list_angka1.add(i)
    for i in range(angka2, batas ,angka2):
            list_angka2.add(i)
    print(len(list_angka1^list_angka2))
daftar_tidak_sama(7,3,30)

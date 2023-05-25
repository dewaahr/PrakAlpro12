def kata_unik_spesial(kalimat1, kalimat2):
    list_1=kalimat1.split()
    list_2=kalimat2.split()
    new_list=[]
    for kata_1 in list_1:
        if kata_1 in list_2:
            new_list.append(kata_1+kata_1)
        else:
            new_list.append(kata_1)
    for kata_2 in list_2:
        if kata_2 in list_1:
            new_list.append(kata_2+kata_2)
        else:
            new_list.append(kata_2)
    hasil=set(new_list)
    return hasil
# kata_unik_spesial('saya mau makan', 'saya mau mandi')

# n=int(input('angka:'))
# bilangan_inp=set()

# for i in range(n):
#     bil=int(input('input set:'))
#     bilangan_inp.add(bil)

# print(bilangan_inp)
# print(min(bilangan_inp))
# print(max(bilangan_inp))
# print(len(bilangan_inp))

nama_1={'dewa','dewi''diba','doby'}

nama_2={'dewa','sargi','dewi','rangga'}

a=nama_1|nama_2
b=nama_1&nama_2
c=nama_1-nama_2
d=nama_1^nama_2
print(a)
print(b)
print(c)
print(d)

data = [2, 4, 3, 2, 7, 8, 6, 4, 5, 5]
data=set(data)
print(sum(data))


data_d={1:['A','B','D','E','F'],2:['B','D','G'],3:['C','F','G']}
set_datad=list()
for keys in data_d.keys():
    set_datad.append(set(data_d[keys]))
print(set_datad)

hasil=set_datad[0]|set_datad[1]|set_datad[2]

print(hasil)

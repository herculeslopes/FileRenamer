import os
from natsort import natsorted

path = input('PATH: ')
name = input('Name: ')

os.chdir(path)

dir_files = os.listdir()
my_files = []

for file in dir_files:
    if file.startswith(name):
        my_files.append(file)

print()
for f in natsorted(my_files):
    print(f)

print()
print('O Programa a seguir modificará os arquivos acima')
print(f'Preview: {name} 00.cbx')
res = input('Deseja prosseguir? ').strip().upper()[0]

if res == "S":

    for index, cbx in enumerate(natsorted(my_files)):
        print()
        print(f'Index: {index} - File: {cbx}')

        extension = os.path.splitext(f)[1]

        print(f'File Extension: {extension}')
        os.rename(cbx, f'{name} {index + 1:0>2}{extension}')
        print(f'Renamed To: {name} {index + 1:0>2}{extension}')

elif res == "N":

    print('Programa Finalizado.')

else:

    print('Resposta inválida.')
    print('Finalilzando programa.')



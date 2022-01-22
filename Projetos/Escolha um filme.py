import random

lista_filmes = ['Poderoso Chefao', 'Annabelle', 'Midsommar', 'Fight Club', 'Doutor Estranho','Pinguins do Papai','Joker',
'Harry Potter', 'Senhor dos Aneis','Star Wars',]
lista_potter = ['Harry Potter e a Pedra Filosofal', 'Harry Potter e a Camara Secreta', 'Harry Potter e o Prisioneiro de Azkaban', 
'Harry Potter e o Calice de Fogo', 'Harry Potter e a Ordem da Fenix', 'Harry Potter e o Enigma do Principe',
'Harry Potter e as Reliquias da Morte pt. 1', 'Harry Potter e as Reliquias da Morte pt. 2',]
lista_terror = ['Annabelle', 'Annabelle 2: A Criacao do Mal','Annabelle 3: De Volta Para Casa']
lista_anéis = ['O Senhor dos Aneis: A Sociedade do Anel', 'O Senhor dos Aneis: As Duas Torres','O Senhor dos Aneis: O Retorno do Rei']
lista_stars_so_os_bons_kkk = ['Star Wars: Episodio III – A Vinganca dos Sith', 'Star Wars: Os Ultimos Jedi','Star Wars Episodio VI - O Retorno de Jedi'] 

R = random.choice(lista_filmes)

if(R=='Harry Potter'):
    R = random.choice(lista_potter)
if(R=='Annabelle'):
    R = random.choice(lista_terror)
if(R=='Senhor dos Anéis'):
    R = random.choice(lista_anéis)
if(R=='Star Wars'):
    R = random.choice(lista_stars_so_os_bons_kkk)

novo = open('filme', 'w')

novo.write(R)
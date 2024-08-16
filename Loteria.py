from PIL import Image
import random
import numpy as np
import time

def selection_sort(dictionary):
    keys=list(dictionary.keys())
    values=list(dictionary.values())
    
    for i in range(len(keys)):
        min_index=i
        for j in range(i+1,len(keys)):
            if keys[j]<keys[min_index]:
                min_index=j
        keys[i], keys[min_index]=keys[min_index], keys[i]
        values[i], values[min_index]=values[min_index], values[i]
    
    return dict(zip(keys, values))

personajes_loteria={1:'El gallo',2:'El diablo',3:'La dama',4:'El catrin',5:'La sirena',6:'La escalera',7:'El paraguas',8:'La botella',9:'El barril',10:'El arbol',11:'El melon',12:'El valiente',13:'El gorrito',14:'La muerte',15:'La pera',16:'La bandera',17:'El bandolon',18:'El violoncello',19:'La garza',20:'El pajaro',21:'La mano',22:'La bota',23:'La luna',24:'El cotorro',25:'El borracho',26:'El negrito',27:'El corazon',28:'La sandia',29:'El tambor',30:'El camaron',31:'Las jaras',32:'El musico',33:'La araña',34:'El soldado',35:'La estrella',36:'El cazo',37:'El mundo',38:'El apache',39:'El nopal',40:'El alacran',41:'La rosa',42:'La calavera',43:'La campana',44:'El cantarito',45:'El venado',46:'El sol',47:'La corona',48:'La chalupa',49:'El pino',50:'El pescado',51:'La palma',52:'La maceta',53:'El arpa',54:'La rana'}
personajes_loteria=selection_sort(personajes_loteria)

def matriz(personajes_loteria):
    A = np.zeros((4, 4), dtype=object)
    cartas_seleccionadas=set()
    for renglon in range(len(A)):
        for columna in range(len(A[0])):
            while True:
                carta = random.randint(1, 54)
                if carta not in cartas_seleccionadas:
                    cartas_seleccionadas.add(carta)
                    A[renglon][columna] = personajes_loteria[carta]
                    break
    return A

personajes_values=list(personajes_loteria.values())
personajes_loteria_jpg={values: f'{values}.jpg' for values in personajes_loteria.values()}

cartas_mostradas=[]
win=0

imagen_negra=Image.new('RGB', (500, 750), (0, 0, 0))
matriz_loteria=matriz(personajes_loteria)

for i in range(0,40):
    while True:
        random_card=random.choice(list(personajes_loteria_jpg.values()))
        if random_card not in cartas_mostradas:
            break

    random_choice_nojpg=random_card.replace('.jpg','')
    imagen_azar=(f'Cartas/{random_card}')
    mnts=Image.open(f'{imagen_azar}')
    mnts=mnts.resize((500,750))
    mnts.show()
    time.sleep(0.01)
    imagen_negra.show()
    cartas_mostradas.append(random_card)
    print(matriz_loteria)
    carta_q_salio=input('Que carta te salio? ')
    
    if carta_q_salio==random_choice_nojpg and random_choice_nojpg in matriz_loteria:
        print('Nice')
        win+=1
        if win==16:             
            print('Has Ganado!')
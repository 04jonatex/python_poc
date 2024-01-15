##############creacion de listas #################3


# 1. listas vacia

lista_vacia : list = ()

# 2. lista con elementos 

motocicletas = ["honda","yamaha","suzuki","honda"]

##############inserciones y actualizaciones###############3

motocicletas.append('ducati')
motocicletas.insert('daelin')
motocicletas[1] = 'bmw'


####################borrados#################3

motocicletas.pop(0)
borrar_ultimo_elemento = motocicletas.pop()
motocicletas.remove('yamaha')
motocicletas.clear()

######## sort #############

vocales = [e,i,o,u,a] 
vocales.sort()

############################# acseso alas listas ###############

numeros = [2,3,1,5,4]
primer_elemento = numeros[0]
primeros_elementos = numeros[0:2]
ultimo_elemento = numeros[-1]
ultimos_elementos = numeros[-2:]

# 1x1
numeros[::1]
#2x2
numeros[::2]
# en reversa
numeros[::-2]


#
comida = ['pizza','pollo','tacos']

comida.copy
comida.extend()































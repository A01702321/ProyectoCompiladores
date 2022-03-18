# Max Burkle Goya - A01702321
# Analizador lexico en programa de python

def eliminate_duplicates(list):
    '''
    Función que elimina elementos duplicados de una lista
    :param list: lista a revisar para eliminar elementos duplicados
    :type list: list
    :return: regresa la lista sin elementos duplicados
    :rtype: list
    '''
    res = []
    dupe = False
    for i in list:
        for j in res:
            if i == j:
                dupe = True
        if dupe == False:
            res.append(i)
        dupe = False
    return res

def clean_terminals(nonterminal, terminal):
    '''
    Función para limpiar lista de terminales de no terminales
    :param nonterminal: lista de elementos no terminales
    :type nonterminal: list
    :param terminal: lista de elementos terminales a limpiar
    :type terminal: list
    :return: lista de elementos terminales limpia
    :rtype: list
    '''
    res = []
    terminales = False
    for i in terminal:
        for j in nonterminal:
            if i == j:
                terminales = True
        if terminales == False:
            res.append(i)
        terminales = False
    return res

def fix_epsilon(list):
    '''
    Función para eliminar el elemento como epsilon de una lista
    :param list: lista a analizar
    :type list: list
    :return: lista sin elementos epsilon
    :rtype: list
    '''
    res=[]
    for i in list:
        if i != "'":
            res.append(i)
    return res

file = input("Ingresar nombre o dirección de archivo de entrada: ")    
f = open(file, "r")
# primer linea del archivo específica la cantidad de linea a leer
lines = int(f.readline())

# identificador de elemento separador de expresiones
separator = '->'

terminal = False
stack = []
terminales = []
noterminales = []

# agregar los elementos a las listas correspondientes
for i in range(lines):
    stack=(f.readline().rstrip('\n').split())
    for x in stack:
        if x == separator:
            terminal = True
        if x!= separator:
            if terminal:
                terminales.append(x)
            else:
                noterminales.append(x)
    terminal = False

# eliminar elementos duplicados y "limpiar" la lista de terminales
noterminales = eliminate_duplicates(noterminales)
terminales = clean_terminals(noterminales ,terminales)
terminales = eliminate_duplicates(terminales)

terminales = fix_epsilon(terminales)
noterminales = fix_epsilon(noterminales)

print('Terminal:', end =" ")
print(*terminales, sep = ", ")
print('Non terminal:', end =" ")
print(*noterminales, sep = ", ")
import string 

def contar_palabras(texto):
    palabras = limpiar_texto(texto)

    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def limpiar_texto(texto):
    texto = texto.lower()
    for signo in string.punctuation:
       texto = texto.replace(signo, "")

    return texto.split() 

def palabras_para_el_porcentaje(porcentaje, contador_dicc):
    total = sum (contador_dicc.values())
    objetivo = total * porcentaje

    sort = sorted(contador_dicc.items(), key=lambda x: x[1], reverse=True)
    acumulado = 0
    necesarias = 0

    for palabra, frecuencia in sort:
        acumulado += frecuencia
        necesarias += 1
        if acumulado >= objetivo:
            break

    return necesarias, sort 

def leer_texto(path):
    with open(path, 'r', encoding='utf-8') as f:
        texto = f.read()
    return texto

porcentaje = 0.8

path = 'varios/pg1661.txt'
texto = leer_texto(path)
contador_dicc = contar_palabras(texto)
necesarias, sort = palabras_para_el_porcentaje(porcentaje,contador_dicc)
print(f'Total de palabras:  {sum (contador_dicc.values())}')
print(f'Total palabras unicas: {len(contador_dicc.items())}')
print(f'Palabras unicas necesarias para cubrir el {porcentaje} del libro: {necesarias}')
print('Las 20 palabras mas repetidas:\n')

for i in range(20):
    print(sort[i])

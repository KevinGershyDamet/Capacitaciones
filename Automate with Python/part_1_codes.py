#! python3

####################### Listas ####################### 

print(list('hola'))

print(list(range(0,100,2)))

lista = ['perro', 'gato', 'culebra']
hola, chau, maso = lista
print(hola, chau, maso)

a, b = 'AAA', 'BBB'
print(a, b)
b, a = a, b
print(a, b)

print(lista.index('culebra'))

lista.append('pajaro')
print(lista)

lista.insert(1,'pescado')
print(lista)

lista.remove('culebra')
print(lista)

del lista[0]
print(lista)

lista.sort() 
print(lista)
lista.sort(reverse=True)
print(lista)

lista_2 = ['a', 'A', 'z', 'Z', 'B']
lista_2.sort()
print(lista_2)
lista_2.sort(key=str.lower)


print('gato' in lista)
for letra in 'Kev':
    print(letra)

print('kev'[-1]) # el índice negativo comienza por el final

texto = 'Soy potente'
texto_nuevo = texto[0:texto.index(' ')] + ' muy ' + texto[texto.index('potente'):]
print(texto_nuevo)



listota = [0, 1, 2, 'potente', 'el wey']
elementos = listota
elementos[3] = 'recontra potente'
print(elementos)
print(listota) # ESTO SIEMPRE PASARÁ CON LAS LISTAS!!! LA LINEA 56 HIZO QUE AHORA TENGAMOS DOS FORMAS DE REFERENCIAR A LA MISMA LISTA
# LO MISMO PASARÁ PARA TODOS LOS VALORES MUTABLES QUE SE ASIGNEN A VARIABLES. CON LOS VALORES INMUTABLES, EN CAMBIO (COMO STRINGS O TUPLAS), NO PASARÁ ESTO



import copy
elementos_2 = copy.deepcopy(listota)
listota.append('uno')
print(listota, elementos_2, elementos)



# Dos diccionarios con las mismas llaves pero en diferente orden serán considerados iguales

dico = {'uno': 1,
        'dos': 2}

print('uno' in dico)

print(list(dico.keys()), dico.values(), dico.items())

for i,j in dico.items():
    print(i,j)

print(dico.get('uno', 0)) # Se solicita la llave 'uno', y si no está definida, se devuelve el valor cero

dico['tres'] = 3 # Sin embargo, si 'tres' ya existe, se estaría cambiando el valor de dicha llave (y podríamos no querer eso)
print(dico)
# En vez de esto, podemos usar lo siguiente:
dico.setdefault('cuatro', 4) # Esto solo agregará el valor si es que 'cuatro' aún no existe como llave (si ya existe, no hará nada)
print(dico)


textaso = 'Hoy estoy recontra contento porque he comenzado a hacer natación. Además estoy aprendiendo japonés y programación, y profundizando mis conocimientos de música.'
# Ahora crearemos un diccionario con el número de veces en que aparece cada letra
contador_de_letras = {}
for letra in textaso.upper(): # Upper lo convierte en mayúsculas
    contador_de_letras[letra] = contador_de_letras.get(letra, 0) + 1
print(contador_de_letras)
import pprint
pprint.pprint(contador_de_letras) # Otorga el resultado de manera ordenada

print("This is Blaine's Charizard")
print('This is Blaine\'s Charizard') # "Escape character" permite colocar un valor que antes no era permitido en el texto

'''
    \' single quote
    \" double quote
    \t tab
    \n new line
    \\ Backslash
'''

print(r'This is Blaine\'s Charizard') # La r inicial hace que se interprete como "raw string" y los parámetros de escape se leen textualmente

textatote = '''Querido James Hetfield,
Estoy muy agradecido contigo por crear mi banda favorita en la vida.
            
Atentamente,
Kevin'''
print(textatote)

print('Hola' in 'Hola cómo estás')


print('Kev'.upper(), 'Kev'.lower())

# pregunta = input()

print('KEV'.isupper())
print('hola estoy bien emocionado'.title())
print('Hola estoy potente'.startswith('Ho'))

print(' '.join(['comida', 'deporte', 'música']))
print('Hola estoy, bien, emocionado'.split(','))
print('Hola'.rjust(20,'*'), 'Chau'.ljust(20))
print('Hola'.center(20,'-')) # Estos métodos agregarán caracteres hasta que la longitud total sea del largo especificado
print('     hola'.strip())
print('artHolatrrrrrraaaaaa'.strip('art')) # Elimina todas estas letras de los extremos, sin importar el orden
print('Holasa'.replace('s','a'))


import pyperclip
pyperclip.copy('Hello!!!')

nombre = 'Kev'
hora = '6 pm'
lugar = 'la playa'
print('Hola %s, te han invitado a una fiesta en %s a las %s.' %(nombre, lugar, hora))



##### Iniciar programas desde fuera de python (se coloca al inicio del código)

#! python3
'''
py.exe "Desktop\Capacitaciones de programación\Automate with Python\codes.py" esto es lo que se debe escribir desde la ventana de comandos
también se puede colocar 'py + ruta' directamente en la ventana que aparece en windows + R (aunque aquí la ventana se cierra automáticamente luego de que el código se ejecuta)

Para correr el archivo BAT, se coloca directamente en el comando la ruta entera + archivo BAT

Además, si no se quiere abrir la ventana de comandos, en vez de @py se puede utilizar @pyw

Además, se puede agregar la carpeta a PATH para solo escribir "corrida" en windows + R
'''



# Los números de teléfono pueden ser 333-444-0000 en EEUU y Canadá

import re
# Para trabajar con re, se usarán raw strings (r'')
numeros = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Nótese que en este caso \ NO ES UN ESCAPE CHARACTER, ya que \d indica dígito
mensaje = 'Puedes llamarme al 123-456-7890 o sino a la oficina al 987-654-1234'

resultado = numeros.search(mensaje)
print(resultado) # Este resultado es un "match"
print(resultado.group()) # Esto muestra el resultado anterior
print(numeros.findall(mensaje)) # Esto devuelve todas las ocurrencias

numeros_2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Los paréntesis separan a la cadena en dos grupos. Si quisiéramos buscar paréntesis, tendríamos que utilizar escape character, de la forma \(\)
resultado_2 = numeros_2.search(mensaje)
print(resultado_2.group(2))


chocoRegex = re.compile(r'choco(barra|animal|manzana)')
mo = chocoRegex.findall('Hola, me gusta la chocobarra, el chocoanimal y la chocomanzana')
print(mo)

batRegex = re.compile(r'Bat(wo)?man') # El ? genera que el campo entre paréntesis pueda repetirse 0 o 1 veces. Así, debe usarse \ para escapar el ? si se quiere usar como texto crudo
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Mi número es 122-3434')
print(mo.group())

# Al igual que ?, * indica uno conteo de ocurrencias, pero 0 o más (en vez de ?, que indica 0 o 1)
# El + indica una o más ocurrencias
# Finalmente, (wo){3} indica que se busca exactamente 3 veces la ocurrencia "wo"

haRegex = re.compile(r'(Aaaa)?(si){5}')
mo = haRegex.search('Aa sisisisisi nonononono')
print(mo.group())

# También se puede usar {1,3} (de 1 a 3 veces), o {3,} (3 o más veces)
# (wo){1,5} es greedy match, pues en un texto que contenga 5 veces repeitdo "wo" se hará el match con 5. Para tomar solo el primer wo, se usa non-greedy match, de la forma (wo){1,5}? (se añade ?)

# Recordemos que search busca la primera ocurrencia.

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
hallados = phoneRegex.findall('Estoy con los números 123-456-7890 y 987-654-3212')
print(hallados)

# Así como \d indica número, \s indica espacio y \w indica palabra (letra o número). Las mayúsculas D, S, W indican los complementos de las minúsculas

contador = re.compile(r'\d+\s\w+')
print(contador.findall('El día de hoy compraré 8 tuercas, 3 tornillos y 22 plátanos'))


# También podemos crear nuestra propia character class (así como existen \d, \s, \w) haciendo uso de []
regexObj = re.compile(r'[aeiou]')
regexObj = re.compile(r'[aeiouAEIOU]')
regexObj = re.compile(r'[a-f]') # letras desde la "a" hasta la "z" en minúsculas

# Además, si se quieren encontrar dos vocales (may o min) consecutivas:
regexObj = re.compile(r'[aeiouAEIOU]{2}')

regexObj = re.compile(r'[^aeiouAEIOU]') # Esto reconocerá al complemento de los caracteres señalados (en este caso, consonantes, caracteres especiales, y puntuaciones)
# Recordemos que en estos ejemplos estamos trabajando con character class propio (entre [])

# También podemos identificar si una cadena de texto empieza con lo requerido:
empieza = re.compile(r'^Hola')
print(empieza.search('Estoy chévere Hola'))
print(empieza.search('Hola estoy chévere'))
# También se podría usar "chau$" con $ al final, para indicar que lo buscado debe acabar con esta cadena de caracteres

# Nótese que "^\d+$" implica que la cadena entera debe ser numérica


# El caracter "." se entiende como cualquier caracter, excepto el de nueva línea
cualquiera = re.compile(r'.oto')
print(cualquiera.findall('Hola choto, estoy joto'))

cualquiera = re.compile(r'.{1,2}oto')
print(cualquiera.findall('Hola choto, estoy joto'))


# Notemos lo conveniente que puede ser usar .*:

chevere = re.compile(r'Nombre: (.*) Apellido: (.*)') # Notemos que aquí estamos generando dos grupos, y el findall devolverá tuplas con estos grupos
print(chevere.findall('Nombre: Kev Apellido: Gershy-Damet'))

# Solo tomemos en cuenta que .* es greedy; mientras que .*? es non-greedy


# Importante recordar que "." no hace alusión a caracter de nueva lína:
dotstar = re.compile(r'.*')
print(dotstar.search('Estoy chévere\nEstoy sexy\nEstoy potente'))
# Esto se soluciona con:
dotstar = re.compile(r'.*', re.DOTALL)
print(dotstar.search('Estoy chévere\nEstoy sexy\nEstoy potente'))
# De la misma forma, la opción re.IGNORECASE (o resumido a re.I) se puede usar para ignorar si [aeiou], por ejemplo, son mayúsculas o minúsculas


# Además, se puede usar el método de buscar y reemplazar (sub)
agentes = re.compile(r'agente \w+')
print(agentes.sub('CONFIDENCIAL', 'El agente paja se lleva chévere con el agente sexy'))

# También se puede tomar solo uno de los grupos (recordemos que cuando usamos (), findall devuelve solo los componentes del paréntesis - grupos)
agentes = re.compile(r'agente (\w)\w+')
print(agentes.sub(r'Agente \1****', 'El agente Ricky se lleva paja con el agente Covarianza'))
# Dos acotaciones: 1) el \1 hace alusión a que se usará el texto obtenido del grupo () número 1; 2) dado que usamos \, se debe usar una r al inicio, de forma que se trabaje como texto crudo (a diferencia del caso anterior, en donde 'CONFIDENCIAL' se escribía sin la r inicial)


# Finalmente, el comando VERBOSE hace que podamos expresar las cadenas de compile de manera más legible, pudiéndolas separar en diferentes líneas, en donde incluso podemos comentar:
hola = re.compile(r'''
\d\d\d  # Esto será el primer bloque de números
-
\d\d\d  # Este será el segundo bloque
-
\d\d\d\d    # Último bloque
''', re.VERBOSE)
print(hola.findall('Hola, estoy chévere y mi número es 999-111-2121'))
# Pueden combinarse múltiples argumentos en compile, de la forma re.VERBOSE | re.I

# Los caracteres colocados en [] al crear caracteres propios no necesitan llevar \ (escape)

# Para un email:

emailRegex = re.compile(r'''

# some.+-thing@casckodc?.com

[a-zA-z0-9_.+]+ # name part
@   # @ symbol
[a-zA-z0-9_.+]+ # sufix part
.com

''', re.VERBOSE)

print(emailRegex.findall('Hola, mi correo es kevin.gershydamet@gmail.com y el que tiene un pata es ricky_varianza_95@hotmail.com'))

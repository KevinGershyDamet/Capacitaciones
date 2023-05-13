
import os
# Biblioteca que permite trabajar con rutas, independientemente del sistema
ruta_actual = os.getcwd() # Devuelve el directorio actual

os.getcwd() # Esto simplemente implica que estamos trabajando en la carpeta misma
# os.chdir('C:\\') # Esto cambia el directorio al especificado
print(os.getcwd())

print(os.path.abspath('hola.png')) # Devuelve la ruta absoluta
print(os.path.abspath('..\\..\\spam.png'))
# Recordemos que .. representa a la carpeta padre; mientras que . representa a la carpeta actual

print(os.path.relpath(os.getcwd(), 'chevere.png'))
# Devuelve una ruta relativa, dadas dos rutas

print(os.path.getsize('..\..\..'))
# Devuelve el tamaño en bytes

print(os.listdir('..\..'))

# Por ejemplo, calculemos el peso total de los archivos en la dirección previa (solo de archivos y no de carpetas)
total_size = 0
for archivo in os.listdir('..\..'):
    if os.path.isfile(os.path.join('..\..', archivo)): # Join permite juntar archivos y devolver la ruta total según estándar de la computadora (Windows, en este caso) || isfile verifica si el argumento es un archivo (isdir verifica si es una carpeta)
        total_size += os.path.getsize(os.path.join('..\..', archivo))
        print(archivo, os.path.getsize(os.path.join('..\..', archivo)))
print(total_size)

try:
    os.makedirs(os.path.join(os.getcwd(), 'hola')) # Crea un directorio 
except:
    print('Carpeta ya creada')

# Abnrir y manejar archivos
archivo = open('C:\\Users\\buser\\Desktop\\Capacitaciones de programación\\Automate with Python\\texto.txt')
texto_archivo = archivo.read()
print(texto_archivo)
archivo.close()

archivo = open('C:\\Users\\buser\\Desktop\\Capacitaciones de programación\\Automate with Python\\texto.txt')
print(archivo.readlines())
archivo.close()

# Para abrir el modo escritura (se chanca) se usa 'w'; mientras que para añadir al final (appen) se usa 'a'
archivo = open('C:\\Users\\buser\\Desktop\\Capacitaciones de programación\\Automate with Python\\texto.txt', 'w')
# El archivo especificado puede no existir, en cuyo caso se creará uno nuevo con ese nombre
archivo.write('Estoy potentísimo')
archivo.write('Estoy potentísimo')
archivo.close()
archivo = open('C:\\Users\\buser\\Desktop\\Capacitaciones de programación\\Automate with Python\\texto.txt', 'a')
archivo.write('Esta es la única línea que se adjuntará al final, con el método append')
archivo.close()



import shelve
shelveFile = shelve.open('mydata')
shelveFile['juegos'] = ['Mario Bros.', 'Pokémon Sword', 'Pokémon XD: Gale of Darkness']
shelveFile.close()
# Esto genera un archivo nuevo en el que se guardará esta información!
shelveFile = shelve.open('mydata')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))



import shutil
shutil.copy('texto.txt', '..\\chevere.txt')
try:
    shutil.copytree('.', '..\\automate_backup')
except:
    print('La carpeta ya existe')
# shutil.move('.\\texto.txt', '.\\nuevo_texto.txt') # Para renombrar, se mueve a la misma carpeta pero con un nuevo nombre


try:
    os.unlink('prueba.txt')
except:
    print('El archivo no existe')
# Elimina el archivo seleccionado. Asimismo, os.rmdir() elimina el directorio seleccionado (SOLO SI ESTÁ VACÍO). Para remover folder con todos los archivos adentro, se utiliza shutil.rmtree()
# IMPORTANTE: ESTOS COMANDOS ELIMINAN PERMANENTEMENTE LOS ARCHIVOS (NO LOS ENVÍA A LA BANDEJA DE RECICLAJE)
# Alternativamente, se puede utilizar send2trash

import send2trash
try:
    send2trash.send2trash('send2trash_texto.txt')
except:
    print('El archivo no existe')


for folderName, subFolders, filenames in os.walk('..'):
    print('El nombre del folder es ' + folderName)
    print('Los subfolders en ' + folderName + ' son: ' + str(subFolders))
    print('Los archivos en ' + folderName + ' son: ' + str(filenames))
# el código os.walk recorre las carpetas del folder una por una


def hola(texto):
    if type(texto) != str:
        raise Exception('Debe introducirse un texto como argumento en la función')
    else:
        print('Hola, hoy quisiste decir ' + texto)
    
    assert texto.startswith('Hola'), 'El texto no comienza por hola' # Aquí, se pone la condición que debe cumplirse

hola('Hola, estoy potente')

import traceback
try:
    a = 1 / 0
except:
    print(traceback.format_exc())


import logging
logging.basicConfig(filename='errores.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # Esto permite desactivar todos los mensajes de DEBUG con esta única línea. CRITICAL es el nivel más alto de mensaje de debugging. Por ende, si desactivamos a nivel CRITICAL se desactivarán los mensajes de debug de todas las categorías. Para colocar otros tipos de mensaje de debug, se puede usar logging.info(), logging.critical(), logging, debug(), logging.error(), logging.warning(). Orden: debug, info, warning, error, critical

#Adicionalmente, si se quieren registrar todos los mensajes de debugging en un archivo, el primer argumento de basicConfig debe ser filename='texto.txt'. Si se elimina esta opción, los mensajes aparecerán en la consola

logging.debug('Inicio del programa')

def factorial(num):
    total = 1
    for x in range(1, num + 1):
        logging.debug('El valor de x en esta iteración es %s' %(x))
        total *= x
    return total

logging.debug('Fin del programa')
print(factorial(7))

import webbrowser
webbrowser.open('https://www.google.com')

import requests
import bs4 # beautifulsoup4

archivo = requests.get('https://www.google.com')
print(archivo.text)
print(archivo.raise_for_status()) # Si se descargó bien, no debería aparecer nada

playFile = open('Prueba.txt', 'wb') # 'wb' permite abrir el archivo en write binary
for chunk in archivo.iter_content(1000):
    playFile.write(chunk)


soup = bs4.BeautifulSoup(archivo.text, 'html.parser') # La opción se coloca para que no se muestre la advertencia
# print(soup.select('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')[0].text) # Aquí se copia y se pega el selector


# Con selenium, elemento.submit() permite enviar el formulario sin tener que hacer click en login
# Además, otros comandos útiles son browser.back(), browser.forward(), browser.refresh() y browser.quit() (este último cierra el navegador)



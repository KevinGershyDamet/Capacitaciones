
import pyautogui
width, height = pyautogui.size() # devuelve el tamaño del entorno en el que estamos trabajando
print(width, height)

print(pyautogui.position()) # devuelve la posición del mouse
pyautogui.moveTo(50, 50, duration = 0.4) # desplaza el mouse, el argumento duration es opcionals
pyautogui.moveRel(10, 0, duration = 0.4) # desplaza en relación a la posición actual
# pyautogui.click(1833, 54) # hace click en la posición seleccionada. También existe la función doubleClick y rightclick. Estas no requieren coordenadas y harán click donde sea que el cursor se encuentre. También se encuentra la función drag, que arrastra el cursos mientras hace click

# SI EN ALGÚN MOMENTO SE QUIERE PAUSAR EL CÓDIGO DE CONTROL DE CURSOR, DEBEMOS TENER EN CUENTA QUE EL PROGRAMA SIEMPRE GENERARÁ PAUSAS CADA DÉCIMA DE SEGUNDO. AQUÍ, DEBEMOS LLEVAR EL CURSOR MANUALMENTE HACIA LA ESQUINA SUPERIOR IZQUIERDA. EL PROGRAMA AUTOMÁTICAMENTE VERIFICARÁ SI SE ENCUENTRA AHÍ, Y PAUSARÁ DE SER ASÍ

# Desde la ventana de comandos, podemos escribir import pyautogui, y luego pyautogui.displayMousePosition()
# pyautogui.click(148, 181)
# pyautogui.typewrite('Hello Harry Potter, my name is Tom Riddle', interval = 0.2)

# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y']) # Aquí mandamos la lista de caracteres que queremos presionar desde el teclado

print(pyautogui.KEYBOARD_KEYS) # Nos permite saber qué teclas efectivamente podemos usar del teclado

# pyautogui.press puede apretar una sola tecla a la vez, en vez de typewrite. Además, pyautoguy.hotkey('ctrl', 'o') permite mandar una combinación de teclas para atajos

pyautogui.screenshot('ejemplo.png')
# pyautogui.locateOnScreen('boton.png') # se inserta una imagen con la sección que se desea detectar. La función devolverá localización, así como altura y ancho de la sección de la imagen
# pyautogui.locateCenterOnScreen(ruta) # funciona igual que la anterior, pero solo devuelve las coordenadas del centro de la sección de imagen hallada

# ESTAS FUNCIONES SERÁN RELATIVAMENTE LENTAS, Y PUEDEN TOMAR HASTA UN SEGUNDO EN EJECUTARSE. SE RECOMIENDA NO UTILIZARLAS EN CONTEXTOS DE REACCIÓN RÁPIDA (JUEGOS EN TIEMPO REAL, POR EJEMPLO)


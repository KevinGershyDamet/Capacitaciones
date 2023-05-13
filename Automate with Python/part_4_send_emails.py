
import smtplib

correo = 'kevin.gershydamet@gmail.com'
contraseña = 'tvmoxodoavwrzrcr' # CONTRASEÑA GOOGLE DESDE APLICATIVO

conexion = smtplib.SMTP('smtp.gmail.com', 587) # Esto especifica el servidor
# conexion = smtplib.SMTP('smtp-mail.outlook.com', 587)
conexion.ehlo() # Esto nos conecta con el servidor
conexion.starttls() # Encripta contraseña
conexion.login(correo, contraseña) # Aquí nos conectamos a nuestra cuenta

# conexion.sendmail(correo, correo, 'Subject:Envio de mensaje automatico\n\nEstamos progresando de manera potente con nuestra programacion de Python.\n\nAtentamente,\n\nKev') # Los caracteres \n son necesarios para especificar que se ha acabado el encabezado. Esto devuelve un diccionario con los correos que no se llegaron a mandar.
# QUEDA PENDIENTE RESOLVER CÓMO COLOCAR TILDES EN EL CORREO
conexion.quit()


import imapclient
conexion = imapclient.IMAPClient('imap.gmail.com', ssl = True) # SSL se usa para encriptar
conexion.login(correo, contraseña)
conexion.select_folder('INBOX', readonly = True) # Esto impide que se eliminen correos. Para borrar correos, se usa readonly = False, y luego conexion.delete_messages([lista])

UIDs = conexion.search('SINCE 20-Jan-2023')
raw_message = conexion.fetch([14890], ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(raw_message[14890][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

# Los mensajes pueden tener parte texto y parte html (formato con colores, por ejemplo)
print(message.text_part.get_payload().decode('UTF-8')) # El código identifica en qué formato se encodificó el correo. UTF-8 se usa la gran mayoría de veces

# Search se puede configurar con distintas opciones de búsqueda
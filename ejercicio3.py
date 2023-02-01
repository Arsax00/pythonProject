import re

e=input("Introduce un correo:")
email="^([a-z,\.,\-,\_,A-Z,0-9]{3,25})@([a-z]{4,}).com$"
comprobar= re.match(email,e)

if comprobar:
    print("Es válido")
else:
    print("No es válido")


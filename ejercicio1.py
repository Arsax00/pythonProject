import re
cadena="Tengo 4 gatos y 6 perros"

buscar=re.findall("6.*",cadena)

if buscar:
   print("Esta seguido por un 6")
else:
   print("No esta seguido por un 6")

import re

caracteres={"d,a,m"}
cadena="Hola que tal mami"
buscar=re.findall(caracteres,cadena)

if buscar:
    print("Tiene los caracteres d,a,m")
else:
    print("No contiene")
import re
from datetime import date
def matricula(dni, fec, mat, nom):
    registroDni="[0-9]{8,}[a-z,A-Z]"
    registroFecha="[dd-mm-aaaa]"
    registroMatricula="[0-9]{4}[A-Z]{3}"
    registroNombre="[A-Z]{1}[a-z]"+"[A-Z]{1}[a-z]"
    encajarDni= re.match(registroDni, dni.__str__())
    encajarFecha= re.match(registroFecha,fec)
    encajarMatricula= re.match(registroMatricula,mat)
    encajarNombre=re.match(registroNombre,nom)

    return encajarFecha,encajarDni,encajarMatricula,encajarNombre is not None

print(matricula("77978679P",date.today(),"2345FFI","Sara Isabel"))
import re

caracteres=({"d","a","m"})
cadena="damms"
buscarM=re.findall("m.*",cadena)
buscarD=re.findall("d.*",cadena)
buscarA=re.findall("a.*",cadena)
if buscarM and buscarA and buscarD and  cadena.__contains__(caracteres.__str__()) == False:
    print("Tiene los caracteres d,a,m")
elif cadena.__contains__(caracteres.__str__()):
    print("No tiene los caracteres d,a,m o tiene más caracteres ")
else:
    print("No tiene los caracteres d,a,m o tiene más caracteres ")
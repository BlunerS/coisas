from datetime import datetime

usuario = input("login:")

hora = datetime.now().time()
print("Usuario {usuario} logou às {H}:{M}:{S}".format(usuario=usuario,
    H=hora.hour, M=hora.minute, S=hora.second))
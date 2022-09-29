a=int(input("presione 1=registrarse "))
while a>2 or a<1:
    a=int(input("ingrese una opcion valida "))
if a==1:
    b=str(input("ingrese su nombre: "))
    c=str(input("ingrese patente del vehiculo: "))
    d=str(input("ingrese su rut: "))
    registro=[b,c,d]
print("ficha de registro terminada")
print("nombre: ",registro[0],"\npatente: ",registro[1],"\nrut: ",registro[2],"")
a=int(input("presione 2 para comenzar la carrera "))
if a==2:
    b=int(input("ingrese latitud eje (x)"))
    c=int(input("ingrese longitud eje (y) "))
    destino=[b,c]
    d=int(input("presione 1 para encender el auto "))
    print("el auto esta encendido ")
    i=0
    i=0
while d==1:
    d=int(input("-si desea acelerarlo prisione 1\n-si desea apagarlo presione 3\n-si desea girarlo presione 2\n "))
    if d==1:
        while d==1:
            for i in range(i,i+1):
                i=i+10
                print("el vehiculo va a ",i,"km/h")
            d=int(input("-si desea seguir acelerando presione 1\n-para volver al menu anterior presione 2"))
        if d==2:
           d=1
    if d==2:
        while d==2:
            print("usted esta en el eje x")
            d=int(input("-para cambiarse presione 2"))
            if d==2:
               print("usted esta ahora en el eje y")
            d=int(input("-para cambiarse presione 2\n-para volver al menu presione 1"))
    if d==3:
        while d==3:
            print("el vehiculo se a apagado ")
            break
        d=int(input("si desea encender el vehiculo nuevamente presione 1"))
        print("el vehiculo se a encendido")
def funcion(h1,h2,m1,m2,s1,s2):
    tm=m1+m2
    ts=s1+s2
    th=h1+h2
    if (ts>59):
        ts-=60
        tm=tm+1
    if (tm>59):
        tm-=60
        th=th+1
    print("El tiempo total del corredor es ",th," horas ",tm," minutos ",ts," segundos ")
    return (th,tm,ts)

i=1
tiempo_total=0
ttm=0
tts=0
bandera1=bandera2=False
print("Carrera de Ciclistas ")
while (1):
    while(bandera1==False):
        print("\nIngresar el tiempo acumulado del ciclista Nº ",i);
        h1=int(input("Horas acumuladas = "))
        m1=int(input("minutos = "))
        s1=int(input("segundos = "))
        if(h1<0 or m1<0 or m1>59 or s1<0 or s1>59):
            bandera1=False
        else:
            bandera1=True
    while(bandera2==False):
        print("cual es el tiempo de la ULTIMA ETAPA del corredor Nº",i," Menor a 4 horas")
        h2=int(input("Horas acumuladas = "))
        m2=int(input("minutos = "))
        s2=int(input("segundos = "))
        if(h2<0 or h2>3 or m2<0 or m2>59 or s2<0 or s2>59):
            bandera2=False
        else:
            bandera2=True
            i=i+1
    th,tm,ts=funcion(h1,h2,m1,m2,s1,s2)
    tiempo_total=tiempo_total+th
    ttm=ttm+tm
    tts=tts+ts
    if (tts>59):
        tts-=60
        ttm=ttm+1
    if (ttm>59):
        ttm-=60
        tiempo_total=tiempo_total+1
    print("valor de h total= ",tiempo_total)
    bandera1=False
    bandera2=False
    print(tiempo_total)
    print(ttm)
    print(tts)
    if (tiempo_total>=999):
        print("\n RESULTADOS\n Numero de Ciclistas : ",i-1)
        print("tiempo total de todos los ciclistas es : ",tiempo_total," horas ",ttm," minutos ",tts," segundos")
        break

tempo_segundos = int(input("Digite o tempo em segundos : "))

horas = tempo_segundos // 3600 
minutos = (tempo_segundos % 3600)//60
segundos = (tempo_segundos % 3600)%60
print(f"Horas : {horas}\nMinutos : {minutos}\nSegundos : {segundos}")
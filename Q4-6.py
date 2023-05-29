def tempo_total_segundos(dias, hora, min, seg):
    segundos = ((dias*24+hora)*60+min)*60+seg
    return segundos


dias1 = 2
hora1 = 5
min1 = 20
seg1 = 30
print("Tempo total:", tempo_total_segundos(
    dias1, hora1, min1, seg1), "segundos")

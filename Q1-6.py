mb = float(input("Informe o tamanho do arquivo em mb para download:"))
mbps = float(input("Informe a velocidade da internet:"))
tempo_download = mb/(mbps/8)/60
print("Tempo aproximado para download", tempo_download, "minutos")

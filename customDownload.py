import pytube

def bordeHorizontal(caracter,longitud):
    for i in range(longitud):
        print(caracter, end="")
    print()

def customDownload(link):
    pyt = pytube.YouTube(link)
    formatos = pyt.streams
    lista_itags = []
    indice = 1

    bordeHorizontal("_",49)

    print(f"|{'Opción':^15}|{'Formato':^15}|{'Calidad':^15}|")

    for formato in formatos:
        f = str(formato).split('"')
        itag = f[1]
        typef = f[3]
        res = f[5]
        lista_itags.append(itag)
        print(f"|{indice:^15}|{typef:^15}|{res:^15}|")
        indice+=1

    bordeHorizontal("-",49)

    op_calidad = int(input("Opción: "))
    pyt_selected=pyt.streams.get_by_itag(lista_itags[op_calidad-1])
    pyt_selected.download("./Downloads")
    print("Downloading...")
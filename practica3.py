import os,json, shutil
from collections import OrderedDict

def copiar(nombrearchivo,estado):
    f=open(nombrearchivo,"a")
    c=open(estado,"r")
    copiado = json.load(c)
    f.write("\n\n")
    f.write(json.dumps(copiado, indent=4))
    f.close()
    c.close()
    print(f">>archivo {estado} copiado en el fichero '{nombrearchivo}'")
    
def eliminar(archivo,codigopostal):
    f = open(archivo,"r+")
    mydata = json.load(f)
    del mydata[codigopostal]
    f.seek(0)
    f.truncate()
    f.write(json.dumps(mydata, indent=4))
    f.close()
    print(f">>se elimino el codigo postal {codigopostal} del archivo {archivo}")
        
def renombrar(archivo,nuevonombre):
    file_oldname = os.path.join(archivo)
    file_newname_newfile= os.path.join(nuevonombre)
    os.rename(file_oldname,file_newname_newfile)
    print(">>archivo renombrado")

def combinar(nombrearch1,nombrearch2):
    a1=open(nombrearch1,"r")
    a2=open(nombrearch2,"r")
    info1 = json.load(a1)
    info2 = json.load(a2)
    lista1 = list(info1.keys())
    lista2 = list(info2.keys())
    if len(lista1) < len(lista2):
        longmenor = len(lista1)
    else:
        longmenor = len(lista2)
    od = OrderedDict()
    for i in range(longmenor):
        od[lista1[i]] = info1[lista1[i]]
        od[lista2[i]] = info2[lista2[i]]
        v=i+1
    if len(lista1) > len(lista2):
        for j in range(v,len(lista1)):
            od[lista1[j]] = info1[lista1[j]]
    else:
        for j in range(v,len(lista2)):
            od[lista2[j]] = info2[lista2[j]]
    n1=nombrearch1.split(".")[0]
    n2=nombrearch2.split(".")[0]
    with open(f"{n1}{n2}.json","w") as fp:
        fp.write(json.dumps(od,indent=4))
    print(f">>se combino el archivo {nombrearch1} con el archivo {nombrearch2} en el fichero")
    
def agrupar(lista):
    secuencia = 1
    while(True):
        if os.path.exists(f"Agrupacion{secuencia}"):
            secuencia+=1
        else:
            break
    os.makedirs(f"Agrupacion{secuencia}")
    for archivo in lista:
        shutil.copyfile(f"{archivo}",f"Agrupacion{secuencia}/{archivo}")
    print(f">>archivos agrupados en la carpeta 'Agrupacion{secuencia}'")
    
entrada=""
while(True):
    entrada = input(">")
    if entrada.split()[0]  == 'copiar':
        copiar(entrada.split()[1],entrada.split()[2])
    elif entrada.split()[0]  == 'eliminar':
        eliminar(entrada.split()[1],entrada.split()[2])
    elif entrada.split()[0]  == 'renombrar':
        renombrar(entrada.split()[1],entrada.split()[2])
    elif entrada.split()[0] == 'combinar': 
        combinar(entrada.split()[1],entrada.split()[2])
    elif entrada.split()[0] == 'agrupar':
        agrupar([entrada.split()[1],entrada.split()[2],entrada.split()[3],entrada.split()[4],entrada.split()[5]])      
    elif entrada == 'EXIT':
        os.system("cls")
        break
    else:
        print('No se reconoce como un comando interno o externo')         



miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
listaPure = []
i = 0
x = 0
for i in range(len(miLista)):
    
    for x in range(len(miLista[i:])):
        
        if miLista[i] != miLista[x]:
            
            listaPure.append(miLista[x])
            print(listaPure,i,x)
    
   

print("La lista solo con elementos únicos:")
print(listaPure)

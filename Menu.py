from Pelicula import listasimple_peliculas

def lectura():

    
    lec_archivo=open('archivo prueba.lfp','r' )
    peliculas=lec_archivo.read().split("\n")
    
    aux=listasimple_peliculas()
    for lineas in peliculas:
        pelicula2= lineas.split(";")
        aux.insertar(pelicula2[0],pelicula2[1],pelicula2[2],pelicula2[3])

    print("Se cargó el archivo exitosamente!")
    return aux


def menu():
    op_menu=''

    aux_todo=listasimple_peliculas()            
    while op_menu != '5':
        print("----------Menu------------")
        print("1. Cargar archivos ")
        print("2. Gestionar pelicula")
        print("3. Filtrado")
        print("5. Salir")
        op_menu=input("Ingrese su opcion: ")

        if op_menu=="1":
            
            aux_todo=lectura()
            
            print("")

        
        elif op_menu=="2":
            print("")
            print('a. Mostrar peliculas')
            print('b. Mostrar actores')
            opcion2=input("Ingrese su opción ")
            if opcion2=="a":
                print(" ")

                aux_todo.listar_pel()
            
            elif opcion2=="b":
                print(" ")
                aux_todo.listar_ac()



        elif op_menu=='3':
            print(" ")
            print("a. Filtrado por actor")
            print("b. Filtrado por año")
            print("c. Filtrado por genero")
            opcion3=input("Ingrese su opciones: ")

            if opcion3=="a":
                print(" ")
                aux_actor=input("ingrese el año de la pelicula ")
                actor=aux_todo.buscarActor(aux_actor)
                if actor is not None:
                
                    print(actor)
                

            if opcion3=="b":
                print("")

                anio=input("ingrese el año de la pelicula ")
                actor=aux_todo.buscarAnio(anio)
                if actor is not None:
                
                    print(actor)

                else:
                    print("No se encontro el dato")

            if opcion3=="c":
                print("")
                genero=input("ingrese el género de la pelicula: ")
                actor=aux_todo.buscarGenero(genero)
                if actor is not None:
                
                    print(actor)

                else:
                    print("No se encontro el dato")
                   



            
                


        elif op_menu=='4':
            print("se grafico")

        elif op_menu=='5':
            print("Finaliza el Programa")
        
        else:
            print("opcion incorrecta")



print("Lenguajes Formales y de Programacion")
print("Seccion: A+")
print("Fernando Misael Morales Ortíz")
print("202001950")
tecla=''
while tecla !="c":
    tecla=input("Bienvenido al programa, para continuar presiones la tecla 'c' ")

    if tecla=="c":
        menu()
    else:
        print("NO se puede continuar")
        print("Ingrese correctamente la tecla solicitada")









            


class Pelicula:
    def __init__(self, nombre, actores, anio, categoria):
        self.nombre=nombre
        self.actores=actores
        self.anio=anio
        self.categoria=categoria
        self.siguiente=None

    def __str__(self):
        return "%s %s" %(self.nombre, self.anio, self.categoria)

class listasimple_peliculas:
    def __init__(self):
        self.cabeza=None
        self.tamaño=0
         

    def insertar(self,nombre,actores, anio,categoria):
        nuevoNodo=Pelicula(nombre,actores,anio,categoria)
        if self.tamaño == 0:
            self.cabeza = nuevoNodo

        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente !=None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevoNodo 
        self.tamaño += 1




    def listar_pel(self):
        auxiliar_dato=self.cabeza
        while auxiliar_dato !=None:
            print(auxiliar_dato.nombre + " "+auxiliar_dato.anio+ " "+auxiliar_dato.categoria )
           
            auxiliar_dato=auxiliar_dato.siguiente

    def listar_ac(self):
        auxiliar_dato=self.cabeza
        while auxiliar_dato !=None:
            print(auxiliar_dato.actores )
           
            auxiliar_dato=auxiliar_dato.siguiente

    def buscarActor(self,actor):
        aux=self.cabeza
        while aux !=None:
            if aux.anio == actor:
                print(aux.nombre )
            aux=aux.siguiente
        return None
    
    def buscarAnio(self,anio):
        aux=self.cabeza
        while aux !=None:
            if aux.anio == anio:
                print(aux.nombre +  ", "+aux.categoria )
            aux=aux.siguiente
        return None
            
    def buscarGenero(self,categoria):
        aux=self.cabeza
        while aux !=None:
            if aux.categoria == categoria:
                print(aux.nombre +  " " )
            aux=aux.siguiente
        

            
            




        
        






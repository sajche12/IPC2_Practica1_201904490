from classes.tablero import Tablero
from classes.lista_tablero import ListaTablero
from classes.lista_piezas import ListaPiezas
from classes.pieza import Pieza
import graphviz
class Menu:
    lista_tableros = ListaTablero()
    lista_piezas = ListaPiezas()
    
    def grafica_tablero(self, matriz):
        # Convertir la cadena "matriz" en un grafo
        grafica = graphviz.Digraph()
        
        grafica.node("nombre", "Guatematel")
        # Agregar los nodos de cada número de fila y columna
        for tablero in self.lista_tableros.lista_tablero:
            for i in range(0, int(tablero.filas)+1):
                grafica.node(str(i), str(i))
                if i == 0:
                    grafica.edge("nombre", str(i))
                    grafica.edge(str(i), str(i+1))
                elif i < int(tablero.filas):
                    grafica.edge(str(i), str(i+1))
            for j in range(1, int(tablero.columnas)+1):
                grafica.node(str(j)+'.'+str(j), str(j))
                grafica.edge("nombre", str(j)+'.'+str(j))
                
        # Agregar los nodos de cada pieza
        # Convertir cada fila de la matriz en un nodo y cada pieza en un borde
        for i, fila in enumerate(matriz.split('\n'), start=1):
            for j, pieza in enumerate(fila.split('|'), start=1):
                if pieza.strip():
                    grafica.node(str(i) + ',' + str(j), pieza.strip(), color="blue")
                elif not pieza.strip():
                    grafica.node(str(i) + ',' + str(j), str(""))
                if j < len(fila.split('|')) - 1:
                    grafica.edge(str(i) + ',' + str(j), str(i) + ',' + str(j+1))
                    
            
                
            



        # Guardar la gráfica en un archivo
        grafica.render('grafica.dot', format='png', view=True)
        
    def tablero(self):
        #definiendo filas y columnas
        columnas = int(input("\nIngrese el ancho del tablero: "))
        filas = int(input("Ingrese el alto del tablero: "))
        tablero_nuevo = Tablero(filas, columnas)
        self.lista_tableros.lista_tablero.agregar(tablero_nuevo)
        
        while True:
            for tablero in self.lista_tableros.lista_tablero:
                print("\nQue color desea utilizar:")
                print("a. Azul")
                print("b. Rojo")
                print("c. Verde")
                print("d. Purpura")
                print("e. Naranja")
                letra_color = input("\nIngrese la letra del color a utilizar: ")
                letra_color = letra_color.lower()
                
                #agregamos el color de la pieza a la lista
                if letra_color == "a":
                    print(f"\nSu color es: Azul")
                    print(f"Rango de filas: 1-{tablero.filas}")
                    posicion_fila = int(input("Ingrese el numero de la fila donde desea colocar la pieza: "))
                    print(f"\nRango de columnas: 1-{tablero.columnas}")
                    posicion_columna = int(input("Ingrese el numero de la columna donde desea colocar la pieza: "))
                    print(f"\nSu pieza color Azul se encuentra en la posicion: Fila:{posicion_fila},Columna:{posicion_columna}")
                    pieza_nueva = Pieza(letra_color, posicion_fila, posicion_columna)
                    self.lista_piezas.lista_piezas.agregar(pieza_nueva)
                elif letra_color == "b":
                    print(f"\nSu color es: Rojo")
                    print(f"Rango de filas: 1-{tablero.filas}")
                    posicion_fila = int(input("Ingrese el numero de la fila donde desea colocar la pieza: "))
                    print(f"\nRango de columnas: 1-{tablero.columnas}")
                    posicion_columna = int(input("Ingrese el numero de la columna donde desea colocar la pieza: "))
                    print(f"\nSu pieza color Rojo se encuentra en la posicion: Fila:{posicion_fila},Columna:{posicion_columna}")
                    pieza_nueva = Pieza(letra_color, posicion_fila, posicion_columna)
                    self.lista_piezas.lista_piezas.agregar(pieza_nueva)
                elif letra_color == "c":
                    print(f"\nSu color es: Verde")
                    print(f"Rango de filas: 1-{tablero.filas}")
                    posicion_fila = int(input("Ingrese el numero de la fila donde desea colocar la pieza: "))
                    print(f"\nRango de columnas: 1-{tablero.columnas}")
                    posicion_columna = int(input("Ingrese el numero de la columna donde desea colocar la pieza: "))
                    print(f"\nSu pieza color Verde se encuentra en la posicion: Fila:{posicion_fila},Columna:{posicion_columna}")
                    pieza_nueva = Pieza(letra_color, posicion_fila, posicion_columna)
                    self.lista_piezas.lista_piezas.agregar(pieza_nueva)
                elif letra_color == "d":
                    print(f"\nSu color es: Purpura")
                    print(f"Rango de filas: 1-{tablero.filas}")
                    posicion_fila = int(input("Ingrese el numero de la fila donde desea colocar la pieza: "))
                    print(f"\nRango de columnas: 1-{tablero.columnas}")
                    posicion_columna = int(input("Ingrese el numero de la columna donde desea colocar la pieza: "))
                    print(f"\nSu pieza color Purpura se encuentra en la posicion: Fila:{posicion_fila},Columna:{posicion_columna}")
                    pieza_nueva = Pieza(letra_color, posicion_fila, posicion_columna)
                    self.lista_piezas.lista_piezas.agregar(pieza_nueva)
                elif letra_color == "e":
                    print(f"\nSu color es: Naranja")
                    print(f"Rango de filas: 1-{tablero.filas}")
                    posicion_fila = int(input("Ingrese el numero de la fila donde desea colocar la pieza: "))
                    print(f"\nRango de columnas: 1-{tablero.columnas}")
                    posicion_columna = int(input("Ingrese el numero de la columna donde desea colocar la pieza: "))
                    print(f"\nSu pieza color Naranja se encuentra en la posicion: Fila:{posicion_fila},Columna:{posicion_columna}")
                    pieza_nueva = Pieza(letra_color, posicion_fila, posicion_columna)
                    self.lista_piezas.lista_piezas.agregar(pieza_nueva)
            
                matriz = ""
                for i in range(1, int(tablero.filas)+1):
                    fila = ""
                    for j in range(1, int(tablero.columnas)+1):
                        pieza = None
                        for pieza_encontrada in self.lista_piezas.lista_piezas:
                            if pieza_encontrada.posicion_fila == i and pieza_encontrada.posicion_columna == j:
                                pieza = pieza_encontrada
                                break
                        if pieza:
                            fila += pieza.color + "|"
                        else:
                            fila += " |"
                    matriz += fila + "\n"
                print(matriz)
                
                      
            print("¿Quieres agregar otra pieza?")
            print("a. Si")
            print("b. No")
            opcion = input("\nIngrese una opcion: ")
            if opcion == "a":
                continue
            elif opcion == "b":
                break
            
        print("\nGenereando grafica del tablero...")   
        self.grafica_tablero(matriz)
                                
    def datos_estudiante(self):
        print("\n----------------------------------------------------------------")
        print("| 1. DIEGO ALDAIR SAJCHE AVILA                                   |")
        print("| 2. 201904490                                                   |")
        print("| 3. INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 SECCION D    |")
        print("| 4. INGENIERIA EN CIENCIAS Y SISTEMAS                           |")
        print("------------------------------------------------------------------\n")
    
    def menu_principal(self):
        while True:
            print("-----------MENU PRINCIPAL-----------")
            print("| 1. CREAR TABLERO                 |")
            print("| 2. MOSTRAR DATOS DEL ESTUDIANTE  |")
            print("| 3. SALIR                         |")
            print("------------------------------------")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.tablero()
            elif opcion == "2":
                self.datos_estudiante()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print("Opcion no valida, ingrese una entre 1 y 3")
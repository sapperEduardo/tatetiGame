import tkinter as tk
import numpy as np


matriz = np.array( [['','',''] for x in range(3)] )

matriz_botones = []


class boton: 
    jugadas = 0
    turno = 'X'
    presionar = True 
    id_reinicio_programado = 0

    def __init__(self, master, row, column, Self):
        self.Self = Self
        self.row = row    
        self.column = column
        self.master = master

        self.texto = tk.StringVar(value='')

        self.boton = tk.Button(self.master, width=4, pady=16 , textvariable=self.texto, font='arial 40 bold', fg='black', relief='raised' )
        self.boton.config(command= self.Presionar )
        self.boton.grid( row=self.row, column=self.column )
        

    # funcion principal de cada boton
    def Presionar(self):

        if self.texto.get() == '' and boton.get_presionar():
            self.Marcar_posicion()
            boton.jugadas += 1

            if boton.get_jugadas() > 4:
                ganador = self.Hay_ganador()            
                if bool(ganador):
                    boton.no_presionar(self)
                    jugador = ganador[0]
                    raya = ganador[1] 
                    self.Self.Sumar_puntos(jugador)
                    self.Marcar_raya(raya, jugador)
                elif boton.get_jugadas() == 9:
                    boton.no_presionar(self)
                    self.Marcar_empate()
            self.Cambiar_turno(self)

    def Marcar_posicion(self):
        turno = boton.get_turno()
        matriz[self.row][self.column] = turno
        self.texto.set(turno)

    def Hay_ganador(self):
        global matriz
        for i in range(3):
            if matriz[i,0] == matriz[i,1] == matriz[i,2] and matriz[i,0] != '':
                return ( matriz[i,0], (1, i) )
        for i in range(3):
            if matriz.T[i,0] == matriz.T[i,1] == matriz.T[i,2] and matriz.T[i,0] != '':
                return ( matriz.T[i,0], (0, i) )
        if matriz[0, 0] == matriz[1, 1] == matriz[2, 2] != '': return (matriz[0,0], (2,1) )
        if matriz[0, 2] == matriz[1, 1] == matriz[2, 0] != '': return (matriz[0,2], (2,0) )
        return False

    def Marcar_raya(self, raya, jugador):
        global matriz_botones
        color = 'SeaGreen2' if jugador == 'O' else 'light slate blue'
        tipo, indice = raya[0], raya[1]
        
        if tipo == 1:[b.Color_fondo(color) for b in matriz_botones[indice]]
        if tipo == 0:[b.Color_fondo(color) for b in matriz_botones.T[indice]]
        
        if tipo == 2:
            if indice == 1: [b.Color_fondo(color) for b in matriz_botones.diagonal()]
            if indice == 0: [b.Color_fondo(color) for b in np.fliplr(matriz_botones).diagonal()]
        boton.id_reinicio_programado = self.master.after(1350, self.Reiniciar )

    def Marcar_empate(self):
        [ [b.Color_fondo('gold') for b in fila] for fila in  matriz_botones ]
        boton.id_reinicio_programado = self.master.after(1350, self.Reiniciar )
            
    def Reiniciar(self): 
        global matriz, matriz_botones
        matriz = np.array( [['','',''] for x in range(3)] )
        [ [b.texto.set('')  for b in fila] for fila in  matriz_botones ]
        boton.jugadas = 0
        boton.Despintar(self)
        boton.si_presionar(self)
    
    def Color_fondo(self, color):
        self.boton.config(bg=color)

    def Despintar(self):
        [ [b.Color_fondo('white') for b in fila] for fila in  matriz_botones ]

    @classmethod
    def Cambiar_turno(cls, self):
        cls.turno = 'O' if cls.turno == 'X' else 'X' 
        self.Self.Actualizar_turno()

    @classmethod
    def get_turno(cls):
        return cls.turno
    
    @classmethod
    def get_jugadas(cls):
        return cls.jugadas

    @classmethod
    def get_presionar(cls):
        return cls.presionar
    
    @classmethod
    def get_id_reinicio_programado(cls):
        return cls.id_reinicio_programado
    
    def no_presionar(self):
        boton.presionar = False

    def si_presionar(self):
        boton.presionar = True




def Crear_botones(master, self):
    global matriz_botones
    for i in range(3):
        fila = []
        for j in range(3):
            b = boton(master, i, j, self)
            fila.append(b)
        matriz_botones.append(fila)
    matriz_botones = np.array(matriz_botones)

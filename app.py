import tkinter as tk
import numpy as np

from botones import boton, Crear_botones





class App():


    def __init__(self):
        
        ## ventana rincipal ##
        self.root = tk.Tk()
        self.root.title('Tatetí')
        self.root.geometry('435x540')
        self.root.iconbitmap('C:\\tateti\\ico\\icono.ico')
        self.root.resizable(False, False)


        # variables 
        self.puntosX = tk.IntVar(value=0)
        self.puntosO = tk.IntVar(value=0)
        self.f_tablero = 'arial 15'
        self.color_X = 'light slate blue'
        self.color_O = 'SeaGreen2'

        # frame superior: el del tablero (puntuacion y turno)
        self.tablero = tk.Frame(self.root, bg='black', pady=7)
        self.marco = tk.Frame(self.tablero, width=440, height= 56, bg='gray40').grid(row=0, columnspan=4)    

        # configuracion del grid
        [self.tablero.grid_columnconfigure(x, weight=1) for x in range(4)]
        self.tablero.grid_rowconfigure(0, weight=1)


        self.etiquetaX = tk.Label(self.tablero, text='"X"', bg=self.color_X, fg='black', font=self.f_tablero, width= 9, height=2)
        self.etiqueta_puntosX = tk.Label(self.tablero, textvariable=self.puntosX, bg=self.color_X, font=self.f_tablero, width= 9, height=2)
        self.etiquetaO = tk.Label(self.tablero, text='"O"',  bg=self.color_O, fg= 
                                  'black', font=self.f_tablero, width= 9, height=2)
        self.etiqueta_puntosO = tk.Label(self.tablero, textvariable=self.puntosO, bg=self.color_O, font=self.f_tablero, width= 9, height=2)
        
        self.etiquetaX.grid(row=0, column=0)
        self.etiquetaO.grid(row=0, column=2)
        self.etiqueta_puntosX.grid(row=0, column=1)
        self.etiqueta_puntosO.grid(row=0, column=3)


        self.tablero.pack()


        # frame inferior: el del juego
        self.mesa = tk.Frame(self.root, bg='black')

        [self.mesa.grid_columnconfigure(x, weight=1) for x in range(3)]
        [self.mesa.grid_rowconfigure(x, weight=1) for x in range(3)]
        
        Crear_botones(self.mesa, self)

        self.mesa.pack(fill= 'both', expand=True)

        self.btn_reiniciar = tk.Button(self.root, text='REINICIAR PUNTOS', font='arial 10 bold', bg='orange red', fg='white', pady=5, command=self.Reiniciar_puntos)
        self.btn_reiniciar.pack(fill='x')

        self.Actualizar_turno()

        # bucle de la ventana principal 
        self.root.mainloop()


    def Actualizar_turno(self):
        turno  = boton.get_turno()

        if turno == 'X': 
            self.etiquetaX.config(fg='white') 
            self.etiquetaO.config(fg='black') 
        else: 
            self.etiquetaO.config(fg='white') 
            self.etiquetaX.config(fg='black') 

    def Sumar_puntos(self, jugador):
        if jugador == 'X':
            self.puntosX.set(self.puntosX.get() + 1)
        else:
            self.puntosO.set(self.puntosO.get() + 1)
    
    def Reiniciar_puntos(self):
        self.puntosO.set(0) 
        self.puntosX.set(0) 
        boton.Reiniciar(self)
        id_r_p = boton.get_id_reinicio_programado()
        if id_r_p:
            self.mesa.after_cancel(id_r_p)




app = App()









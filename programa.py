import webbrowser as webbrowser
import customtkinter as ctk
from sympy import symbols, integrate, lambdify, sympify, pi, E
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation



ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

x, y = symbols('x y')

def insertar_texto(valor):
    entry_funcion.insert("insert", valor)

def poner_funcion(funcion):
    entry_funcion.delete(0, "end")
    entry_funcion.insert(0, funcion)

def calcular():
    funcion_str = entry_funcion.get()
    try:
        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())
        y_min = float(entry_ymin.get())
        y_max = float(entry_ymax.get())
    except ValueError:
        output_label.configure(text="¡Error en los límites! Usa solo números.")
        return

    try:
        f = sympify(funcion_str)
    except:
        output_label.configure(text="¡Error! Función inválida.")
        return

    try:
        volumen = integrate(f, (x, x_min, x_max), (y, y_min, y_max))
        output_label.configure(text=f"Volumen: {volumen}")
        if check_grafica.get() == 1:
            graficar_superficie(funcion_str, f, x, y, x_min, x_max, y_min, y_max)
    except Exception as e:
        output_label.configure(text=f"Error en el cálculo: {e}")

def graficar_superficie(funcion_str, f, x_sym, y_sym, x_min, x_max, y_min, y_max):
    x_vals = np.linspace(x_min, x_max, 100)
    y_vals = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    f_numeric = lambdify((x_sym, y_sym), f, 'numpy')
    Z = f_numeric(X, Y)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Superficie: {funcion_str}")

    def animate(frame):
        elev = 30 + 15 * np.sin(np.radians(frame))  # Oscila entre 15 y 45 grados
        azim = frame  # Rota de 0 a 360
        ax.view_init(elev, azim)

    ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 1), interval=50)
    plt.show()

def abrir_ayuda():
    webbrowser.open("https://github.com/isaacDiazR/Calculadora-de-integrales-dobles")



# --- INTERFAZ ---
app = ctk.CTk()
app.geometry("950x900")
app.title("Calculadora de Volumen bajo Superficie")

fuente_estetica = ("Segoe UI", 20)



# Título principal
ctk.CTkLabel(app, text="📐 Calculadora de Volumen", font=("Segoe UI", 28, "bold")).pack(pady=20)


# Campo de función
frame_funcion = ctk.CTkFrame(app)
frame_funcion.pack(pady=10)
ctk.CTkLabel(frame_funcion, text="Función f(x, y):", font=fuente_estetica).pack(side="left", padx=10)
entry_funcion = ctk.CTkEntry(frame_funcion, width=500, font=fuente_estetica)
entry_funcion.pack(side="left")

# Botones de funciones de prueba
frame_funciones = ctk.CTkFrame(app)
frame_funciones.pack(pady=10)

ctk.CTkButton(frame_funciones, text="🌈 x*y + y^2", font=fuente_estetica, command=lambda: poner_funcion("x*y + y^2")).pack(side="left", padx=10)
ctk.CTkButton(frame_funciones, text="🔥 sin(x)*cos(y)", font=fuente_estetica, command=lambda: poner_funcion("sin(x)*cos(y)")).pack(side="left", padx=10)
ctk.CTkButton(frame_funciones, text="💧 exp(-x^2 - y^2)", font=fuente_estetica, command=lambda: poner_funcion("exp(-x^2 - y^2)")).pack(side="left", padx=10)

# Teclado
teclado_frame = ctk.CTkFrame(app)
teclado_frame.pack(pady=15)

botones = [
    ['7', '8', '9', '+', '-', 'π', 'e'],
    ['4', '5', '6', '*', '/', '(', ')'],
    ['1', '2', '3', '^', 'sqrt(', 'log(', 'ln('],
    ['0', '.', ',', 'sin(', 'cos(', 'tan(', 'exp('],
    ['x', 'y', '^2', '^3']
]

for i, fila in enumerate(botones):
    for j, texto in enumerate(fila):
        b = ctk.CTkButton(teclado_frame, text=texto, width=80, height=60, font=fuente_estetica,
                          command=lambda val=texto: insertar_texto(val))
        b.grid(row=i, column=j, padx=5, pady=5)

# Límites
frame_limits = ctk.CTkFrame(app)
frame_limits.pack(pady=20)

entry_xmin = ctk.CTkEntry(frame_limits, width=100, placeholder_text="x min", font=fuente_estetica)
entry_xmin.grid(row=0, column=0, padx=10)
entry_xmax = ctk.CTkEntry(frame_limits, width=100, placeholder_text="x max", font=fuente_estetica)
entry_xmax.grid(row=0, column=1, padx=10)
entry_ymin = ctk.CTkEntry(frame_limits, width=100, placeholder_text="y min", font=fuente_estetica)
entry_ymin.grid(row=0, column=2, padx=10)
entry_ymax = ctk.CTkEntry(frame_limits, width=100, placeholder_text="y max", font=fuente_estetica)
entry_ymax.grid(row=0, column=3, padx=10)

check_grafica = ctk.IntVar()
ctk.CTkCheckBox(app, text="Mostrar gráfica 3D", variable=check_grafica, font=fuente_estetica).pack(pady=10)

ctk.CTkButton(app, text="Calcular Volumen", command=calcular, font=fuente_estetica, height=60).pack(pady=20)


ctk.CTkLabel(app, text="- Isaac Diaz", font=fuente_estetica).pack(side="left", padx=10)
ctk.CTkLabel(app, text="- David Aceros", font=fuente_estetica).pack(side="left", padx=10)
ctk.CTkLabel(app, text="- Carlos Mantilla", font=fuente_estetica).pack(side="left", padx=10)

output_label = ctk.CTkLabel(app, text="", font=fuente_estetica, wraplength=700)
output_label.pack(pady=10)

# Botón de ayuda en esquina superior derecha
boton_ayuda = ctk.CTkButton(app, text="❓ Ayuda", command=abrir_ayuda, font=("Segoe UI", 16), width=100)
boton_ayuda.place(relx=0.97, rely=0.02, anchor="ne")


app.mainloop()
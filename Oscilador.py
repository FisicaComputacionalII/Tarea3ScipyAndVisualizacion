import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
def Oscilador(f0,df0,tf,beta,omega0,F=0,omega=0,steps=100):
    """Función que soluciona la ecuación diferencial dadas f0, df0
    los valores de f y su derivada en t=0, el tiempo final y el número de pasos.
    Entrega la solución para la posición (f(t)) y la velocidad(f'(t))"""
    # Definimos la función
    def f(y, t):
        """Oscilador armonico forzado amortiguado"""
        return np.array([y[1],-2*beta*y[1] -y[0]*omega0**2+F*np.cos(omega*t)])
    # Las condiciones iniciales
    y0 = np.array([f0, df0])
    # intervalo de integración
    t = np.linspace(0,tf, steps) 
    # Realizamos la integración
    sol = odeint(f, y0, t)
    # Entregamos el intervalo de tiempo, la posicion y la veocidad
    # como una tupla 
    return t, sol[:, 0], sol[:, 1]

def Plot(x,y,x_name="",y_name="",titulo="",Marker = '.',Color = "red"):
    """Esta función entrega una gráfica de """
    # Definimos figura y gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    #A continuación defina la estética y contenido de su gráfica
    # los valores de los ejes y el marcador 
    ax.plot(x, y, marker = Marker, c=Color)  
    # Se ponen titulo y nombre de los ejes
    ax.set(title = titulo,
        xlabel = x_name,
        ylabel = y_name)
    return fig

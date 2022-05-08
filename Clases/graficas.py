import matplotlib.pyplot as plt
import pandas as pd





class Graficas:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
    def histograma_precios(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Price"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('Precio', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_precio.png', bbox_inches='tight')
        return plt.show()
    
    def histograma_ingresos(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Avg. Area Income"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('Ingresos', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:green'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_ingresos.png', bbox_inches='tight')
        return plt.show()
    
    def histograma_edad(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["Avg. Area House Age"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('Edad', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:red'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_edad.png', bbox_inches='tight')
        return plt.show()
    
    def grafica_dispersion(self):
        
        fig, ax = plt.subplots()
        ax.scatter(self.datos["Price"],self.datos["Avg. Area Income"],self.datos["Avg. Area House Age"])
        ax.set_title('Precios vs Edad vs Ingresos', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        plt.savefig('Graficos/dispersion_precio_edad_ingresos.png', bbox_inches='tight')
        plt.show()
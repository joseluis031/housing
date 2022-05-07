import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
import numpy as np

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        #Bucle `que me indica si hay datos perdidos o no`
        for i in self.datos:
            if i =="":
                print("Hay datos perdidos")
                #En caso de haber datos perdidos, los sustituye por ceros
                self.datos.fillna(0)
            else:
                print("No hay datos perdidos")
    def calculo_media(self):
        media = self.datos["Avg. Area Income"].mean()
        return media
    def calculo_desviacion(self):
        desviacion = self.datos["Avg. Area Income"].std()
        return desviacion
    def percentiles(self, n):
        percentil = np.percentile(self.datos["Avg. Area Income"], n)
        return percentil
    def mediana(self):
        return self.datos["Avg. Area Income"].median()

     
     
    def calculo_media_area(self):
        media = self.datos["Avg. Area House Age"].mean()
        return media
    def calculo_desviacion_area(self):
        desviacion = self.datos["Avg. Area House Age"].std()
        return desviacion
    def percentiles_area(self, n):
        percentil = np.percentile(self.datos["Avg. Area House Age"], n)
        return percentil
    def mediana_area(self):
        return self.datos["Avg. Area House Age"].median() 
    
    
    
    def calculo_media_area_population(self):
        media = self.datos["Area Population"].mean()
        return media
    def calculo_desviacion_area_population(self):
        desviacion = self.datos["Area Population"].std()
        return desviacion
    def percentiles_area_population(self, n):
        percentil = np.percentile(self.datos["Area Population"], n)
        return percentil
    def mediana_area_population(self):
        return self.datos["Area Population"].median()  
    
    
    
    def calculo_media_precio(self):
        media = self.datos["Price"].mean()
        return media
    def calculo_desviacion_precio(self):
        desviacion = self.datos["Price"].std()
        return desviacion
    def percentiles_precio(self, n):
        percentil = np.percentile(self.datos["Price"], n)
        return percentil
    def mediana_precio(self):
        return self.datos["Price"].median() 
    
    
    
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
    
class Correlacion:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
    def correlacions(self):
        correlacion = np.corrcoef(self.datos["Avg. Area House Age"], self.datos["Avg. Area Income"])
        correlacion2 = np.corrcoef(self.datos["Price"], self.datos["Area Population"])
        return "{}\n{}".format(correlacion, correlacion2)
        
    
hola1 = Graficas("USA_Housing.csv")
hola2 = Correlacion("USA_Housing.csv")
print(hola2.correlacions())
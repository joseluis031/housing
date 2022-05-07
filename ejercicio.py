import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
import numpy as np

class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
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
    
    
    
    
hola = Ejercicio("USA_Housing.csv")
print("La media de Area Income es: " ,hola.calculo_media())
print("La desviacion de Area Income es: ",hola.calculo_desviacion())
print("La mediana de Area Income es: ",hola.mediana())
print("El percentil de Area Income 25 es:",hola.percentiles(25))
print("\n")
print("La media de Area House Age es: " ,hola.calculo_media_area())
print("La desviacion de Area House Age es: ",hola.calculo_desviacion_area())
print("La mediana de Area House Age es: ",hola.mediana_area())
print("El percentil de Area House Age 25 es:",hola.percentiles_area(25))
print("\n")
print("La media de Area Population es: " ,hola.calculo_media_area_population())
print("La desviacion de Area Population es: ",hola.calculo_desviacion_area_population())
print("La mediana de Area Population es: ",hola.mediana_area_population())
print("El percentil de Area Population 25 es:",hola.percentiles_area_population(25))
print("\n")
print("La media de Price es: " ,hola.calculo_media_precio())
print("La desviacion de Price es: ",hola.calculo_desviacion_precio())
print("La mediana de Price es: ",hola.mediana_precio())
print("El percentil de Price 25 es:",hola.percentiles_precio(25))
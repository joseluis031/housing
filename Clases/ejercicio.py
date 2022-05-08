import matplotlib.pyplot as plt
import pandas as pd
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
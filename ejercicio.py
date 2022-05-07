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

         
    
    
    
    
hola = Ejercicio("USA_Housing.csv")
print("La media es: " ,hola.calculo_media())
print("La desviacion es: ",hola.calculo_desviacion())
print("La mediana es: ",hola.mediana())
print("El percentil 25 es: ",hola.percentiles(25))
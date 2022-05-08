# housing
El link de este repositorio es:[GitHub](https://github.com/joseluis031/housing.git)


## 1 - Grafique las variables implicadas de las maneras que crea oportunas.
```
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
   ```
## 2 - Identifique si es necesaria una limpieza de datos y/o completar valores perdidos.
   Dentro del apartado 1, he incluido un bucle que me comprueba si hay datos perdidos o no.
   Tras realizar la comprobacion se puede ver que no hay datos perdidos
## 3 - Obtenga las correlaciones entre variables y analice si se pueden observar algunas relaciones interesantes.
   ```
   import pandas as pd




class Correlacion:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
    
    def correlaciones_edad_ingresos(self):
        print('Correlación Pearson(Edad/Ingresos): ', self.datos['Avg. Area House Age'].corr(self.datos['Avg. Area Income'], method='pearson'))
        print('Correlación spearman(Edad/Ingresos): ', self.datos['Avg. Area House Age'].corr(self.datos['Avg. Area Income'], method='spearman'))
        print('Correlación kendall(Edad/Ingresos): ', self.datos['Avg. Area House Age'].corr(self.datos['Avg. Area Income'], method='kendall')) 
    
    def correlaciones_precio_area(self):
        print('Correlación Pearson(Precio/Area): ', self.datos['Price'].corr(self.datos['Area Population'], method='pearson'))
        print('Correlación spearman(Precio/Area): ', self.datos['Price'].corr(self.datos['Area Population'], method='spearman'))
        print('Correlación kendall(Precio/Area): ', self.datos['Price'].corr(self.datos['Area Population'], method='kendall')) 
    
    def correlaciones_precio_ingresos(self):
        print('Correlación Pearson(Precio/Ingresos): ', self.datos['Price'].corr(self.datos['Avg. Area Income'], method='pearson'))
        print('Correlación spearman(Precio/Ingresos): ', self.datos['Price'].corr(self.datos['Avg. Area Income'], method='spearman'))
        print('Correlación kendall(Precio/Ingresos): ', self.datos['Price'].corr(self.datos['Avg. Area Income'], method='kendall')) 
        ```
## 4 - Grafique todo lo que considere oportuno.

## 5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.


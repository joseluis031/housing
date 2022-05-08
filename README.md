# housing
El link de este repositorio es:[GitHub](https://github.com/joseluis031/housing.git)


## 1 - Grafique las variables implicadas de las maneras que crea oportunas.
Este es el codigo que he utilizado para calcular las medidas que he considerado interesantes y para graficar los graficos que he considerado que tienen mas sentido
y son mas claros despues de probar todos los tipos posibles
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
   
   ```
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
```
## 2 - Identifique si es necesaria una limpieza de datos y/o completar valores perdidos.
   Dentro del apartado 1, he incluido un bucle que me comprueba si hay datos perdidos o no.
   Tras realizar la comprobacion se puede ver que no hay datos perdidos, en caso de que si hubiera valores perdidos, los completaria con el valor 0
## 3 - Obtenga las correlaciones entre variables y analice si se pueden observar algunas relaciones interesantes.
Este es el codigo que he utilizado para calcular 3 tipos diferentes de correlacion utilizando las variables de "Price","Area Population","Avg. Area Income" y "Avg. Area House Age"
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
He considerado interesante calcular el grafico relacionando todas las variables entre si mediante una matriz de correlacion que mas tarde he graficado
```
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




class Mas_cosas:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        
    def matriz_correlacion(self):
        # Se renombran las columnas para que sean más descriptivas
        self.datos.columns = ["Price", "Avg. Area Income", "Avg. Area House Age", "Avg. Area Number of Rooms",
                        "Avg. Area Number of Bedrooms", "Area Population", "Address"]
            
        # Variables numéricas
        self.datos = self.datos.select_dtypes(include=['float64', 'int'])
        # Matriz de correlación
        # ==============================================================================
        corr_matrix = self.datos.corr(method='pearson')
        print(corr_matrix)
    def matriz_grafica(self):
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
        corr_matrix = self.datos.corr(method='pearson')

        sns.heatmap(corr_matrix,
            annot     = True,
            cbar      = False,
            annot_kws = {"size": 8},
            vmin      = -1,
            vmax      = 1,
            center    = 0,
            cmap      = sns.diverging_palette(20, 220, n=200),
            square    = True,
            ax        = ax)

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation = 45,
            horizontalalignment = 'right',
        )

        ax.tick_params(labelsize = 10)
        plt.savefig('Graficos/matriz_correlacion.png', bbox_inches='tight')
        return plt.show()
```
## 5 - (Opcional) Aplique algún tipo de clustering o reducción de dimensionalidad e intente encontrar relaciones entre los datos.
He utilizado un clustering basado en la densidad de las variables que he considerado oportunas.
He utilizado DBSCAN evita el problema de de identificar formas arbitrarias siguiendo la idea de que, para que una observación forme parte de un cluster, tiene que haber un mínimo de observaciones vecinas dentro de un radio de proximidad y de que los clusters están separados por regiones vacías o con pocas observaciones.
```
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_blobs

# Gráficos
# ==============================================================================
from matplotlib import style
style.use('ggplot') or plt.style.use('ggplot')

# Preprocesado y modelado
# ==============================================================================
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import scale
from sklearn.metrics import silhouette_score

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')


class Clustering:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.datos.pop("Address")
    def cluster_precio(self):
        # Escalado de datos
        # ==============================================================================
        X = self.datos.drop(columns='Price').to_numpy()
        X_scaled = scale(X)
        
        # Modelo
        # ==============================================================================
        modelo_dbscan = DBSCAN(
                            eps          = 0.2,
                            min_samples  = 5,
                            metric       = 'euclidean',
                        )

        modelo_dbscan.fit(X=X_scaled)

        # Clasificación
        # ==============================================================================
        labels = modelo_dbscan.labels_

        fig, ax = plt.subplots(1, 1, figsize=(4.5, 4.5))

        ax.scatter(
            x = X[:, 0],
            y = X[:, 1], 
            c = labels,
            marker    = 'o',
            edgecolor = 'black'
        )

        # Los outliers se identifican con el label -1
        ax.scatter(
            x = X[labels == -1, 0],
            y = X[labels == -1, 1], 
            c = 'red',
            marker    = 'o',
            edgecolor = 'black',
            label = 'outliers'
        )

        ax.legend()
        ax.set_title('Clusterings precios');
        plt.savefig('Graficos/clustering_precio.png', bbox_inches='tight')
        plt.show()
        
    def cluster_ingresos(self):
            # Escalado de datos
            # ==============================================================================
            X = self.datos.drop(columns='Avg. Area Income').to_numpy()
            X_scaled = scale(X)
            
            # Modelo
            # ==============================================================================
            modelo_dbscan = DBSCAN(
                                eps          = 0.2,
                                min_samples  = 5,
                                metric       = 'euclidean',
                            )

            modelo_dbscan.fit(X=X_scaled)

            # Clasificación
            # ==============================================================================
            labels = modelo_dbscan.labels_

            fig, ax = plt.subplots(1, 1, figsize=(4.5, 4.5))

            ax.scatter(
                x = X[:, 0],
                y = X[:, 1], 
                c = labels,
                marker    = 'o',
                edgecolor = 'black'
            )

            # Los outliers se identifican con el label -1
            ax.scatter(
                x = X[labels == -1, 0],
                y = X[labels == -1, 1], 
                c = 'red',
                marker    = 'o',
                edgecolor = 'black',
                label = 'outliers'
            )

            ax.legend()
            ax.set_title('Clusterings ingresos');
            plt.savefig('Graficos/clustering_ingresos.png', bbox_inches='tight')
            plt.show()
            
    def cluster_edad(self):
            # Escalado de datos
            # ==============================================================================
            X = self.datos.drop(columns='Avg. Area House Age').to_numpy()
            X_scaled = scale(X)
            
            # Modelo
            # ==============================================================================
            modelo_dbscan = DBSCAN(
                                eps          = 0.2,
                                min_samples  = 5,
                                metric       = 'euclidean',
                            )

            modelo_dbscan.fit(X=X_scaled)

            # Clasificación
            # ==============================================================================
            labels = modelo_dbscan.labels_

            fig, ax = plt.subplots(1, 1, figsize=(4.5, 4.5))

            ax.scatter(
                x = X[:, 0],
                y = X[:, 1], 
                c = labels,
                marker    = 'o',
                edgecolor = 'black'
            )

            # Los outliers se identifican con el label -1
            ax.scatter(
                x = X[labels == -1, 0],
                y = X[labels == -1, 1], 
                c = 'red',
                marker    = 'o',
                edgecolor = 'black',
                label = 'outliers'
            )

            ax.legend()
            ax.set_title('Clusterings edad');
            plt.savefig('Graficos/clustering_edad.png', bbox_inches='tight')
            plt.show()
```
            
## Main
```
if __name__ == "__main__":  
    main = int(input("Que datos quieres ver?(1(calculos faciles), 2(graficas), 3(correlaciones),"
                     "4(matriz correlacion),5(Clustering):"))
    if main == 1:
        from Clases.ejercicio import Ejercicio
        
        hola = Ejercicio("USA_Housing.csv")
        print("La media de Area Income es: " ,hola.calculo_media())
        print("La desviacion de Area Income es: ",hola.calculo_desviacion())
        print("La mediana de Area Income es: ",hola.mediana())
        print("El 1 percentil de Area Income es:",hola.percentiles(25))
        print("El 3 percentil de Area Income es:",hola.percentiles(75))

        print("\n")
        print("La media de Area House Age es: " ,hola.calculo_media_area())
        print("La desviacion de Area House Age es: ",hola.calculo_desviacion_area())
        print("La mediana de Area House Age es: ",hola.mediana_area())
        print("El 1 percentil de Area House Age es:",hola.percentiles_area(25))
        print("El 3 percentil de Area House Age es:",hola.percentiles_area(75))

        print("\n")
        print("La media de Area Population es: " ,hola.calculo_media_area_population())
        print("La desviacion de Area Population es: ",hola.calculo_desviacion_area_population())
        print("La mediana de Area Population es: ",hola.mediana_area_population())
        print("El 1 percentil de Area Population es:",hola.percentiles_area_population(25))
        print("El 3 percentil de Area Population es:",hola.percentiles_area_population(75))

        print("\n")
        print("La media de Price es: " ,hola.calculo_media_precio())
        print("La desviacion de Price es: ",hola.calculo_desviacion_precio())
        print("La mediana de Price es: ",hola.mediana_precio())
        print("El 1 percentil de Price es:",hola.percentiles_precio(25))
        print("El 3 percentil de Price es:",hola.percentiles_precio(75))
        
    elif main == 2:
        from Clases.graficas import Graficas
        
        hola1 = Graficas("USA_Housing.csv")
        print(hola1.histograma_ingresos())
        print(hola1.histograma_edad())
        print(hola1.histograma_precios())
        print(hola1.grafica_dispersion())

        
    elif main == 3:
        from Clases.correlacion import Correlacion
        
        hola2 = Correlacion("USA_Housing.csv")
        print(hola2.correlaciones_edad_ingresos())
        print (hola2.correlaciones_precio_area())
        print(hola2.correlaciones_precio_ingresos())
        
    elif main == 4:
        from Clases.correlacion2 import Mas_cosas
        
        hola3 = Mas_cosas("USA_Housing.csv")
        print(hola3.matriz_grafica())     
        
    elif main == 5:
        from Clases.clustering import Clustering
        
        hola4 = Clustering("USA_Housing.csv")
        print(hola4.cluster_edad())
        print(hola4.cluster_ingresos())
        print(hola4.cluster_precio())   
        ```
Todas las graficas estan guardadas en formato png en una carpeta

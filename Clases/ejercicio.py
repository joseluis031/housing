import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
import numpy as np
import seaborn as sns

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

from sklearn.datasets import make_blobs

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
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
    def cluster(self):
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
        ax.set_title('Clusterings generados por DBSCAN');
        plt.savefig('Graficos/clustering_precio.png', bbox_inches='tight')

        plt.show()
        
hola5 = Clustering("USA_Housing.csv")
print(hola5.cluster())

 
 
# Importamos las librerias necesarias
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly as py
import plotly.io as pio
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn import preprocessing
from yellowbrick.cluster import KElbowVisualizer
import warnings
warnings.filterwarnings("ignore")
py.offline.init_notebook_mode(connected = True)
pio.renderers.default='browser'
class Clustering2:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.datos.pop("Address")
    def clus2(self):
        df = pd.read_csv('USA_Housing.csv')
        print('Dimensiones del df:', df.shape)
        #____________________________________________________________
        # Vamos a sacar informacion sobre los tipos y nulos del df
        df.drop_duplicates(inplace = True)
        tab_info=pd.DataFrame(df.dtypes).T.rename(index={0:'tipo de la columna'})
        tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()).T.rename(index={0:'campos nulos (cant)'}))
        tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.
                                rename(index={0:'campos nulos (%)'}))
        display(tab_info)
        #__________________
        #
        display(df[:5])
        df['Price'] = pd.get_dummies(df['Price']).values[:,0]
        plt.style.use('fivethirtyeight')
        plt.figure(1 , figsize = (15 , 6))
        n = 0 
        for x in ['Price' , 'Avg. Area Income' , 'Avg. Area House Age']:
            n += 1
            plt.subplot(1 , 3 , n)
            plt.subplots_adjust(hspace =0.5 , wspace = 0.5)
            sns.distplot(df[x] , bins = 20)
            plt.title('Distplot of {}'.format(x))
        X = df.copy()
        X.drop(labels=['Price'], axis=1, inplace=True)
        X1 = preprocessing.normalize(X)
        model = KMeans()
        visualizer = KElbowVisualizer(model, k=(1,12))
        visualizer.fit(X1)        # Entrenamos con los datos
        visualizer.show()        # Renderizamos la imagen
        plt.show()
        
hola5 = Clustering2("USA_Housing.csv")
print(hola5.clus2())      
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
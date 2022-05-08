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
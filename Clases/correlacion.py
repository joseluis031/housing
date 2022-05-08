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

if __name__ == "__main__":  
    main = int(input("Que datos quieres ver?(1(calculos faciles), 2(graficas), 3(correlaciones),"
                     "4(matriz correlacion):"))
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
        from Clases.ejercicio import Graficas
        
        hola1 = Graficas("USA_Housing.csv")
        print(hola1.histograma_ingresos())
        print(hola1.histograma_edad())
        print(hola1.histograma_precios())
        
    elif main == 3:
        from Clases.ejercicio import Correlacion
        
        hola2 = Correlacion("USA_Housing.csv")
        print(hola2.correlaciones_edad_ingresos())
        print (hola2.correlaciones_precio_area())
        print(hola2.correlaciones_precio_ingresos())
        
    elif main == 4:
        from Clases.ejercicio import Mas_cosas
        
        hola3 = Mas_cosas("USA_Housing.csv")
        print(hola3.matriz_grafica())        

#from pruebas import pruebas_codigo_estudiante
import csv
import pandas as pd


def solucion():
    filename = 'FB.csv'
    df = pd.read_csv(filename, float_precision='round_trip')
    df.rename(columns={'Date': 'Fecha'}, inplace=True)
    df['Mean-Min-Max'] = df.iloc[:, 2:4].mean(axis=1)
    concepto = []
    concep = ''
    for i in df['Mean-Min-Max']:
        if i < 239:
            concep = 'MUY BAJO'
        elif 239 <= i < 265:
            concep = 'BAJO'
        elif 265 <= i < 291:
            concep = 'MEDIO'
        elif 291 <= i < 317:
            concep = 'ALTO'
        elif i >= 317:
            concep = 'MUY ALTO'
        concepto.append(concep)
    df = df.assign(Concepto=concepto)
    idx_lowest_mean = df['Mean-Min-Max'].idxmin()
    idx_highest_mean = df['Mean-Min-Max'].idxmax()
    lowest_mean = float(df['Mean-Min-Max'].min())
    highest_mean = float(df['Mean-Min-Max'].max())
    date_lowest_mean = df.iloc[idx_lowest_mean, 0]
    date_highest_mean = df.iloc[idx_highest_mean, 0]
    analisis = df[['Fecha', 'Mean-Min-Max', 'Concepto']]
    analisis_archivo = pd.DataFrame(analisis)
    analisis_archivo.to_csv('analisis_archivo.csv', sep='\t', index=False)
    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean
       


solucion()

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)
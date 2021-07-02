import pandas as pd

filename = 'FB.CSV'

df = pd.read_csv(filename)
hlmean = list((df['High'] + df['Low'])/2)
df = df.assign(mean=hlmean)
df = df.round({'mean': 9})
df.rename(columns={'mean': 'Mean-Min-Max'}, inplace=True)
# df['Mean-Min-Max'] = df.iloc[:, 2:4].mean(axis=1)
concepto = []
for i in df['Mean-Min-Max']:
    if i < 239:
        concep = 'MUY BAJO'
        concepto.append(concep)
    elif 239 <= i < 265:
        concep = 'BAJO'
        concepto.append(concep)
    elif 265 <= i < 291:
        concep = 'MEDIO'
        concepto.append(concep)
    elif 291 <= i < 317:
        concep = 'ALTO'
        concepto.append(concep)
    elif i >= 317:
        concep = 'MUY ALTO'
        concepto.append(concep)
df = df.assign(Concepto=concepto)
df.rename(columns={'Date': 'Fecha'}, inplace=True)
analisis = df[['Fecha', 'Mean-Min-Max', 'Concepto']]
analisis_archivo = pd.DataFrame(analisis)
idx_lowest_mean = analisis_archivo['Mean-Min-Max'].idxmin()
idx_highest_mean = analisis_archivo['Mean-Min-Max'].idxmax()
lowest_mean = float(analisis_archivo['Mean-Min-Max'].min())
highest_mean = float(analisis_archivo['Mean-Min-Max'].max())
highest_mean = round(highest_mean, 8)
date_lm = analisis_archivo.iloc[idx_lowest_mean, 0]
date_hm = analisis_archivo.iloc[idx_highest_mean, 0]
print(date_hm)
print(type(date_hm))
print(type(highest_mean))
print(highest_mean)
print(date_lm)
print(lowest_mean)
analisis_archivo.to_csv('analisis_archivo.csv', sep='\t', index=False)

# d_date = df['Date']
# d_hlmean = (df['High'] + df['Low'])/2
# date = pd.DataFrame(d_date, columns=['Date'])
# date_mean = date.assign(Mean=d_hlmean)







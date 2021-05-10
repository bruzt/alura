import pandas
import matplotlib.pyplot as pyplot
import seaborn

seaborn.set()

def main():

    dataCSV = './dados_experimentos.zip'
    resultCSV = './dados_resultados.csv'

    dataframe = pandas.read_csv(dataCSV, compression = 'zip')
    resultDataframe = pandas.read_csv(resultCSV)

    columnsMap = {
        'droga': 'composto'
    }
    
    dataframe.rename(columns=columnsMap, inplace=True)

    #print(resultDataframe['11-beta-hsd1_inhibitor'].unique())

    #print(resultDataframe.info())

    #print(resultDataframe.select_dtypes('int64').sum().sort_values(ascending=False))
    #print(resultDataframe.drop('id', axis=1).sum().sort_values(ascending=False)) # .drop('id', axis=1) remove coluna

    """
    for column in resultDataframe.columns:
        print(column.split('_')[-1])
    """

    #print(resultDataframe.sum(axis=1)) # .sum(axis=1) soma linhas

    dataframe['com_controle'] = dataframe['tratamento'] == 'com_controle'
    dataframe['com_droga'] = dataframe['tratamento'] == 'com_droga'

    dataframe['24h'] = dataframe['tempo'] == 24
    dataframe['48h'] = dataframe['tempo'] == 48
    dataframe['72h'] = dataframe['tempo'] == 72

    dataframe['d1'] = dataframe['dose'] == 'D1'
    dataframe['d2'] = dataframe['dose'] == 'D2'

    dataframe = dataframe.drop(['tratamento', 'tempo', 'dose'], axis=1)

    resultDataframe['qtd_moa'] = resultDataframe.sum(axis=1) # moa = mecanismo de ação
    resultDataframe['moa_ativo'] = resultDataframe['qtd_moa'] != 0

    mergedData = pandas.merge(dataframe, resultDataframe[['id', 'qtd_moa', 'moa_ativo']], on='id')

    #print(mergedData.query('com_controle == True')['moa_ativo'].value_counts())
    #print(mergedData.query('com_droga == True')['moa_ativo'].value_counts())

    compounds = mergedData['composto'].value_counts().index[:10]

    fig = pyplot.figure(figsize=(10, 8))
    ax = seaborn.boxplot(data=mergedData.query('composto in @compounds'), x='composto', y='g-0', hue='moa_ativo')
    ax.set_title('Boxplot composto - G-0')
    fig.add_subplot(ax)
    pyplot.show()

if __name__ == '__main__':
    main()

# g = expressão génica
# c = tipo celular
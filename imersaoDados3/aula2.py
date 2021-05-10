import pandas
import matplotlib.pyplot as pyplot
import seaborn

seaborn.set()

def main():

    dataUrl = './dados_experimentos.zip'

    data = pandas.read_csv(dataUrl, compression = 'zip')

    columnsMap = {
        'droga': 'composto'
    }
    
    data.rename(columns=columnsMap, inplace=True)

    """
    compoundIndexes = data['composto'].value_counts().index[0:5] # [0:5] = slice(0, 5)

    ax = seaborn.countplot(x='composto', data=data.query('composto in @compoundIndexes'), order=compoundIndexes)
    ax.set_title('Top 5 compostos')
    pyplot.show()
    """

    """
    print(data['g-0'].min())
    print(data['g-0'].max())
    print(data['g-0'].mean())
    """

    #print(data['g-0'].describe())

    """
    fig1 = pyplot.figure(figsize=(10, 8))
    fig1.add_subplot(data['g-0'].hist(bins=100))

    fig2 = pyplot.figure(figsize=(10, 8))
    fig2.add_subplot(data['g-19'].hist(bins=100))
    pyplot.show()
    """

    """
    fig1 = pyplot.figure(figsize=(10, 8))
    ax1 = seaborn.histplot(data=data['g-0'])
    ax1.set_title('G-0')
    fig1.add_subplot(ax1)

    fig2 = pyplot.figure(figsize=(10, 8))
    ax2 = seaborn.histplot(data=data['g-19'])
    ax2.set_title('G-19')
    fig2.add_subplot(ax2)
    pyplot.show()
    """

    #data.loc[:, 'g-0':'g-771'].describe().T.hist(bins=100) # .T = rotaciona o grafico, linhas viram colunas, colunas viram linhas

    """
    fig = pyplot.figure(figsize=(10, 8))
    ax = seaborn.histplot(data=data.loc[:, 'g-0':'g-771'].describe().T['mean'], bins=100)
    ax.set_title('Genética')
    fig.add_subplot(ax)
    
    fig2 = pyplot.figure(figsize=(10, 8))
    ax2 = seaborn.histplot(data=data.loc[:, 'c-0':'c-99'].describe().T['mean'], bins=50)
    ax2.set_title('Linhagem celular')
    fig2.add_subplot(ax2)
    pyplot.show()
    """
    
    fig = pyplot.figure(figsize=(10, 8))
    ax = seaborn.boxplot(x='tratamento', y='g-0', data=data)
    ax.set_title('Boxplot G-0')
    fig.add_subplot(ax)
    pyplot.show()

if __name__ == '__main__':
    main()

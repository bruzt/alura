import pandas
import matplotlib.pyplot as pyplot
import seaborn
import numpy

seaborn.set()

def main():

    dataUrl = './dados_experimentos.zip'

    data = pandas.read_csv(dataUrl, compression = 'zip')

    columnsMap = {
        'droga': 'composto'
    }
    
    data.rename(columns=columnsMap, inplace=True)

    #print(data.head())

    #print(pandas.crosstab(data['dose'], data['tempo']))

    #print(pandas.crosstab([data['dose'], data['tempo']], data['tratamento']))

    #print(pandas.crosstab([data['dose'], data['tempo']], data['tratamento'], normalize=True))

    #print(pandas.crosstab([data['dose'], data['tempo']], data['tratamento'], normalize='index'))

    #print(pandas.crosstab([data['dose'], data['tempo']], data['tratamento'], values=data['g-0'], aggfunc='mean'))

    #print(data.groupby(["dose", "tempo", "tratamento"])['g-0'].count())

    """
    fig = pyplot.figure(figsize=(10, 8))
    ax = seaborn.scatterplot(x='g-0', y='g-8', data=data)
    ax.set_title('Dispersão G1-G8')
    fig.add_subplot(ax)
    pyplot.show()
    """

    lineKws = {
        'color': 'red'
    }

    """
    ax = seaborn.lmplot(x='g-0', y='g-8', data=data, line_kws=lineKws, height=8).ax
    ax.set_title('Dispersão G1-G8')
    pyplot.show()
    """

    """
    seaborn.lmplot(x='g-0', y='g-8', data=data, col='tratamento', line_kws=lineKws, height=8).axes
    pyplot.show()
    """

    """
    seaborn.lmplot(x='g-0', y='g-8', data=data, col='tratamento', row='tempo', line_kws=lineKws).axes
    pyplot.show()
    """

    #print(data.loc[:, 'g-0':'g-771'].corr())

    correlation = data.loc[:, 'g-0':'g-50'].corr()
    #correlation = data.loc[:, 'c-0':'c-50'].corr()

    mask = numpy.triu(numpy.ones_like(correlation, dtype=bool))

    cmap = seaborn.diverging_palette(230, 20, as_cmap=True)

    cbarKws = {
        'shrink': .5
    }

    pyplot.subplots(figsize=(15, 13))
    seaborn.heatmap(
        correlation, 
        mask=mask, 
        cmap=cmap, 
        center=0, 
        #vmin=-1, 
        #vmax=1, 
        square=True, 
        linewidths=.5, 
        cbar_kws=cbarKws,
        #annot=True
    )
    pyplot.show()
    


if __name__ == '__main__':
    main()

# g = expressão génica
# c = tipo celular
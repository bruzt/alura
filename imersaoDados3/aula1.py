import pandas
import matplotlib.pyplot as pyplot

def main():

    #dataUrl = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'
    dataUrl = './dados_experimentos.zip'

    data = pandas.read_csv(dataUrl, compression = 'zip')

    #print(data.shape) # linhas, colunas
    #print(data.head()) 

    #print(data['tratamento'].unique())

    #print(data['tempo'].unique())

    #print(data['dose'].unique())

    #print(data['droga'].unique(), '-', len(data['droga'].unique()))

    #print(data.tail())

    #print(data['dose'].value_counts(normalize = True))

    #data['tratamento'].value_counts().plot(kind = 'pie')
    #pyplot.show()
    
    #data['tempo'].value_counts().plot(kind = 'bar', title = 'tempo')
    #pyplot.show()

    data['tempo'].value_counts().plot.bar()
    pyplot.show()

    #filtered_data = data[data['g-0'] > 0]
    #print(filtered_data.head())

if __name__ == '__main__':
    main()

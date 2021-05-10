import pandas
import matplotlib.pyplot as pyplot
import seaborn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as trainTestSplit
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score as accuracyScore
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

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

    dataframe = pandas.get_dummies(dataframe, columns=['tratamento', 'tempo', 'dose']) # cria novas colunas com os resultados e seuas valores são 0 e 1 (falso ou verdadeiro)

    resultDataframe['qtd_moa'] = resultDataframe.sum(axis=1) # moa = mecanismo de ação
    resultDataframe['moa_ativo'] = resultDataframe['qtd_moa'] != 0

    mergedData = pandas.merge(dataframe, resultDataframe[['id', 'qtd_moa', 'moa_ativo']], on='id')

    x = mergedData.drop(['id', 'composto', 'qtd_moa', 'moa_ativo'], axis=1)
    y = mergedData['moa_ativo']

    trainingX, testX, trainingY, testY =  trainTestSplit(x, y, train_size=0.8, test_size=0.2, stratify=y)

    tested=[]
    size = range(1,10)
    for i in size:

        forestModel = RandomForestClassifier(max_depth=i)
        forestModel.fit(trainingX, trainingY)

        testScore = forestModel.score(testX, testY)
        #print(f'Acurácia arvore de descisão nivel {i}: ', testScore)
        tested.append(testScore)

    fig = pyplot.figure(figsize=(10, 8))
    ax = seaborn.lineplot(x=size, y=tested, label='Dados teste')
    ax.set_title('Taxa de acerto da floresta randomica por profundidade')
    ax.set(xlabel='Profundidade', ylabel='Taxa de acerto')
    fig.add_subplot(ax)
    pyplot.show()

if __name__ == '__main__':
    main()

# g = expressão génica
# c = tipo celular
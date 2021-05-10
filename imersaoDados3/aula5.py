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

    """
    dataframe['com_controle'] = dataframe['tratamento'] == 'com_controle'
    dataframe['com_droga'] = dataframe['tratamento'] == 'com_droga'

    #dataframe['com_controle'] = dataframe['com_controle'].astype(int) # transforma True em 1 e False em 0
    #dataframe['com_droga'] = dataframe['com_droga'].astype(int)

    dataframe['24h'] = dataframe['tempo'] == 24
    dataframe['48h'] = dataframe['tempo'] == 48
    dataframe['72h'] = dataframe['tempo'] == 72

    dataframe['d1'] = dataframe['dose'] == 'D1'
    dataframe['d2'] = dataframe['dose'] == 'D2'
    """

    dataframe = pandas.get_dummies(dataframe, columns=['tratamento', 'tempo', 'dose'])

    resultDataframe['qtd_moa'] = resultDataframe.sum(axis=1) # moa = mecanismo de ação
    resultDataframe['moa_ativo'] = resultDataframe['qtd_moa'] != 0

    mergedData = pandas.merge(dataframe, resultDataframe[['id', 'qtd_moa', 'moa_ativo']], on='id')

    """
    x = mergedData.select_dtypes('float64') # Seleciona todos as colunas que tem float com dado, nesse caso todas as expressções génicas (g) e tipos celulares (c)
    y = mergedData['moa_ativo']

    trainingX, testX, trainingY, testY =  trainTestSplit(x, y, train_size=0.8, test_size=0.2, stratify=y) # divide a base em 4 para treino e teste, test_size=0.2 = 20% para teste e 80% para treino

    logisticRegression = LogisticRegression(max_iter=1000)
    logisticRegression.fit(trainingX, trainingY)
    print('Acurácia regressão logistica: ', logisticRegression.score(testX, testY))

    dummyModel = DummyClassifier(strategy='most_frequent')
    dummyModel.fit(trainingX, trainingY)
    dummyPrediction = dummyModel.predict(testX)
    print('Acurácia dummy: ', accuracyScore(testY, dummyPrediction))
    """

    """
    tested=[]
    trained = []
    for i in range(1, 16):
        treeModel = DecisionTreeClassifier(max_depth=i)
        treeModel.fit(trainingX, trainingY)

        testScore = treeModel.score(testX, testY)
        print(f'Acurácia arvore de descisão nivel {i}: ', testScore)
        tested.append(testScore)

        trainedScore = treeModel.score(trainingX, trainingY)
        print(f'Acurácia arvore de descisão nivel {i} - dados trainado: ', trainedScore)
        trained.append(trainedScore)

    """

    """
        fig, ax = pyplot.subplots(figsize=(15, 10), facecolor='k')
        tree.plot_tree(
            treeModel,
            ax=ax,
            fontsize=10,
            rounded=True,
            filled=True,
            feature_names=trainingX.columns,
            class_names=['Não Ativado', 'Ativado'],
        )
        pyplot.show()
    """

    """
    fig = pyplot.figure(figsize=(10, 8))
    ax1 = seaborn.lineplot(x=range(1,16), y=tested, label='Dados teste')
    ax2 = seaborn.lineplot(x=range(1,16), y=trained, label='Dados treino')
    ax1.set_title('Comparativo usando os dados de teste e os dados de treino')
    fig.add_subplot(ax1)
    fig.add_subplot(ax2)
    pyplot.show()
    """

    print(mergedData.head())

    x = mergedData.drop(['id', 'composto', 'qtd_moa', 'moa_ativo'], axis=1)
    y = mergedData['moa_ativo']

    trainingX, testX, trainingY, testY =  trainTestSplit(x, y, train_size=0.8, test_size=0.2, stratify=y)

    forestModel = RandomForestClassifier()
    forestModel.fit(trainingX, trainingY)

    score = forestModel.score(testX, testY)
    print(f'Acurácia floresta de descisão: ', score)


if __name__ == '__main__':
    main()

# g = expressão génica
# c = tipo celular
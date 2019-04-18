from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def training(file, test):

    # ------ Training -------
    data = pd.read_csv(file)
    X = data.iloc[:, 1:-1]
    y = data.iloc[:, 0]

    d = defaultdict(LabelEncoder)

    Xfit = X.apply(lambda x: d[x.name].fit_transform(x))

    le_y = LabelEncoder()
    yfit = le_y.fit_transform(y)

    ohc = defaultdict(OneHotEncoder)
    final = pd.DataFrame()

    for i in range(22):
        # transforming the columns using One hot encoder
        Xtemp_i = pd.DataFrame(ohc[Xfit.columns[i]].fit_transform(
            Xfit.iloc[:, i:i+1]).toarray())

        # Naming the columns as per label encoder
        ohc_obj = ohc[Xfit.columns[i]]
        labelEncoder_i = d[Xfit.columns[i]]
        Xtemp_i.columns = Xfit.columns[i]+"_" + \
            labelEncoder_i.inverse_transform(ohc_obj.active_features_)

        # taking care of dummy variable trap
        X_ohc_i = Xtemp_i.iloc[:, 1:]

        # appending the columns to final dataframe
        final = pd.concat([final, X_ohc_i], axis=1)

    classifier = KNeighborsClassifier(n_neighbors=1, p=2, metric='minkowski')
    classifier.fit(final, yfit)

    # ------ End of Training -------

    test = pd.read_csv(test)

    X = test.iloc[:, :-1]

    # d = defaultdict(LabelEncoder)

    Xfit = X.apply(lambda x: d[x.name].transform(x))

    # ohc = defaultdict(OneHotEncoder)
    res = pd.DataFrame()

    for i in range(22):
        # transforming the columns using One hot encoder
        Xtemp_i = pd.DataFrame(ohc[Xfit.columns[i]].transform(
            Xfit.iloc[:, i:i+1]).toarray())

        # Naming the columns as per label encoder
        ohc_obj = ohc[Xfit.columns[i]]
        labelEncoder_i = d[Xfit.columns[i]]
        Xtemp_i.columns = Xfit.columns[i]+"_" + \
            labelEncoder_i.inverse_transform(ohc_obj.active_features_)

        # taking care of dummy variable trap
        X_ohc_i = Xtemp_i.iloc[:, 1:]

        # appending the columns to final dataframe
        res = pd.concat([res, X_ohc_i], axis=1)

    y_pred = classifier.predict(res)
    df = pd.DataFrame(columns=['class'])
    for i in range(len(y_pred)):
        if(y_pred[i] == 1):
            df.loc[i] = 'p'
            # e_cnt = e_cnt + 1
        elif(y_pred[i] == 0):
            df.loc[i] = 'e'
            # p_cnt = p_cnt + 1

    df['Id'] = test['Id'].values
    df.to_csv('prediction.csv', index=False)


if __name__ == "__main__":
    training('train.csv', 'test.csv')

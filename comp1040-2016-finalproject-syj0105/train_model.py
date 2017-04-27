import numpy as np
import pandas as pd
from scipy.stats import skew
from sklearn.linear_model import LassoCV
import sklearn.cross_validation as cv
import matplotlib.pyplot as plt


def readData(fn):
    # read the file
    # remove the first id and last price to get the feature data
    df = pd.read_csv(fn)

    features = df.loc[:, 'MSSubClass':'SaleCondition']

    return df, features


def transformFeatures(features, features_test):
    all_features = pd.concat([features, features_test])

    names = []

    # for every feature
    for feature in all_features:
        # test if its numerical
        if all_features[feature].dtype != "object":
            # test if it is too skew
            if skew(features[feature].dropna()) > 0.8:
                names.append(feature)
                # print('skewed')
                # print(feature)
                # log transformation
                all_features[feature] = np.log1p(features[feature])

    # convert categority to indicator variable
    all_features = pd.get_dummies(all_features)

    # print(all_features.head(10))
    # replace empty value with mean
    all_features = all_features.fillna(all_features.mean())

    # split to train and test feature
    features = all_features[:features.shape[0]]
    features_test = all_features[features.shape[0]:]

    return features, features_test


def modelTraining(features, target):
    linear_model = LassoCV(alphas=[0.00001, 0.0001, 0.001, 0.01, 0.1], max_iter=10000).fit(features, target)

    # print selected alpha
    # print(linear_model.alpha_)

    # the cross validation score
    crossScore = cv.cross_val_score(linear_model, features, target, scoring="mean_squared_error")

    return linear_model, linear_model.alpha_, crossScore


def getTopCoefficient(linear_model, features):
    model_coefficient = pd.Series(linear_model.coef_, index=features.columns)

    # non-zero coefficient features are selected
    numSelect = sum(model_coefficient != 0)
    removed = model_coefficient.shape[0] - numSelect
    print("select %d variables and remove %d variables" % (numSelect, removed))

    # smallest 10
    neg10 = model_coefficient.sort_values(ascending=True).head(10)
    # largest 10
    pos10 = model_coefficient.sort_values(ascending=False).head(10)

    # print(neg10)
    # print(pos10)

    topCoefficent = pd.concat([pos10, neg10])

    return topCoefficent


def modelTesting(linear_model, features, features_test):
    # prediction on train data
    train_pred = np.expm1(linear_model.predict(features))
    pd.DataFrame({"pred": train_pred, "correct": df["SalePrice"]}).to_csv("compare.csv",
                                                                          index=False, header=True)
    # compute the relative error
    meanRela = np.zeros_like(train_pred)
    for i in range(meanRela.shape[0]):
        meanRela[i] = np.abs(train_pred[i] - df["SalePrice"][i]) / df["SalePrice"][i]

    # print the mean relative error
    print(np.mean(meanRela))

    # save train prediction to file
    outFrameTrain = pd.DataFrame({"id": df.Id, "SalePrice": train_pred})
    outFrameTrain.to_csv("train_pred.csv", index=False, header=True)

    # do prediction on test data and save to file
    test_pred = np.expm1(linear_model.predict(features_test))
    outFrame = pd.DataFrame({"id": df_test.Id, "SalePrice": test_pred})
    outFrame.to_csv("test_pred.csv", index=False, header=True)


if __name__ == '__main__':
    df, features = readData('train.csv')
    df_test, features_test = readData('test.csv')

    # log transform skewed features, convert category to indicator variable
    # replace empty value by mean
    features, features_test = transformFeatures(features, features_test)

    # transfom sale price
    target = np.log1p(df["SalePrice"])

    # example transformation to let data more approximate to normal distribution
    LotArea = pd.DataFrame({"LotArea": df["LotArea"], "log(LotArea + 1)": np.log1p(df["LotArea"])})
    LotArea.hist()

    # train model
    linear_model, alpha, crossScore = modelTraining(features, target)

    # print selected alpha
    print('alpha: ' + str(alpha))
    print('cross score: ' + str(crossScore))

    # show features with top coefficient which have the biggest influence on price
    topCoefficent = getTopCoefficient(linear_model, features)

    # plot the coefficient bar graph
    print(topCoefficent)
    plt.figure()
    topCoefficent.plot(kind="barh")
    plt.title("Coefficients")
    plt.xlabel("Model Coefficient")
    plt.show()

    # model prediction on train and test data
    modelTesting(linear_model, features, features_test)


import unittest

from train_model import *


class TestTrainModel(unittest.TestCase):
    def test_readData(self):
        df, features = readData('train.csv')

        # test read right number of rows and columns
        self.assertEqual(df.shape, (1460, 81))
        self.assertEqual(features.shape, (1460, 79))

        self.assertEqual(features['SaleCondition'][0], 'Normal')
        self.assertEqual(features['Neighborhood'][0], 'CollgCr')

    def test_transformFeatures(self):
        df, features = readData('train.csv')
        df_test, features_test = readData('test.csv')

        nf, nf_test = transformFeatures(features, features_test)

        self.assertTrue(features.shape[0] == nf.shape[0])

        self.assertTrue(features_test.shape[0] == nf_test.shape[0])

        self.assertTrue(features.shape[1] < nf.shape[1])

        self.assertTrue(features_test.shape[1] < nf_test.shape[1])

        self.assertEqual(nf['Neighborhood_CollgCr'][0], 1)
        self.assertEqual(nf['SaleCondition_Normal'][0], 1)

    def test_train_model(self):
        df, features = readData('train.csv')
        df_test, features_test = readData('test.csv')

        # log transform skewed features, convert categority to indicator variable,
        # replace empty value by mean
        features, features_test = transformFeatures(features, features_test)

        # transfom sale price
        target = np.log1p(df["SalePrice"])
        linear_model, alpha, crossScore = modelTraining(features, target)

        for i in range(len(crossScore)):
         self.assertTrue(crossScore[i] < 0.05)

    def test_get_top_coefficient(self):
        df, features = readData('train.csv')
        df_test, features_test = readData('test.csv')

        # log transform skewed features, convert categority to indicator variable,
        # replance empty value by mean
        features, features_test = transformFeatures(features, features_test)

        # transfom sale price
        target = np.log1p(df["SalePrice"])
        linear_model, alpha, crossScore = modelTraining(features, target)
        topCoefficent = getTopCoefficient(linear_model, features)

        self.assertEqual(len(topCoefficent), 20)

        self.assertTrue(topCoefficent['GrLivArea'] > 0)

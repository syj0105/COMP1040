import pandas as pd

df = pd.read_csv('train.csv')

import matplotlib.pyplot as plt

neighborhoodNames = list(set(df['Neighborhood']))
neiPrices = [df.loc[df['Neighborhood'] == name]['SalePrice'] for name in neighborhoodNames]

# plot house price of different neighborhood
plt.figure(figsize=(18, 6))
plt.boxplot(neiPrices, labels=neighborhoodNames)
plt.xlabel("Neighborhood")
plt.ylabel('Sale Price')

# plot house price of different HouseStyle
styleNames = list(set(df['HouseStyle']))
stylePrices = [df.loc[df['HouseStyle'] == name]['SalePrice'] for name in styleNames]
# plt.set_aspect(1.5)
plt.figure(figsize=(8, 6))
plt.boxplot(stylePrices, labels=styleNames)
plt.xlabel("Style")
plt.ylabel('Sale Price')

# plot house price histogram
plt.figure()
plt.hist(df['SalePrice'], 100, normed=1, facecolor='green', alpha=0.5)
plt.xlabel("Sale Price")

# plot house price box plot
plt.figure()
plt.boxplot(df['SalePrice'], labels=["Sale Price"])

plt.show()
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
style.use('ggplot')

df_train = pd.read_csv('data/train.csv')

surviveds =  df_train['Survived']

sexes = df_train['Sex']

#df_train['Gender'] = 2
#df_train['Gender'].loc[(df_train['Sex']=='male')] = 1

gender = df_train['Gender'] = df_train['Sex'].map({'female': 2, 'male': 1}).astype(int)
sumMale = df_train['Gender'].loc[(df_train['Gender'] == 1)].sum()
sumFemale = df_train['Gender'].loc[(df_train['Gender'] == 2)].sum()/2

sumMaleSurvived = df_train['Gender'].loc[(df_train['Gender'] == 1) & (df_train['Survived'] == 1)].sum()
sumFemaleSurvived = df_train['Gender'].loc[(df_train['Gender'] == 2) & (df_train['Survived'] == 1)].sum()/2

list1 = [sumMale, sumFemale]
list2 = [sumMaleSurvived, sumFemaleSurvived]
# print df_train
#


temp3 = pd.crosstab([df_train['Pclass'], df_train['Sex']], df_train['Survived'].astype(bool))
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)
plt.show()

# from mpl_toolkits.mplot3d import  axes3d
# import numpy as np
# def get_test_data(delta=0.05):
#
#     from matplotlib.mlab import  bivariate_normal
#     x = y = np.arange(-3.0, 3.0, delta)
#     X, Y = np.meshgrid(x, y)
#
#     Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
#     Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
#     Z = Z2 - Z1
#
#     X = X * 10
#     Y = Y * 10
#     Z = Z * 500
#     return X, Y, Z
#
#
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# x, y, z = axes3d.get_test_data(0.05)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2)
#
# plt.show()
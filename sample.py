from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

# diabetes_X = diabetes.data[:, np.newaxis, 2]   # one feature
diabetes_X = diabetes.data #more than one feature

diabetes_X_train = diabetes_X[:-30]   #features
diabetes_X_test = diabetes_X[-30:]

diabetes_Y_train = diabetes.target[:-30]  #labels
diabetes_Y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)
                                                      #test            #predicted
print("mean square average error is :", mean_squared_error(diabetes_Y_test, diabetes_y_predicted))

print("weights :" ,model.coef_)
print("intercept: ", model.intercept_)
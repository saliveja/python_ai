import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

# Binarize data. All values above 2.1 is 1.  
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data) 
print("\nBinarized data:\n", data_binarized) 

# Print mean and standard deviation 
print("\nBEFORE:") 
print("Mean =", input_data.mean(axis=0)) 
print("Std deviation =", input_data.std(axis=0))

# Remove mean.
data_scaled = preprocessing.scale(input_data) 
print("\nAFTER:") 
print("Mean =", data_scaled.mean(axis=0)) 
print("Std deviation =", data_scaled.std(axis=0))

#In the latter, the standard deviation is marginal in comparison with 'before':

#BEFORE:
#Mean = [ 3.775 -1.15  -1.3  ]
#Std deviation = [3.12039661 6.36651396 4.0620192 ]

#AFTER:
#Mean = [1.11022302e-16 0.00000000e+00 2.77555756e-17]

# maximum value is 1 and all the other values are relative to this value
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1)) 
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data) 
print("\nMin max scaled data:\n", data_scaled_minmax) 

# Normalize data 
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1') 
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2') 
print("\nL1 normalized data:\n", data_normalized_l1) 
print("\nL2 normalized data:\n", data_normalized_l2)
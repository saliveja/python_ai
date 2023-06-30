import numpy as np
from sklearn import preprocessing

input_labels = ["red", "black", "red", "green", "black", "yellow", "white"]

# converting list items to numbers
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel mapping:")

# printing each list item with a number
for i, item in enumerate(encoder.classes_):
    print(f"{item} --> {i}")

# applying above to a new list
test_labels = ["green", "red", "black"]
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels) 
print("Encoded values =", list(encoded_values))

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))

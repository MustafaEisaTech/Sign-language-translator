import pickle
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_dict = pickle.load(open('./data.pickle', 'rb'))
#debugging purposes
#print(len(data_dict['data']), len(data_dict['labels']))
data = np.asarray(data_dict['data'])
labels = np.array(data_dict['labels'])
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42, shuffle=True, stratify=labels
)

#debugging purposes
#print(f"x_train shape: {len(x_train)}, y_train shape: {len(y_train)}")
#print(f"x_test shape: {len(x_test)}, y_test shape: {len(y_test)}")


#print(f"Data shape: {data.shape}")
#print(f"Labels shape: {labels.shape}")

#x_train, y_train, x_test, y_test = train_test_split(data, labels ,test_size=0.2, random_state=42, shuffle=True, stratify=labels)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_pred= y_predict, y_true=y_test)

print(f'{score * 100}% of samples were classified correctly !')

f = open('model.p', 'wb')
pickle.dump({'model':model}, f)
f.close()
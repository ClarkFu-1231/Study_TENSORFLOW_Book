import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
np.random.seed(10)

df= pd.read_csv("./diabetes.csv")
dataset= df.values
np.random.shuffle(dataset)

X= dataset[:, 0:8]
Y= dataset[:, 8]

'''定義模型'''
model= Sequential()
model.add(Dense(10, input_shape=(8, ), activation= "relu"))
model.add(Dense(8, activation= "relu"))
model.add(Dense(1, activation= "sigmoid"))
model.summary()

'''編譯模型'''
model.compile(loss="binary_crossentropy", optimizer="sgd",
              metrics=["accuracy"])

'''訓練模型'''
model.fit(X, Y, epochs=150, batch_size=10)

'''評估模型'''
loss, accuracy= model.evaluate(X, Y)
print("準確度={:.2f}".format(accuracy))


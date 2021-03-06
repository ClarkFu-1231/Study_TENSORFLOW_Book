'''在輸出層使用softmax啟動函數'''
import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
np.random.seed(10)

df= pd.read_csv("./diabetes.csv")
dataset= df.values
np.random.shuffle(dataset)

X= dataset[:, 0:8]
Y= dataset[:, 8]

Y= to_categorical(Y)

'''定義模型'''
model= Sequential()
model.add(Dense(10, input_shape=(8, ), activation= "relu"))
model.add(Dense(8, activation= "relu"))
model.add(Dense(2, activation= "softmax"))#在輸出層使用softmax啟動函數
model.summary()

'''編譯模型'''
model.compile(loss="binary_crossentropy", optimizer="sgd",
              metrics=["accuracy"])

'''特徵標準化'''
X -= X.mean(axis=0)
X /= X.std(axis=0)

'''訓練模型'''
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

'''評估模型'''
loss, accuracy= model.evaluate(X, Y)
print("準確度={:.2f}".format(accuracy))


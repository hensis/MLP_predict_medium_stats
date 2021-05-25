from numpy import array
from keras.models import Sequential
from keras.layers import Dense

all_views = [12, 34 ,22, 10, 40, {...}]

X = []
y = []

for i in range(len(all_views)):
  end_c = i + 10
  out_end_c = end_c + 4
  
  if out_end_c > len(all_views):
    break
    
  X.append(all_views[i:end_c])
  y.append(all_views[end_c:out_end_c])

X = array(X)
y = array(y)

for i in range(len(X)):
    print(X[i], y[i])

"""
for i in range(len(X)):
    print(X[i], y[i])
"""

model = Sequential()
model.add(Dense(100, activation='relu', input_dim=10))
model.add(Dense(200, activation='softmax'))
model.add(Dense(4))
model.compile(optimizer='adam', loss='mse')

model.fit(X, y, epochs=2000, verbose=2)

x_input = array([3, 5, 7, 2, 9, 10, 2, 6, 4, 9])
x_input = x_input.reshape((1, 10))
yhat = model.predict(x_input, verbose=2)
print(yhat)

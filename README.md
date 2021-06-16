# Forecasting Medium Stats with a simple MLP

[Read the Blog](https://betterprogramming.pub/predict-your-future-medium-stats-using-deep-learning-ce49bb3361ea)


- Problem overview
- Data extraction
- Data preparation
- Building the model
- Training and predicting
- Improvements and future work

> The following readme only guides you through the main points of the topic, if you want to have a full understanding of what's going on here [Read the Blog](https://betterprogramming.pub/predict-your-future-medium-stats-using-deep-learning-ce49bb3361ea)



## Problem Overview

[Read the Blog](https://betterprogramming.pub/predict-your-future-medium-stats-using-deep-learning-ce49bb3361ea)

## Data Extranction

1. We load the data from the JSON and store it as a NumPy Array object.
There are multiple ways of doing so: with python-requests, with JavaScript’s fetch method, etc. However, to make sure you actually understand what data are exactly scraping, I’ll do it manually with the help of the Chrome Developer tools.
- Open medium.com/@{username}/stats/total/{start_ts}/{end_ts}. If you are authenticated as {username}, you will see the JSON data loaded.
- Open the dev tools, and using a for loop in JavaScript, we’ll build a list of all the views:
```
all_views = []
for (i=0; i < json.payload.value.length; i++) {
    all_views.push(json.payload.value[i].reads)
}
```
This will build our list. Now we want to copy it:
`copy(all_views)`

Finally, we want to transform the copied data into single-line data. We can use Text to One Line.

## Data Preparation

We now want to prepare the data for our MLP. We’ll do this by building a dataset that will look like this:

```
X, y
[ 2 10 10  7 12  6 11 30 10 19] [35 22 15 17]
[10 10  7 12  6 11 30 10 19 35] [22 15 17 19]
[10  7 12  6 11 30 10 19 35 22] [15 17 19 23]
[ 7 12  6 11 30 10 19 35 22 15] [17 19 23 17]
```

```
from numpy import array

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
```
We got a list of all our views per hour(all_views), then we use a for loop to split the data into X (the input used to predict y), and y (our output).

## Building the Model

```
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=10))
model.add(Dense(200, activation='softmax'))
model.add(Dense(4))
model.compile(optimizer='adam', loss='mse')
```

## Training & Predicting

```
model.fit(X, y, epochs=2000, verbose=2)
```

```
x_input = array([3, 5, 7, 2, 9, 10, 2, 6, 4, 9])
x_input = x_input.reshape((1, 10))
```

```
yhat = model.predict(x_input, verbose=2)
```

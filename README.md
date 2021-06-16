# Forecasting Medium Stats with a simple MLP

[Read the Blog](https://betterprogramming.pub/predict-your-future-medium-stats-using-deep-learning-ce49bb3361ea)


- Problem overview
- Data extraction
- Data preparation
- Building the model
- Training and predicting
- Improvements and future work

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


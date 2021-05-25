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

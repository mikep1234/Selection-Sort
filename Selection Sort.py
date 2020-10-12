X = [3, 7, 2, 9, 6, 7, 8, 0, 1]
print(X)
for i in range(len(X)):
    min_index = i
    for b in range(len(X)):
        if X[b] < X[i]:
            X[i], X[b] = X[b], X[i]
            print(X)
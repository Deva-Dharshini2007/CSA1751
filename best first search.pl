edge(a, b, 2).
edge(a, c, 1).
edge(c, d, 1).
edge(b, d, 5).

best_path(X, Y, Cost) :-
    edge(X, Y, Cost).

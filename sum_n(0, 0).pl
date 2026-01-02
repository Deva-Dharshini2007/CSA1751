sum_n(0, 0).
sum_n(N, S) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, S1),
    S is N + S1.

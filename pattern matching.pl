pattern(hello).
pattern(world).
pattern(prolog).

match(X) :-
    pattern(X).

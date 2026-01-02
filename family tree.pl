parent(john, mary).
parent(john, tom).
parent(mary, ann).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

male(john).
female(mary).
female(ann).

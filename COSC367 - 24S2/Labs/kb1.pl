/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(no_lenses, _Age, _Astigmatic, RATE) :- low_tear_rate(RATE).
diagnosis(soft_lenses, AGE, no, RATE) :- young(AGE), normal_tear_rate(RATE).
diagnosis(hard_lenses, AGE, yes, RATE) :- young(AGE), normal_tear_rate(RATE).

reflection(point(X, Y), point(Y, X)).

not_same(X, Y) :- X \= Y.
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.

female(juliet).
parent(bob, juliet).
parent(bob, john).

directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).


contains(X, Y) :- directlyIn(Y, X).
contains(X, Y) :- directlyIn(Y, Z), contains(X, Z).

second([_, X | _], X).

twice([], []).
twice([H | T], [H, H | T2]) :- twice(T, T2).

tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).
listtran([], []).

listtran([H1 | T1], [H2 | T2]) :-
    tran(H1, H2),
    listtran(T1, T2).

listtran([H1 | T1], [H2 | T2]) :-
    tran(H2, H1),
    listtran(T1, T2).


preorder(leaf(X), [X]).

preorder(tree(Root, Left, Right), [Root | Traversal]) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).
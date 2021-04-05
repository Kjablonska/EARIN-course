find_triplets(A, B, C) :-
    between(1, 20, A),
    between(1, 20, B),
    A < B,
    between(1, 20, C),
    B < C,
    C*C =:= A*A + B*B.

is_triple(A, B, C) :-
  D is C*C - A*A - B*B,  % must use "is" for arithmetic
  D = 0.
pythagorean_triplets(A, B, C) :-
    between(1, 20, A),
    between(1, 20, B),
    A < B,
    between(1, 20, C),
    B < C,
    C*C =:= A*A + B*B.
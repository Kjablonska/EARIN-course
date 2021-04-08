pythagorean_triplets(A, B, C) :-
    between(1, 1000, A),
    between(1, 1000, B),
    A < B,
    C is 1000 - A - B,
    B < C,
    C*C =:= A*A + B*B,
    write("(A="), write(A), write(", B="), write(B), write(", C="), write(C), write(")"), nl, fail.

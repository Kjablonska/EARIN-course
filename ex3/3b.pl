% Assumptions:
% a < b < c
% a^2 + b^2 = c^2
% a, b, c has a value between 1-20.

pythagorean_triplets(A, B, C) :-
    between(1, 20, A),
    between(1, 20, B),
    A < B,
    between(1, 20, C),
    B < C,
    C*C =:= A*A + B*B,
    write("(A="), write(A), write(", B="), write(B), write(", C="), write(C), write(")"), nl, fail.
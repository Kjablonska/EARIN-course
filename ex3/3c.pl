% Assumptions:
% a + b + c = 1000  => c = 1000 - a - b
% a < b < c
% a^2 + b^2 = c^2

pythagorean_triplet(A, B, C) :-
    between(1, 333, A),     % 1000 / 3
    X is A + 1,
    between(X, 500, B),     % 1000 / 2
    A < B,
    C is 1000 - A - B,
    B < C,
    C*C =:= A*A + B*B,
    write("(A="), write(A), write(", B="), write(B), write(", C="), write(C), write(")"), nl, fail.

% https://stackoverflow.com/questions/2817848/find-pythagorean-triplet-for-which-a-b-c-1000

triplets(A, B, C) :-
    between(1, 333, A),
    between(1, 500, B),
    A < B,
    C is 1000 - A - B,
    B < C,
    1000 =:= A + B + C,
    C*C =:= A*A + B*B.

boundary(A, B, C) :-
    1000 =:= A + B + C.
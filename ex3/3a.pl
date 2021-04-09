% Assumptions:
% A1 is half the size of A0
% A2 is half the size of A1
% ...
% A6 is half the size of A5

isA0(A0, A1, A2, A3, A4, A5) :-
    A01 is A1/2,
    A02 is A2/4,
    A03 is A3/8,
    A04 is A4/16,
    A05 is A5/32,
    S is A0 + A01 + A02 + A03 + A04 + A05,
    S >= 1.
triples(A, B, C) :- C*C =:= A*A + B*B, boundary(A, B, C), write(A), write(B), write(C), nl.
boundary(A, B, C) :- A>0, A=<20, B>0, B=<20, C>0, C=<20.
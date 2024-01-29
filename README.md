# Lindemayer-system

A Lindenmayer system is defined iteratively, and it consists of:
a) an alphabet of symbols which can be used to create strings, 
b) an initial string used to begin the iterative construction and
c) replacement rules that specify how to replace selected symbols of the string by strings of symbols (from the
same alphabet). 
Originally, these Lindenmayer systems were used to describe the behaviour of plant cells and
to model the growth processes of plant development. In this exercise you will work with two systems called the Koch curve and the Sierpinski triangle.
**Koch curve**
The Koch curve can be generated using a) an alphabet consisting of the symbols S, L and R, b) the
initial string ’S’ and c) the replacement rules
S → SLSRSLS
L → L
R → R
The initial string is S. After the first iteration one obtains the string SLSRSLS. After the second iteration
one obtains the string SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS

**Sierpinski triangle** 
The Sierpinski triangle can be generated using a) an alphabet consisting of the symbols A,
B, L and R, b) the initial string A and c) the replacement rules for each step of the iteration.
A → BRARB
B → ALBLA
L → L
R → R
The initial string is A. After the first iteration one obtains the string BRARB. After the second iteration
one obtains the string ALBLARBRARBRALBLA. 

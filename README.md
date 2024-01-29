# Lindenmayer System

## Description
A Lindenmayer system (L-system) is defined iteratively, consisting of:
- An alphabet of symbols to create strings.
- An initial string for iterative construction.
- Replacement rules specifying how to replace symbols with strings from the same alphabet. 

Originally used to describe plant cell behavior and model plant development growth processes.

## Systems
In this exercise, we explore two systems: the Koch curve and the Sierpinski triangle.

### Koch Curve
- Alphabet: S, L, R
- Initial string: S
- Replacement rules:
  - S → SLSRSLS
  - L → L
  - R → R
- Example iterations:
  - Initial: S
  - After 1st iteration: SLSRSLS
  - After 2nd iteration: SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS

### Sierpinski Triangle
- Alphabet: A, B, L, R
- Initial string: A
- Replacement rules:
  - A → BRARB
  - B → ALBLA
  - L → L
  - R → R
- Example iterations:
  - Initial: A
  - After 1st iteration: BRARB
  - After 2nd iteration: ALBLARBRARBRALBLA

## Notes
Ensure the formatting of your README is correct when committing changes to avoid any discrepancies.

README FILE

By NADIR HAJOUJI

Given a prime p < 15073, the program can do the following:

- Find all supersingular elliptic curves defined over Fp2.
- Compute the supersingular 2-isogeny graph.
1. Elements of Fp2

The class ElementFp2 will be used to represent and√manipulate elements of Fp2.![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.001.png)

Every element of Fp2 can be described as a + b d for some a,b,d ∈ Fp - here, d is assumed to be a

nonsquare element. To construct an object that represents this element, use the class ElementFp2. 1.1. Example.

- Let p = 193, and d = −11. Note that d is a quadratic nonresidue mod p, so we can describe elements √ ![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.002.png)

in Fp2 as a + b √−11.![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.003.png)

- Let u = 80 + 12 −11 ∈Fp2. ElementFp2(193,-11,80,12) constructs an object that represents u:![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.004.png)

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.005.png)

- The coefficients a,b are treated as elements of Fp, in the sense that they are deemed equal if and only if they are congruent mo√d p. This extends to elements of Fp2: if we define a “new” element ![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.006.png)u2 = (80 + 193) + (12 − 193) −11, the code will treate u,u2 as equal:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.007.png)

- We can add and multiply elements of Fp2 using +,∗:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.008.png)

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.009.png)

- u.scale(n) returns the scalar multiple of u by the integer n. Note that n can be any (positive or negative) integer.

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.010.png)

- We can also subtract/divide. Subtraction can be done directly using -:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.011.png)

- To divide by an element w, say, we have to compute the multiplicative inverse of w and multiply by the inverse:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.012.png)

- Finally, some elementary functions from Galois theory (Galois conjugate, norm, minimal polynomial)

can be computed using u.conj(), u.norm(), u.minPoly(’x’).

- Conjugates are straightforward: u.conj() represents the Galois conjugate of u as an element of Fp2.
- The norm of u is computed by multiplying u and the conjugate of u, and returning the first coordinate of the product. Note that the output of u.norm() is an integer, not an element of F .

p2

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.013.png)

- u.minPoly(’x’) returns a string that represents the minimal polynomial of u over the field Fp, using ’x’ as the variable.

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.014.png)

2. Supersingular Elliptic Curves

Say we want information about supersingular curves in characteristic p = 193.

- We start by creating an object using the class supSingFp2:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.015.png)

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.016.png)

- To obtain j-invariants of the supersingular curves, we use:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.017.png)

Note that the output is a list of objects in the class ElementFp2.

- The set of j-invariants can also be described as the zero set of a polynomial with coefficients in Fp. The polynomial will have either linear or quadratic factors; we can either obtain the list of factors,

or the full polynomial written as a product. In both cases, all polynomials are represented as strings.

To use these, a string needs to be chosen to represent the variable:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.018.png)

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.019.png)

- The 2-isogeny graph was computed to obtain the j-invariants. To obtain the adjacency matrix of the 2-isogeny graph:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.020.png)

- If we want explicit models of the supersingular curves, we can use:

![](Aspose.Words.348aa9fe-3170-4da9-af9a-c233a9d53486.021.png)

Each of the pairs (f,g) represents an equation:

y2 = x3 + fx + g describing a supersingular elliptic curve.

Note that the coefficients f,g are elements of Fp2.

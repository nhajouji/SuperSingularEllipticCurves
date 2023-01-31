# SuperSingularEllipticCurves
Compute supersingular curves over finite fields
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 008](https://user-images.githubusercontent.com/115039038/215645645-7773e850-9df6-42ab-a662-67866f3002b2.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 009](https://user-images.githubusercontent.com/115039038/215645652-2deb6b0c-f341-4f8a-8ad0-a35843202d95.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 010](https://user-images.githubusercontent.com/115039038/215645659-c5d7c44f-eeb0-4fca-b101-a5ff787f9a16.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 011](https://user-images.githubusercontent.com/115039038/215645664-69e86ea8-a655-4722-99f3-a398237bbce6.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 012](https://user-images.githubusercontent.com/115039038/215645669-c220e967-c596-49cf-bc99-2cddcf57700e.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 013](https://user-images.githubusercontent.com/115039038/215645672-96eafd86-1fa8-4e0b-9a78-5e49d3b25050.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 014](https://user-images.githubusercontent.com/115039038/215645678-c375bc9b-ede4-4b62-bdac-4574d7b47464.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 015](https://user-images.githubusercontent.com/115039038/215645682-b7c01fde-e013-4a4d-ae11-3d42b004561f.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 016](https://user-images.githubusercontent.com/115039038/215645690-547bb528-c022-4a75-9f27-eb0bdf209dbb.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 017](https://user-images.githubusercontent.com/115039038/215645695-401c632a-374d-433a-bee4-24d9572c0682.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 018](https://user-images.githubusercontent.com/115039038/215645698-9a9b1019-881a-471c-8436-db58b8f85dba.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 019](https://user-images.githubusercontent.com/115039038/215645705-efa4efae-9748-4ba5-8a6d-4904594184af.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 020](https://user-images.githubusercontent.com/115039038/215645710-456c65b9-43c5-4e95-9b09-335ff06f140d.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 021](https://user-images.githubusercontent.com/115039038/215645716-de2821c5-0b9c-45cb-bf03-8ac628bf2ad1.png)
![Aspose Words 9107101b-66ff-48f5-9b2c-15a844057dd0 022](https://user-images.githubusercontent.com/115039038/215645722-cbe6528c-40be-4d83-b01d-f93d9931bccb.png)

Given a prime p < 15073, the program can do the following:

- Find all supersingular elliptic curves defined over Fp2.
- Compute the supersingular 2-isogeny graph.
1. Elements of Fp2

The class ElementFp2 will be used to represent and√manipulate elements of Fp2.![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.001.png)

Every element of Fp2 can be described as a + b d for some a,b,d ∈ Fp - here, d is assumed to be a

nonsquare element. To construct an object that represents this element, use the class ElementFp2. 1.1. Example.

- Let p = 193, and d = −11. Note that d is a quadratic nonresidue mod p, so we can describe elements √ ![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.002.png)

in F as a + b −11.

p2

√ ![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.003.png)

- Let u = 80 + 12 −11 ∈F . ElementFp2(193,-11,80,12) constructs an object that represents u: p2

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.004.png)

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.005.png)

- The coefficients a,b are treated as elements of Fp, in the sense that they are deemed equal if and

only if they are congruent mod

√ p. This extends to elements of Fp2: if we define a “new” element![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.006.png)

u2 = (80 + 193) + (12 − 193) −11, the code will treate u,u2 as equal:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.007.png)

- We can add and multiply elements of Fp2 using +,∗:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.008.png)

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.009.png)

- u.scale(n) returns the scalar multiple of u by the integer n. Note that n can be any (positive or negative) integer.

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.010.png)

- We can also subtract/divide. Subtraction can be done directly using -:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.011.png)

- To divide by an element w, say, we have to compute the multiplicative inverse of w and multiply by the inverse:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.012.png)

- Finally, some elementary functions from Galois theory (Galois conjugate, norm, minimal polynomial)

can be computed using u.conj(), u.norm(), u.minPoly(’x’).

- Conjugates are straightforward: u.conj() represents the Galois conjugate of u as an element of Fp2.
- The norm of u is computed by multiplying u and the conjugate of u, and returning the first coordinate of the product. Note that the output of u.norm() is an integer, not an element of F .

p2

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.013.png)

- u.minPoly(’x’) returns a string that represents the minimal polynomial of u over the field Fp, using ’x’ as the variable.

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.014.png)

2. Supersingular Elliptic Curves

Say we want information about supersingular curves in characteristic p = 193.

- We start by creating an object using the class supSingFp2:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.015.png)

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.016.png)

- To obtain j-invariants of the supersingular curves, we use:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.017.png)

Note that the output is a list of objects in the class ElementFp2.

- The set of j-invariants can also be described as the zero set of a polynomial with coefficients in Fp. The polynomial will have either linear or quadratic factors; we can either obtain the list of factors,

or the full polynomial written as a product. In both cases, all polynomials are represented as strings.

To use these, a string needs to be chosen to represent the variable:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.018.png)

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.019.png)

- The 2-isogeny graph was computed to obtain the j-invariants. To obtain the adjacency matrix of the 2-isogeny graph:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.020.png)

- If we want explicit models of the supersingular curves, we can use:

![](Aspose.Words.9107101b-66ff-48f5-9b2c-15a844057dd0.021.png)

Each of the pairs (f,g) represents an equation:

y2 = x3 + fx + g describing a supersingular elliptic curve.

Note that the coefficients f,g are elements of Fp2.

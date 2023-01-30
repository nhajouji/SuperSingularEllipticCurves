# The following program takes as input a prime p,
# and returns a list of supersingular j values.

# The result will be a list of elements of F_p^2, the field with p^2 elements.
# All computations will be happening in that field.

# We wil need to divide elements.

# To divide in F_p, we essentially need to be able to solve ax+by = 1 for x,y.

# The function axbySolve produces x,y such that ax+by is the gcd of a,b.
# Note that a,b are assumed to be positive in the code for axbySolve.

def magicBox0(last4,a2):
    n0 = last4[0][0]
    n1 = last4[1][0]
    d0 = last4[0][1]
    d1 = last4[1][1]
    n2 = a2*n1+n0
    d2 = a2*d1+d0
    newlast4 = [last4[1],[n2,d2]]
    return newlast4

def axbySolve(a,b):
    m = min(a,b)
    n = max(a,b)
    lst4 = [[0,1],[1,0]]
    while n % m !=0:
        q = n//m
        r = n % m
        lst4 = magicBox0(lst4,q)
        newn = m
        newm = r
        n = newn
        m = newm
    q = n//m
    lst4 = magicBox0(lst4,q)
    xy = lst4[0]
    if a<b:
        if xy[0]*a>xy[1]*b:
            return [xy[0],-xy[1]]
        else:
            return [-xy[0],xy[1]]
    elif xy[0]*b>xy[1]*a:
        return [-xy[1],xy[0]]
    else:
        return [xy[1],-xy[0]]

# The following function takes as input an integer a and a prime p,
# an integer b such that ab is congruent to 1 mod p.

# If a is divisible by p, the function will simply return 0.

def invMod(a,p):
    if a % p == 0:
        return 0
    xy = axbySolve(a,p)
    return xy[0] %p

# We will need to choose a nonsquare d in F_p in order to construct F_p^2.
# To describe an element of Fp2, we need to fix an element n in Fp
# which does not have a square root in Fp.
# Elements of Fp2 will be described as a + b sqrt(n), where a, b are in Fp.
# To describe an element, we need to specify p, n, a, b.

class ElementFp2:
    def __init__(self,p,n,a,b):
        self.char = p
        self.nonsquare = n
        self.proj1 = a % p
        self.proj2 = b % p
        self.vec = (a%p,b%p)
    def __repr__(self):
        p = self.char
        n = self.nonsquare
        a = self.proj1
        b = self.proj2
        if a == 0 and b == 0:
            return "0"
        elif a == 0:
            return str(b)+" sqrt("+str(n)+")"
        elif b == 0:
            return str(a)
        else:
            return str(a)+"+"+str(b)+" sqrt(" +str(n)+")"
    def text(self):
        p = self.char
        n = self.nonsquare
        a = self.proj1
        b = self.proj2
        if a == 0 and b == 0:
            return "0"
        elif a == 0:
            return str(b)+" sqrt("+str(n)+")"
        elif b == 0:
            return str(a)
        else:
            return str(a)+"+"+str(b)+" sqrt(" +str(n)+")"
    def __eq__(self,other):
        p = self.char
        a1 = self.proj1
        a2 = other.proj1
        b1 = self.proj2
        b2 = other.proj2
        return ((a1-a2)%p==0) and ((b1-b2)%p==0)
    
    def __add__(self,other):
        a1 = self.proj1
        a2 = other.proj1
        b1 = self.proj2
        b2 = other.proj2
        p = self.char
        ns = self.nonsquare
        return ElementFp2(p,ns,(a1+a2) % p, (b1+b2)%p)
    
    def __mul__(self,other):
        a1 = self.proj1
        a2 = other.proj1
        b1 = self.proj2
        b2 = other.proj2
        p = self.char
        ns = self.nonsquare
        a3 = (a1*a2+ns*b1*b2) % p
        b3 = (a1*b2+a2*b1) % p
        return ElementFp2(p,ns,a3,b3)
    
    def scale(self,c):
        p = self.char
        ns = self.nonsquare
        cfp2 = ElementFp2(p,ns,c,0)
        return self*cfp2

    def __sub__(self,other):
        return self + other.scale(-1)
    
    def conj(self):
        a = self.proj1
        b = self.proj2
        p = self.char
        ns = self.nonsquare
        return ElementFp2(p,ns, a, p-b)
    
    def norm(self):
        cnj = self.conj()
        n2 = self*cnj
        return n2.proj1
    
    def multInv(self):
        cnj = self.conj()
        nrm2 = self*cnj
        n = nrm2.proj1
        p = self.char
        ninv = invMod(n,p)
        rec = cnj.scale(ninv)
        return rec

    def inFp(self):
        b = self.proj2
        return b==0

    def minPoly(self,x):
        p = self.char
        a = self.proj1
        b = self.proj2
        if b == 0:
            return x+'-'+str(a)
        else:
            c0 = self.norm()
            c1 = (-2*self.proj1)%p
            return x+"^2+"+str(c1)+x+'+'+str(c0)

    

# To solve quadratic equations, we need to be able to compute square roots.

# genSqrtDic takes as input a prime p and an integer d.
# The function assumes that d is a nonresidue mod p,
# and returns a dictionary whose keys are tuples of integers (a,b),
# and where the value of (a,b) is the set of square roots of a+b sqrt(d)
# in the field F_p^2. The square roots are represented as elements of Fp2.

def genSqrtDic(p,d):
    dic = {(a,b):[] for a in range(p) for b in range(p)}
    for a in range(p):
        for b in range(p):
            rt = ElementFp2(p,d,a,b)
            dic[(rt*rt).vec].append(rt)
    return dic

# solveQuadratic takes as input a tuple ab = (a,b), where a, b are in Fp2.
# Note that a,b should be defined using the same nonsquare ns in Fp2.
# The pair ab represents a quadratic eqution x^2 + ax + b =0.
# We also need a dictionary, which should be obtained using genSqrtDic(p,ns),
# where ns is the same nonsquare used to define a and b.
# The function assumes that the keys of dic are tuples (a0,b0) that represent
# a0+b0 sqrt(ns) in Fp2, and the value of (a0,b0) is a list of elements in Fp2
# that square to a0+b0 sqrt(ns).
# The output of solveQuadratic is a list of the roots of the quadratic equation.

def solveQuadratic(ab,dic):
    a = ab[0]
    b = ab[1]
    p = a.char
    half = (p+1)//2
    d = disc(ab)
    rtds = dic[d.vec]
    rtsab = [(r-a).scale(half) for r in rtds]
    return rtsab


# Elliptic curves

# All curves will be represented by equations of the form y^2 = x(x^2+ax+b)
# To describe a curve, we specify the coefficients (a,b) as a tuple of length 2.
# The coefficients are assumed to be elements of Fp2.

# For such a pair, we compute the discriminant and j-invariant using disc/jInv:

def disc(ab):
    a = ab[0]
    b = ab[1]
    return a*a+b.scale(-4)

def jInv(ab):
    a = ab[0]
    b = ab[1]
    num = ((a*a-b.scale(3))*(a*a-b.scale(3))*(a*a-b.scale(3))).scale(256)
    den = b*b*disc(ab)
    return num*(den.multInv())

# weirCoefsFrom2tor computes "short Weierstrass coefficients" from a pair (a,b).
# This is not needed in any of the current code, but may be useful in the future.

def weirCoefsFrom2tor(ab):
    a = ab[0]
    b = ab[1]
    a2 = a*a
    a3 = a2*a
    f = a2.scale(-3)+b.scale(9)
    g = a3.scale(2)+a*b.scale(-9)
    return (f,g)

def jFromFG(fg):
    f = fg[0]
    g = fg[1]
    f2 = f*f
    f3 = f2*f
    num = f3.scale(4*1728)
    d = f3.scale(4)+g*g.scale(27)
    den = d.multInv()
    return num * den

# For a given curve, there are three pairs (a,b) we need to use.
# If we have one pair (a,b), we can obtain the other two pairs by:

# First, solving the quadratic equation x^2 + ax + b.
# There will be two solutions, r1 and r2.

# Second, we do a change of variable xi <-> x+ri to the cubic x(x^2+ax+b).
# This gives us two new equations xi(xi^2 + ai xi + bi).

# The function allPairs will take as input a pair (a,b),
# and return a list containing all 3 pairs needed.

# Since we need to solve quadratic equations, we also need a square root dict.

def allPairs(ab,dic):
    rts = solveQuadratic(ab,dic)
    r0 = rts[0]
    r1 = rts[1]
    a0 = r0.scale(2)-r1
    b0 = r0 *(r0-r1)
    a1 = r1.scale(2)-r0
    b1 = r1 * (r1 - r0)
    return [ab, (a0,b0), (a1,b1)]


# twoIsog takes as input a pair (a,b) that represents an elliptic curve,
# and produces a new pair of the same type
# that represents the 2-isogenous curve.

def twoIsog(ab):
    a = ab[0]
    b = ab[1]
    a2 = a.scale(-2)
    b2 = disc(ab)
    return (a2,b2)


# twoIsogenyGraph

# ab2graphDic takes as input an pair ab0 = (a0,b0) that represents
# an equation for a supersingular curve of the form y^2 = x(x^2 + a0 x + b0)
# and a dictionary of square roots.
# The function computes the 2-isogeny graph from this data,
# and returns a dictionary whose keys are the supersingular j-invariants,
# encoded as tuples of integers, and the value associated to each key is
# a set containing the endpoints of the three edges leaving that vertex.

def ab2GraphsAndModels(ab0,dic):
    js = []
    eqs = [ab0]
    graph = {}
    models = {}
    while len(eqs) > 0:
        neweqs = []
        for ab in eqs:
            jab = jInv(ab).vec
            if jab not in js:
                js.append(jab)
                jabModels = allPairs(ab,dic)
                ab2s = [twoIsog(ab1) for ab1 in jabModels]
                jab2s = [jInv(ab2).vec for ab2 in ab2s]
                graph.update({jab:jab2s})
                models.update({jab:jabModels})
                for i in [0,1,2]:
                    if jab2s[i] not in js:
                        neweqs.append(ab2s[i])
        eqs = neweqs
    return [graph,models]

# Set-up

# We now start with a prime p, and produce the j-invariants.
# The choice of p will determine the nonsquare we use:
# we will restrict to nonsquares in the list below:

nonSquares = [-1,-2,-3,-7,-11,-19,-43,-67,-163]

# For any odd prime p < 15073, one of those integers is a quadratic nonresidue.

def chooseNonSquare(p):
    if p % 4 == 3:
        return -1
    elif p % 3 == 2:
        return -3
    elif p % 8 == 5:
        return -2
    for d in [-7,-11,-19,-43,-67,-163]:
        q = -d
        sqs = [a**2 % q for a in range(1,(q+1)//2)]
        p0 = p % q
        if p0 not in sqs:
            return d
    return "Couldn't find one - make sure p is an odd prime, and p < 15073 "

# The nonsquare we obtained will determine our starting elliptic curve.
# If the nonsquare is -1,-2,-3 or -7, the corresponding elliptic curve
# can be described by an equation y^2 = x(x^2 + ax + b) with a,b in Z.
# As a result, we do not have to do any additonal work to obtain (a,b).

# If the nonsquare is -11, -19, -43, -67, -163, the elliptic curve we will use
# does not have 2-torsion over Z, so we will have to start with a pair
# fg = (f,g), where f, g are integers representing y^2 = x^3 + fx + g.
# The cubic x^3 + fx + g does not have a root in Z, but will have one in Z/p.
# To obtain (a,b), we simply need to find a root of r of x^3 + fx + g.
# The coefficients a,b can be obtained from r, f, g.

fgs=[(-264,1694),(-152,722),(-3440,77658),(-29480,1948226),(-8697680,9873093538)]
fgDic = {nonSquares[4+i]:fgs[i] for i in range(5)}

#evCubic takes as input a pair fg = (f,g), an integer x and a prime p,
#and returns the value x^3 + fx +g mod p.

def evCubic(fg,x,p):
    f = fg[0]
    g = fg[1]
    return ((x**3)+f*x+g) % p

# findCoefs0 takes p as an input,
# uses chooseNonSquare to find a suitable nonsquare d.
# If d = -1,-2,-3 or -7, findCoefs returns a pair of integers (a,b)
# such that y^2 = x(x^2+ax +b) is supersingular.
# If d is not one of those values, findCoefs0 checks fgDic for coefficients
# (f,g) representing an elliptic curve y^2 = x^3 + fx + g.
# The program then uses evCubic to search for a solution to the cubic;
# once a solution is found, the program computes a change of variable
# to produce a suitable pair (a,b).

def findCoefs0(p):
    d = chooseNonSquare(p)
    if d == -1:
        return (ElementFp2(p,-1,0,0),ElementFp2(p,-1,-1,0))
    elif d == -3:
        return (ElementFp2(p,-3,3,0),ElementFp2(p,-3,3,0))
    elif d == -2:
        return (ElementFp2(p,-2,4,0),ElementFp2(p,-2,2,0))
    elif d == -7:
        return (ElementFp2(p,-7,-21,0),ElementFp2(p,-7,112,0))
    else:
        fg = fgDic[d]
        f = fg[0]
        x= 0
        while x < p and evCubic(fg,x,p)!= 0:
            x+=1
        if x == p:
            return "No 2-torsion found"
        else:
            return (ElementFp2(p,d,(3*x)%p,0),ElementFp2(p,d,(3*x*x+f)%p,0))

# We now have everything in place.
# superSingularJs takes as input a prime p,
# uses findCoefs0 to obtain a pair (a,b) that represents a supersingular curve,
# then uses ab2alljs to obtain all j-invariants from the pair (a,b).

def getMatJsNSsqrtD(p):
    ab0 = findCoefs0(p)
    d = ab0[0].nonsquare
    sqrtdic = genSqrtDic(p,d)
    graphmodel = ab2GraphsAndModels(ab0,sqrtdic)
    graph = graphmodel[0]
    models = graphmodel[1]
    js = list(graph.keys())
    nojs = len(js)
    idic = {js[i]:i for i in range(nojs)}
    mat = []
    for i in range(nojs):
        ji = js[i]
        endpts = graph[ji]
        endptis = [idic[j] for j in endpts]
        row = [0] * nojs
        for k in endptis:
            row[k]+=1
        mat.append(row)
    return [mat,js,d,models,sqrtdic]

# Creating an element in class supSingFp2 runs getMatJsNSsqrtD(p)
# to compute the 2-isogeny graph and collect all the data obtained.
# Once the class is initialized, the j-invariants, models, etc. are easily
# obtained from the data we just obtained, without having to repeat the initial
# long computation.

#

class supSingFp2:
# Computes the 2-isogeny graph using getMatJsNSsqrtD;
# the data can be accessed in the future as self.rawdata
# without needing to repeat the initial computation.
    def __init__(self,p):
        self.char = p
        self.rawdata = getMatJsNSsqrtD(p)
    def __repr__(self):
        p = self.char
        return "Data about supersingular curves in characteristic "+str(p)
# self.js() converts the j-invariants in rawdata to elements of Fp2
# and returns a list containing the result
    def js(self):
        data = self.rawdata
        d = data[2]
        p = self.char
        jpairs = data[1]
        return [ElementFp2(p,d,ab[0],ab[1]) for ab in jpairs]
# self.twoIsogMat() returns the adjacency matrix of the 2-isogeny graph
    def twoIsogMat(self):
        data = self.rawdata
        return data[0]
# self.twoTorModels(j) returns a list containing 3 pairs (a,b)
# that can be used to represent the elliptic curve with given j-invariant.
# These models were obtained during the computation of the 2-isogeny graph;
    def twoTorModels(self,j):
        data = self.rawdata
        return data[3][j.vec]
# self.shortWeirEQs(j) returns a pair of coefficients (f,g) that represent
# an elliptic curve y^2 = x^3 + fx + g with j-invariant j.
    def shortWeirEQs(self,j):
        data = self.rawdata
        return weirCoefsFrom2tor(data[3][j.vec][0])
# self.fgs() returns the set of (f,g)'s for all possible j-invariants.
    def fgs(self):
        j0s = self.js()
        return [self.shortWeirEQs(j) for j in j0s]
    
 

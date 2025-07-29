---
title: Multiplication is Simple, Really
author: Catman
layout: post
long: true
---

> We can convert problems of pure multiplication to problems of pure addition! Specifically, The multiplicative group $(0,\infty)$ is isomorphic to the additive group $\mathbb{R}$. Another similar case is that of the multiplicative group modulo $p$, which is isomorphic to the additive group modulo $p-1$ due to the existence of primitive roots. In both cases, the math is greatly simplified!

---

### The Exponential Function

The exponential function, which I will assume exists, is a bijective function $\exp:\mathbb{R} \to (0,\infty)$ such that

$$\exp(x+y) = \exp(x)\exp(y).$$

In other words, $\exp$ is an isomorphism between the additive group of reals and the multiplicative group of positive reals. It's inverse is called $\log$.

#### Existence of $n^{th}$ Roots is Easy
Given some $x\in(0,\infty)$ and a positive integer $n$, I will show that there exists exactly one $y\in (0,\infty)$ such that $y^n = x$.

Because of the isomorphism, we can rewrite the problem in the world of addition:

> Given some $x\in \mathbb{R}$ and a positive integer $n$, there exists exactly one $y\in\mathbb{R}$ such that $ny = x$.

The problem is so much easier now! The difficult part here is showing that $\exp$ exists in the first place

### Primitive Roots

A very useful tool in modular arithmetic is *primitive roots* of the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$, which give us a tool very similar to the exponential function in the real numbers.

The *order* of $g$ is the smallest positive exponent $a$ such that $g^a \equiv 1 \pmod p$. This is denoted
$|g|$. In the case where
$|g| = p-1$, the residue $g$ is a primitive root.

Why does this matter? The values $g,g^2,\dots,g^{p-1}$ make up the entirety of $(\mathbb{Z}/p\mathbb{Z})^\times$! This means that the group is cyclic, so we can translate problems about multiplication mod $p$ to addition mod $p-1$. And addition in modular arithmetic is much simpler!

#### Proving $(\mathbb{Z}/p\mathbb{Z})^\times$ is Cyclic
Like the exponential function, it is somewhat difficult to show that primitive roots exist in the first place. Here is an outline of the proof:

* Let $A(d)$ be the number of elements of $\{1,\dots,p-1\}$ with multiplicative order $d$.
  * This can only be nonzero for divisors of $p-1$.
* If
  $|a| = d$, then the polynomial $x^d - 1$ over the field $F_p$ has roots $1,a,a^2,\dots,a^{d-1}$.
  * It can't have any more than $d$ roots because $F_p$ is a field.
  * Exactly $\varphi(d)$ of the roots have order $d$.
* So $A(d)$ is either $0$ or $\varphi(d)$.
* The sums $\sum_{d\mid p-1}A(d)$ and $\sum_{d\mid p-1}\varphi(d)$ are both equal to $p-1$, thus $A(d) = \varphi(d)$ for all $d\mid p-1$.
* In particular, $A(p-1) = \varphi(p-1) > 0$.

#### What About $k^{th}$ Roots Mod $p$?

* I leave it as an exercise to show that there are $\frac{p-1}{\gcd(k,p-1)}$ nonzero $k^{th}$ powers modulo $p$. Just like in the case of reals, the key is to shift to the additive perspective.

### Conclusion

I conclude that both the exponential function and primitive roots are super powerful!
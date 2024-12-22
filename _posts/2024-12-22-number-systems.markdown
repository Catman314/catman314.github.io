---
layout: post
title:  "A Journey of Number Systems"
---

This is the first post of a series on calculus.
### Intro
> We all know what real numbers are... just decimal expansions... right?

Real numbers are not just decimal expansions, for a few reasons
* There is nothing special about the number 10; we could choose any base.
* Defining addition, subtraction, multiplication and division based on just the decimal expansion is very tedious. There is a better way.

This post will explore the number systems: $\mathbb{N},\mathbb{Z},\mathbb{Q}$, and finally $\mathbb{R}$ and $\mathbb{C}$.

---
* TOC
{:toc}
---

### Natural Numbers
The natural numbers $\mathbb{N}$ are the numbers $(0,1,2,3,\dots)$. Some people omit the 0, but I think it's nicer to include it. They have the following properties:
* **Givens:** We start with the number $0$ given, as well as a successor operator $S$ (intuitively, think of $S(n)$ as "add 1 to $n$").
* $0$ is not the successor of a natural number.
* **$S$ is injective:** Two different numbers can't have the same successor (Think about what happens if they did).
* **Induction:** Let's say $P$ is some property about natural numbers, Suppose that we know $P(0)$ is true, and also that $P(n) \implies P(n+1)$. Then we can conclude that $P$ is true for every natural number.

It turns out that any two structures with these properties *are the same!*

---
<details>
<summary>Proof</summary>

<p>
Suppose $(\mathbb{N},0,S)$ and $(\mathbb{N'},0',S')$ both satisfy the axioms. Define $\phi:\mathbb{N}\to\mathbb{N}'$ recursively so that

$$
\begin{align*}
    \phi(0) &= 0' \\
    \phi(S(n)) &= S'(\phi(n)).
\end{align*}
$$
The fact that recursion is allowed is a theorem implied by the axioms. Now we have that $\phi$ is a homomorphism by definition, so we just need to show that $\phi$ is bijective. I leave this as an exercise (in other words, I'm lazy).
</p>
</details>
---

We can define addition and multiplication recursively, and their properties (commutativity, associativity, etc.) are proven by induction.

### The Integers
Now we want to subtract two numbers, but we realise we can't do $1 - 2$. We need more numbers.

The idea for this construction is to define integers as differences of natural numbers. Following intuition based on prior knowledge, we will make the following definitions.
* **Addition:** $(a-b) + (c-d) = (a+c) - (b+d)$
* **Multiplication:** $(a-b)\cdot(c-d) = (ac + bd) - (ad + bc)$
* **Equivalence:** $(a-b)\equiv(c-d) \iff a + d = b + c$

We can prove that $(\equiv)$ is an equivalence relation (do it), and that if $a\equiv a'$ and $b\equiv b'$, then

$$a+b \equiv a'+b' \qquad\text{and}\qquad a\cdot b\equiv a'\cdot b'$$

Therefore, we can define the integers $\mathbb{Z}$ as the equivalence classes created by $(\equiv)$, and addition and multiplication are both well defined. For example,

$$-1 = \{(0-1), (1-2), (2-3), (3-4),\dots\}$$

Also, the natural numbers are contained in the integers, using $n \mapsto [(n-0)].$ Check that addition and multiplication in $\mathbb{N}$ is the same in $\mathbb{Z}$.

Verify that $\mathbb{Z}$ is a ring.

### The Rationals
Constructing $\mathbb{Q}$ is very similar to constructing $\mathbb{Z}$. Instead of differences, we use quotients. Also, we must remember that dividing by $0$ is illegal.
* **Addition:** $(a/b) + (c/d) = (ad + bc) / bd$
* **Multiplication:** $(a/b) \cdot (c/d) = ac / bd$
* **Equivalence:** $(a/b)\equiv (c/d) \iff ad = bc$.

Again, we define $\mathbb{Q}$ as the equivalence classes of $(\equiv)$, and verify that the integers are inside the rationals as $n\mapsto [(n/1)]$.

Verify that $\mathbb{Q}$ is a field (remember that $(a/0)$ is not a rational number).

### The Reals
TO BE CONTINUED
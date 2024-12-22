---
layout: post
title:  "A Journey of Number Systems"
date:   2024-12-22 09:32:15 -0500
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
The natural numbers $\mathbb{N}$ are the numbers $$\{0,1,2,3,\dots\}.$$ Some people omit the 0, but I think it's nicer to include it. They have the following properties (The Peano Axioms):
* **Givens:** We start with the number $0$ given, as well as a successor operator $S$ (intuitively, think of $S(n)$ as "add 1 to $n$").
* $0$ is not the successor of a natural number.
* **$S$ is injective:** Two different numbers can't have the same successor (Think about what happens if they did).
* **Induction:** Let's say $P$ is some property about natural numbers, Suppose that we know $P(0)$ is true, and also that $P(n) \implies P(n+1)$. Then we can conclude that $P$ is true for every natural number.

Induction is basically an infinite chain of implications

$$P(0) \implies P(1) \implies P(2) \implies P(3) \implies \dots$$

Only the natural numbers satisfy every condition.

We can define addition and multiplication recursively, and their properties (commutativity, associativity, etc.) are proven by induction.

<details markdown=1 open>
<summary>Exercises</summary>
* Create recursive definitions of addition, multiplication, and exponents.
* Prove some properties of addition and multiplication.
* We say $m\le n$ if and only if there is an integer $k$ such that $n = k + m$.
* Show that there is only one structure up to isomorphism satisfying the Peano Axioms
</details>

### The Integers
Now we want to subtract two numbers, but we realise we can't do $1 - 2$. We need more numbers.

The idea for this construction is to define integers as differences of natural numbers. Following intuition based on prior knowledge, we will make the following definitions.
* **Addition:** $(a-b) + (c-d) = (a+c) - (b+d)$
* **Multiplication:** $(a-b)\cdot(c-d) = (ac + bd) - (ad + bc)$
* **Ordering:** $(a-b)\le (c-d) \iff a+d \le b+c$
* **Equivalence:** $(a-b) = (c-d) \iff a + d = b + c$
    * If we want to be formal, this would be an equivalence relation, and $\mathbb{Z}$ would be the equivalence classes.


Also, the natural numbers are contained in the integers, using $n \mapsto (n-0).$

<details markdown=1 open>
<summary>Exercises</summary>
* Check that addition and multiplication in $\mathbb{Z}$ are well defined.
* The map $n\mapsto (n-0)$ is an injective homomorphism (addition, multiplication, and ordering must be preserved).
* Verify that $\mathbb{Z},+,\cdot$ is a ring.
</details>

### The Rationals
Constructing $\mathbb{Q}$ is very similar to constructing $\mathbb{Z}$. Instead of differences, we use quotients. Also, we must remember that dividing by $0$ is illegal.
* **Addition:** $(a/b) + (c/d) = (ad + bc) / bd$
* **Multiplication:** $(a/b) \cdot (c/d) = ac / bd$
* **Ordering:** $(a/b)\le(c/d) \iff ad \le bc$
* **Equivalence:** $(a/b)\equiv (c/d) \iff ad = bc$.
    * Again, equivalence classes.

<details markdown=1 open>
<summary>Exercises</summary>
* Prove that our definition of equivalence is an equivalence relation. Notice that we assume the denominator must be nonzero at some point.
* The integers are embedded in the rationals by $z \mapsto (z/1)$. Show that this is a homomorphism (verify addition, multiplication, and ordering).
* $\mathbb{Q,+,\cdot,\le}$ is an ordered field.
</details>

### The Reals
TO BE CONTINUED
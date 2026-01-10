---
title: "Sequence Convergence via Landau Notation"
author: Catman
layout: post
long: true
---

This is the first part of (hopefully) a series explaining calculus via Landau notation. I think that this approach will make confusing concepts more clear.

### Little-$o$

If $b_n$ is a positive sequence, the notation $a_n \in o(b_n)$ says that $(a_n)$ is much smaller (closer to zero) than $(b_n)$. More precisely, it means $a_n$'s magnitude is eventually less than any multiple of $b_n$.

A particularly useful case is $o(1)$. We have $a_n \in o(1)$ if $a_n$ is eventually less than any multiple of 1, i.e. any real number $\varepsilon > 0$. A good example is

$$\frac{1}{n} \in o(1)$$

because for any $\varepsilon > 0$, the terms $\frac{1}{n}$ will eventually go below $\varepsilon$. Intuitively, $o(1)$ represents all the sequences which vanish to $0$ over time, and we will use this idea to define limits.

### The Limit of a Sequence

Let $(a_n)$ be some sequence of real numbers. We want to capture the idea of $(a_n)$ approaching some value $x$. In other words, the difference between $(a_n)$ and $x$ should vanish over time. We can use $o(1)$ now!

$$
\begin{align*}
  a_n - x &\in o(1) \\
  a_n &\in x + o(1)
\end{align*}
$$

For example, the sequence defined by $a_n = \frac{n+1}{n}$ converges to 1 because

$$\frac{n + 1}{n} = 1 + \frac{1}{n} \in 1 + o(1),$$

### Arithmetic with $o$

Here are some ways that little-$o$ can be manipulated:

> *Properties of $o$*
> * *Constants are absorbed:* $M\cdot o(f(x)) = o(f(x))$
> * *Multiplication:*
>   * $f(x)\cdot o(g(x)) =o(\vert f(x)\vert g(x))$
>   * $o(f(x))\cdot o(g(x)) = o(f(x)g(x))$
> * *Addition:*
>   * If $f(x) \in o(g(x))$, then $f(x) + o(g(x)) = o(g(x))$
>   * $o(f(x)) + o(g(x)) = o(f(x) + g(x))$

#### Arithmetic with Sequence Limits

If $(a_n) = a + o(1)$ and $(b_n) = b + o(1)$, then

$$
\begin{align*}
  (a_n + b_n) &\in a + b + o(1) + o(1) \\
  &= a + b + o(1) \\
  (a_n\cdot b_n) &\in (a+o(1))(b+o(1)) \\
  &= ab + a\cdot o(1) + b\cdot o(1) + o(1)\cdot o(1) \\
  &= ab + o(1) \\
\end{align*}
$$

This is SO MUCH EASIER than the usual proofs of these facts.


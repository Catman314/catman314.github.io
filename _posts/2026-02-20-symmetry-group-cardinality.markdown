---
title: Cardinality of Infinite Symmetry Groups
author: Catman
layout: post
long: true
---

> We will show that if $X$ is infinite, then in terms of cardinality, there are as many bijections as there are functions from $X\to X$.

### Notation
* $S_X$ denotes the set of permutations of $X$.
* $X^X$ is the set of all functions from $X\to X$.

My approach will be to construct a cycle of injections $\mathcal{P}(X)\to S_X\to X^X\to \mathcal{P}(X)$, which will show that these sets all have the same cardinality by the Schroder-Bernstein theorem.

The injection $S_X\to X^X$ is easy; the inclusion map. The other two are more difficult.


### Some Set Theory

Before we go further, we will need a few facts about cardinality. Let $X$ be an infinite set. Then

* $
|X| =
|X\sqcup X|$, where $\sqcup$ is the disjoint union operation,
* $
|X| =
|X\times X|$,
* $
|X^X| =
|\mathcal{P}(X)|$.

Each of these will follow from the previous. I love Zorn's lemma, so I will use it to prove the first two.

#### Disjoint Union

<details><summary>
<strong>Theorem: </strong> Let $X$ and $Y$ be equinumerous disjoint infinite sets. Then $|X\cup Y|$ has the same cardinality as $|X|$.
</summary>
<div markdown="1">

*Proof.* Suppose $X$ and $Y$ are equinumerous disjoint infinite sets, with a bijection $\varphi:X\bij Y$. Define

$$\mathcal{F} := \{f:A\cup\varphi(A)\bij A\mid A\subseteq X, A\text{ is infinite}\},$$

partially ordered by function extension. Since $X$ is infinite, it contains a countably infinite subset $Z$, and the sets $Z\cup \varphi(Z)$ and $Z$ have the same cardinality, so $\mathcal{F}$ is nonempty.

A chain in $\mathcal{F}$ has an upper bound in $\mathcal{F}$ obtained by unioning the domains. Therefore, Zorn's lemma states that $\mathcal{F}$ has a maximal element, say $g:B\cup\varphi(B)\bij B$ for some $B\subseteq X$.

Assume for the sake of contradiction that $X\setminus B$ is infinite. Then there is some countably infinite $Z\subseteq X$ which is disjoint with $B$. But then $g$'s domain can be extended to include $Z\cup \varphi(Z)$ because a bijection $Z\cup\varphi(Z)\bij Z$ exists. This contradicts the maximality of $g$, thus $X\setminus B$ is finite.

Because $X$ is infinite, this implies
$|B| = |X|$, so there is a bijection $h:X\bij B$, and finally the bijection

$$h^{-1}\circ g\circ (h\cup (\varphi\circ h\circ \varphi^{-1})):X\cup Y\bij X.$$

</div>
</details>


#### Product

<details><summary>
<strong>Theorem: </strong> If $X$ is infinite, then
$|X| = |X\times X|$.
</summary>
<div markdown="1">

*Proof.* Let $X$ be an infinite set. Let $\mathcal{B}$ be the set of bijections $Y\times Y\bij Y$ for infinite subsets $Y\subseteq X$, ordered by function extension.

Since $X$ has a countable subset, $\mathcal{B}$ is nonempty because
$|\mathbb{N}\times\mathbb{N}| = |\mathbb{N}|.$

Every chain in $\mathcal{B}$ has an upper bound in $\mathcal{B}$ by unioning the domains. Therefore, $\mathcal{B}$ has some maximal element, say $f:A\times A\bij A$.

We will now show that
$|A| = |X|$. Assuming that
$|A| < |X|$, then
$|X - A|$ contains a subset $B$ with equal cardinality to $A$. Then all the sets

$$A, B, A\times A, A\times B, B\times A, B\times B$$

have the same cardinality, so by the disjoint union theorem above, we have

$$|(A\times B)\cup (B\times A)\cup (B\times B)| = |B|.$$

We can use this to extend $f$ to the domain $(A\cup B)\times (A\cup B)$, contradicting the maximality of $f$. Therefore,
$|A| = |X|$, and so

$$|X| = |X\times X|.$$

</div>
</details>


#### Power Set

<details><summary>
<strong>Theorem: </strong> If $X$ is infinite, then $|X^X| = |\mathcal{P}(X)|$.
</summary>
<div markdown="1">

*Proof.* An injection $\mathcal{P}(X)\inj X^X$ exists by choosing two elements $x_1,x_2\in X$ and considering functions where $$f(X)\subseteq \{x_1,x_2\}$$.

An injection $X^X\to \mathcal{P}(X\times X)$ exists by considering the graphs of functions in $X^X$. Since
$|X| = |X\times X|$, we have

$$|\mathcal{P}(X)| = |\mathcal{P}(X\times X)|.$$

By the Schroder-Bernstein theorem,
$|\mathcal{P}(X)| = |X^X|$.

</div>
</details>

We now have the second injection of the trio: $X^X\inj \mathcal{P}(X)$.

### A Bijection for each Subset

Let $X$ be infinite. All that remains is to find an injection $\mathcal{P}(X)\inj S_X$. We will use the fact that
$$|X| = |X\times\{0,1\}|,$$
which is a corollary of the disjoint union theorem above. Let $$\varphi:X\bij X\times\{0,1\}$$. Define $$f:\mathcal{P}(X)\to S_{X\times\{0,1\}}$$ by

$$
\begin{align*}
  f(A) &:= f_A \\
  f_A(x,\lambda) &:= \begin{cases}
    (x, 1 - \lambda) & x\in A \\
    (x, \lambda) & x\notin A.
  \end{cases}
\end{align*}
$$

It's easy to check that $f$ is injective, and so we have the final injection we needed. Therefore,
$|S_X| = |X^X|$. There are as many bijections as there are functions when $X$ is infinite. That is weird.
---
layout: post
title: "Constructing the Real Numbers"
tags: [notes]
series: "Real Analysis Notes"
series-index: 0
---

A nice way to construct $\mathbb{R}$ is by equivalence classes of Cauchy sequences in $\mathbb{Q}$. Unlike Dedekind cuts, this method generalizes to "completing" arbitrary normed vector spaces, which creates some other interesting structures.

### Cauchy Sequences
A Cauchy sequence in $\mathbb{Q}$ can be thought of as a sequence which converges, but not necessarily to a particular rational number. The idea of "completing" the rationals is to create new numbers until every Cauchy sequence converges.

Since we don't have these new numbers yet, we need a different definition of Cauchy sequences. A Cauchy sequence's terms get closer and closer to *each other* rather than a particular convergence point. More formally:

> A sequence $(a_n)$ is *Cauchy* if for all $\varepsilon>0$ there exists some $N$ such that for all $m,n > N$ we have $\vert a_m - a_n\vert < \varepsilon$.

<details><summary>
<strong>Theorem:</strong> Every convergent sequence is Cauchy.
</summary>

<div markdown="1">
Suppose $(a_n)\to a$ and fix $\varepsilon>0$. Then we can choose $N$ such that for all $n>N$ we have $|a_n - a| < \varepsilon/2$. Then for any $m,n > N$, we have
$$|a_m - a_n| < |a_m - a| + |a_n - a| < \varepsilon,$$
thus $(a_n)$ is Cauchy.
</div>
</details>

The converse is not true for $\mathbb{Q}$, but it will be for $\mathbb{R}$.

### The Construction of $\mathbb{R}$ by Equivalence Classes

> Two Cauchy sequences $(a_n)$ and $(b_n)$ are called *equivalent* if $(a_n-b_n)\to 0$. In this case we write $(a_n)\sim(b_n)$.

<details markdown="1"><summary>
<strong>Theorem:</strong> Equivalence of Cauchy sequences is an equivalence relation.
</summary>

<div markdown="1">
* It's clear that $(a_n)\sim (a_n)$.
* Also, we have $(a_n)\sim(b_n) \implies (b_n)\sim(a_n)$ because for any sequence converging to 0, it's negative will also converge to 0.
* Since the sum of two sequences converging to 0 also converges to 0 (why?), transitivity holds.
</div>
</details>

> The *real numbers* $\mathbb{R}$ are the equivalence classes of Cauchy sequences. For a given Cauchy sequence $(a_n)$, $\lim a_n$ is a real number defined as the equivalence class containing $(a_n)$.

Also, we define the inclusion map $\iota:\mathbb{Q}\to\mathbb{R}$ to be $\iota(q) = \\{(a_n)\mid (a_n)\text{ converges to $q$ in the rationals }\\}$, so that $\mathbb{Q}$ is essentially a subset of $\mathbb{R}$.

### Addition and Subtraction

The four basic operations are all defined elementwise for Cauchy sequences. We now need to show that these operations are well defined for equivalence classes, and that rational arithmetic remains unchanged.

<details><summary>
<strong>Theorem:</strong> If $(a_n)$ and $(b_n)$ are Cauchy, then $(a_n + b_n)$ is Cauchy.
</summary>
<div markdown="1">

Fix $\varepsilon>0$, and choose $N$ so that for all $m,n\ge N$ we have both $\vert a_m - a_n\vert < \varepsilon/2$ and $\vert b_m - b_n\vert < \varepsilon/2$. Then we have

$$|(a_m + b_m) - (a_n + b_n)| \le |a_m - a_n| + |b_m - b_n| < \varepsilon.$$

</div>
</details>

<details><summary>
<strong>Theorem:</strong> If $(a_n),(a'_n),(b_n)$ are all Cauchy and $(a_n)\sim(a'_n)$, then $(a_n+b_n)\sim(a'_n+b_n)$, and so addition in $\mathbb{R}$ is well defined.
</summary>
<div markdown="1">

We have $\vert (a_n+b_n) - (a'_n+b_n)\vert = \vert a_n - a'_n\vert$ so the result is immediate.

</div>
</details>

<details><summary>
<strong>Theorem:</strong> Suppose that $(a_n)\to a$ and $(b_n)\to b$ in the rationals. Then $(a_n+b_n)\to a+b$.
</summary>
<div markdown="1">

Fix $\varepsilon > 0$. Choose $N$ so that
$|a_n - a| < \varepsilon/2$ and
$|b_n - b| < \varepsilon/2$ for all $n\ge N$. Then we have

$$|(a_n + b_n) - (a + b)| \le |a_n - a| + |b_n - b| < \varepsilon.$$

</div>
</details>

Finally, we should check that the structure we expect of addition holds, which is pretty simple.

<details><summary>
<strong>Theorem:</strong> $(\mathbb{R},+)$ is an abelian group.
</summary>
<div markdown="1">

* Associativity and commutativity are easy to check.
* $\lim(0,0,\dots)$ is the identity.
* $\lim(-a_1,-a_2,\dots)$ is the inverse of $\lim(a_1,a_2,\dots)$.
  * The inverse is Cauchy because distances between terms are preserved, and that's the only thing used in the definition.

</div>
</details>

Subtraction is defined using the additive inverse.

### Multiplication and Division

Defining multiplication is done in a similar way, although verifying that it's well defined is harder.

<details><summary>
<strong>Theorem: </strong> If $(a_n)$ and $(b_n)$ are Cauchy, so is $(a_nb_n)$.
</summary>
<div markdown="1">

* Fix $\varepsilon > 0$. 
* Since Cauchy sequences are bounded, choose $M > 0$ such that $\vert a_n\vert < M$ and $\vert b_n\vert < M$ for all $n$.
* Choose $N$ so that for all $m,n\ge N$ we have

$$|a_m-a_n| < \varepsilon/2M,\qquad |b_m-b_n| < \varepsilon/2M$$

Then for all $m,n\ge N$,

$$
\begin{align*}
  |a_mb_m - a_nb_n| &= |a_mb_m - a_mb_n + a_mb_n - a_nb_n| \\
  &\le |a_m||b_m-b_n| + |b_n||a_m-a_n| \\
  &\le M(|a_m-a_n| + |b_m-b_n|) \\
  &< M\left(\frac{\varepsilon}{2M} + \frac{\varepsilon}{2M}\right) = \varepsilon.
\end{align*}
$$

</div>
</details>

<details><summary>
<strong>Theorem: </strong> If $(a_n),(a'_n),(b_n)$ are Cauchy and $(a_n)\sim(a'_n)$, then $(a_nb_n)\sim(a'_nb_n)$.
</summary>
<div markdown="1">

* Fix $\varepsilon>0$.
* Since $(b_n)$ is Cauchy, we can choose some $M$ as an upper bound for $(b_n)$.
* Choose $N$ so that $\vert a_n - a'_n\vert < \varepsilon/M$ for all $n\ge N$.
* Then $\vert a_nb_n - a'_nb_n\vert  = \vert b_n\vert\vert a_n-a'_n\vert \le M\vert a_n-a'_n\vert  < \varepsilon$.

</div>
</details>

<details><summary>
<strong>Theorem: </strong> If $(a_n)\to a$ and $(b_n)\to b$ in the rationals, then $(a_nb_n)\to ab$.
</summary>
<div markdown="1">

* Fix $\varepsilon>0$.
* Choose $M>b$ as an upper bound for $(a_n)$.
* Choose $N$ such that for all $n\ge N$ we have
  $|a_n - a| < \varepsilon/2M$ and
  $|b_n - b| < \varepsilon/2M$.
* Then for all $n\ge N$,

$$
\begin{align*}
  |a_nb_n - ab| &= |a_nb_n - a_nb + a_nb - ab| \\
  &\le |a_n||b_n-b| + |b||a_n-a| \\
  &\le M(|a_n-a| + |b_n-b|) \\
  &< M\left(\frac{\varepsilon}{2M} + \frac{\varepsilon}{2M}\right) = \varepsilon.
\end{align*}
$$

</div>
</details>

Now for division:

<details><summary>
<strong>Theorem: </strong> If $(a_n)$ is Cauchy and nonzero, with all of it's terms nonzero, then $(1/a_n)$ is Cauchy.
</summary>
<div markdown="1">

* Fix $\varepsilon>0$.
* Since $(a_n)\not\to 0$, we can choose $\delta>0$ such that $\vert a_n\vert > \delta$ for all $n$.
* Choose $N$ so that for all $m,n\ge N$ we have $\vert a_m - a_n\vert < \delta^2\varepsilon$. Then we have

$$\left|\frac{1}{a_m}-\frac{1}{a_n}\right| = \frac{|a_m-a_n|}{|a_ma_n|} < \frac{\delta^2\varepsilon}{\delta^2} = \varepsilon.$$

</div>
</details>

<details><summary>
<strong>Theorem: </strong> If $(a_n),(a'_n)$ are nonzero equivalent Cauchy sequences, then $(1/a_n)\sim(1/a'_n)$.
</summary>
<div markdown="1">

* Fix $\varepsilon>0$.
* Since $(a_n)$ and $(a'_n)$ are nonzero, we can choose $\delta>0$ so that $\vert a_n\vert>\delta$ and $\vert a'_n\vert>\delta$ for all $n$.
* Choose $N$ so that for all $n\ge N$ we have $\vert a_n - a'_n\vert < \delta^2\varepsilon$. Then we have

$$\left|\frac{1}{a_n}-\frac{1}{a'_n}\right| = \frac{|a_n-a'_n|}{|a_na'_n|} < \frac{\delta^2\varepsilon}{\delta^2} = \varepsilon.$$

</div>
</details>

<details><summary>
<strong>Theorem: </strong> If $(a_n)\to a\ne 0$, then $(1/a_n)\to 1/a$.
</summary>
<div markdown="1">

* Fix $\varepsilon>0$.
* Choose $\delta>0$ such that $\vert a_n\vert > \delta$ for all $n$, and
  $|a|>\delta$. The proof from here is essentially the same as the previous one.

</div>
</details>

Now that we've shown that multiplication are well defined and respect rational arithmetic, we can state some structure theorems. These are about as easy as the previous ones.

<details><summary>
<strong>Theorem: </strong> $(\mathbb{R},+,\cdot)$ forms a field.
</summary>
<div markdown="1">

* That $(\mathbb{R},+)$ is an abelian group has been determined.
* Multiplication is associative, commutative, and distributes over addition by properties of $\mathbb{Q}$.
* $(1,1,\dots)$ is the multiplicative identity.
* $(1/a_1,1/a_2,\dots)$ is the multiplicative inverse of $(a_1,a_2,\dots)$.
* $0\ne 1$, as the difference $(1,1,\dots)$ doesn't converge to 0.

</div>
</details>


### Comparison

Comparison is a bit more difficult to define than arithmetic, but it's not too difficult. We will define positive and negative first:

> * $(a_n)$ is positive if there is some $\varepsilon>0$ such that $(a_n) > \varepsilon$ for almost all $n$.
> * $(a_n)$ is negative if $-(a_n)$ is positive.
> * $(a_n) < (b_n)$ if $(b_n - a_n)$ is positive.
> * $(a_n) \le (b_n)$ if $(b_n - a_n)$ is positive or zero.

It's useful to have a good characterization of strict inequality.

We shall make sure this is well defined:

<details><summary>
<strong>Theorem: </strong> If $(a_n)$ is positive and $(a_n)\sim(a'_n)$, then $(a'_n)$ is positive.
</summary>
<div markdown="1">

* Choose $\varepsilon>0$ such that
  $a_n > \varepsilon$ and
  $a'_n > a_n - \varepsilon/2$ for almost all $n$.
* Combining the inequalities, we get $a'_n > \varepsilon/2$ for almost all $n$, so $(a'_n)$ is positive.

</div>
</details>

Since $<$ and $\le$ are defined from previous real operations, they are well defined. For verifying consistency with rational numbers, it suffices to look at constant sequences. Now we will show that $\le$ is a total order:

<details><summary>
<strong>Theorem: </strong> $\le$ is a total ordering of $\mathbb{R}$.
</summary>
<div markdown="1">

* **Reflexivity:** A sequence is equivalent to itself since $(0,0,\dots)\to 0$.
* **Transitivity:** Suppose that $(a_n)\le (b_n)$ and $(b_n)\le (c_n)$. If either are equivalent, the result follows from $\le$ being well defined.
  * Assume the inequalities are strict, as this form of transitivity will help later.
  * We can choose $\varepsilon_1,\varepsilon_2>0$ so that for almost all $n$, we have $b_n - a_n > \varepsilon_1$ and $c_n - b_n > \varepsilon_2$.
  * Adding these, we get $c_n - a_n > \varepsilon_1 + \varepsilon_2$, showing that $(a_n) < (c_n)$.
* **Antisymmetry:** Suppose that $(a_n) < (b_n)$ and $(b_n) < (a_n)$. By transitivity of the strict inequality, this implies $(a_n) < (a_n)$, which is a contradiction.
* **Trichotomy:** Assume that infinitely many terms of $(a_n)$ are nonnegative and infinitely many are negative. We will show that $(a_n)\to 0$.
  * Fix $\varepsilon>0$ and choose $N$ so that for all $m,n\ge N$ we have
    $|a_m-a_n|<\varepsilon/2$.
  * In particular, we can choose $m,n\ge N$ such that $a_m\ge 0$ and $a_n < 0$.
  * Then $|a_m| = a_m-a_n+a_n < \varepsilon/2$.
  * For any $j\ge N$ we have $|a_j|\le |a_m - a_j| + |a_m| < \varepsilon$, thus $(a_n)\to 0$.
* Now assume that almost all terms are nonnegative. We can check that $(a_n)$ is positive or zero in this case.
* If almost all terms are negative, we can verify that $(a_n)$ is negative or zero.
* In all cases, $(a_n)$ is definitely positive, negative, or zero.

</div>
</details>

And now we verify the ordered field properties relating to arithmetic.

<details><summary>
<strong>Theorem: </strong> $\mathbb{R}$ is an ordered field.
</summary>
<div markdown="1">

* Suppose that $(a_n) < (b_n)$. Then we have $(a_n) + (c_n) < (b_n) + (c_n)$ by rational arithmetic.
* Suppose that $(a_n) > 0$ and $(b_n) > 0$. Then we know that $(a_n)$ is almost always bounded below by some $\varepsilon_1$ and $(b_n)$ is by some $\varepsilon_2$, thus $(a_nb_n)$ is almost always bounded below by $\varepsilon_1\varepsilon_2$.

</div>
</details>


### Completeness

Now for the big moment! We will show that the completeness axiom holds for these Cauchy sequences. This is quite challenging! To do this, we need to construct a Cauchy sequence to be our candidate for the least upper bound.

<details><summary>
<strong>Theorem: </strong> Every nonempty bounded set in $\mathbb{R}$ has a least upper bound.
</summary>
<div markdown="1">

Let $S\subseteq\mathbb{R}$ be nonempty and bounded, let $y_0$ be a rational upper bound of $S$, and let $x_0$ be a rational non upper bound of $S$. We will define the sequences $(x_n)$ and $(y_n)$ recursively as

$$\begin{align*}
  x_{n+1} &= \begin{cases}
    \frac{x_n + y_n}{2} & \text{if this is not an upper bound} \\
    x_n & \text{otherwise}
  \end{cases} \\
  y_{n+1} &= \begin{cases}
    \frac{x_n + y_n}{2} & \text{if this is an upper bound} \\
    y_n & \text{otherwise.}
  \end{cases}
\end{align*}$$

It's easy to see that $(x_n)$ and $(y_n)$ are equivalent Cauchy sequences. I claim that they converge to the least upper bound.
* Since each term of $(y_n)$ is an upper bound of $S$, it's limit is an upper bound.
* Suppose there was some upper bound $(z_n) < (x_n)$.
  * Then choose $\varepsilon>0$ such that $x_n - z_n > \varepsilon$ for almost all $n$.
  * Because of this and the fact that $(x_n)$ and $(z_n)$ are Cauchy, we can choose $q$ such that $z_n < q < x_n$ for almost all $n$.
  * Choose $s\in S$ such that $s>q$. This is possible since $x_n$ consists of non upper bounds
  * Now $z_n$ is not an upper bound.
* So we've found the least upper bound!

</div>
</details>


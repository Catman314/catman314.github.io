---
title: Rearrangement of Infinite Series
author: Catman
layout: post
long: true
---

> As I was reading Abbott's *Understanding Analysis*, I came upon the theorem stating that if a series converges absolutely, then any rearrangement of the series converges to the same value. I 

### Rearranged Sums are Weird

The first thing I did was look back at the example from Section 2.1, where

$$
\begin{align*}
  s &= 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \frac{1}{7} - \frac{1}{8} + \frac{1}{9} - \dots \\
  t &= 1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \frac{1}{9} + \frac{1}{11} - \frac{1}{6} + \dots.
\end{align*}
$$

It turns out that $t = 1.5 s$, so these sums are not equal even though they have the same terms.

Let $(a_n)$ be the sequence $(1,-\frac{1}{2},\frac{1}{3},\dots)$, who's sum is $s$. Then we have

$$t = a_1 + a_3 + a_2 + a_5 + a_7 + a_4 + a_9 + a_{11} + a_6 + \dots.$$

Now look at, say, the first 13 terms of this rearranged series, and with the indices sorted.

$$
\begin{align*}
  \sum_{k=1}^13 a_{\sigma(k)} &= a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + a_8 + a_9 + a_{11} + a_{13} + a_{15} + a_{17} \\
  &= \sum_{k=1}^9 a_k + a_{11} + a_{13} + a_{15} + a_{17}
\end{align*}
$$

One observation is that the sum includes all of the first 9 terms. If we keep adding more and more of the rearranged series, the number of initial terms will get arbitrarily large. We also know that the sum of these initial terms gets arbitrarily close to $s$.

But there are also extra terms outside those initial terms, and these extras can cause problems for us. In our particular example, the number of extra terms increases over time. They are also all positive with no negative terms to balance it out, and this actually ends up adding a bit extra to the sum.

### But I Want to Rearrange :(

We've seen that when summing the rearranged series, there is a split between *initial terms* and *extra terms*. The initial terms are very well behaved, approaching $s$ over time, but the extra terms are harder to predict. We want to somehow impose a restriction on the extra terms which makes them negligible over time. Here are some approaches I can think of:

* Limit the sum of the extra terms' absolute values. This can be done by requiring the series to be absolutely convergent.
* Limit the number of extra terms. We can do this by adding a rule that $\sigma(n + k) > n$ for all $n$ and all $k\ge \alpha$.
* A combination of both perhaps?

### The Absolute Convergence Approach

This is the most common form of the rearrangement theorem: If a series converges *absolutely*, then every rearrangement has the same sum.

To prove this, fix $\varepsilon > 0$. Suppose the original series sums to $S$. We want to show that for all $n$ beyond some $N$,

$$\left\vert \sum_{k=1}^{n} a_{\sigma(k)} - S\right\vert < \varepsilon$$

With the idea of initial and extra terms in mind, we define $M$ so that
* We have
  $\left|\sum_{k=1}^M a_k - S\right| < \varepsilon/2$.
* For all $n > m \ge M$ we have
  $\sum_{k=M+1}^\infty |a_k| < \varepsilon/2$. This is possible by absolute convergence.

Now we need to choose $N$ such that $\sigma(1),\sigma(2),\dots,\sigma(N)$ contains all of the indices $1,2,\dots,M$. We define

$$N = \max\{\sigma^{-1}(1),\sigma^{-1}(2),\dots,\sigma^{-1}(n)\}$$

to ensure this. For any $n\ge N$, the set $\sigma(1),\sigma(2),\dots,\sigma(n)$ consists of the initial indices $1,2,\dots,M$, as well as the extra indices which I'll call $n_1,n_2,\dots,n_j$. The rearranged sum is then split into

$$\sum_{k=1}^n a_{\sigma(k)} = \sum_{k=1}^M a_{k} + \sum_{k=1}^j a_{n_k}.$$

Then we have

$$
\begin{align*}
  \left|\sum_{k=1}^M a_{k} + \sum_{k=1}^j a_{n_k} - s\right| &\le \left|\sum_{k=1}^M a_{k} - s\right| + \sum_{k=M+1}^\infty |a_k| \\
  &< \varepsilon/2 + \varepsilon/2 = \varepsilon.
\end{align*}
$$
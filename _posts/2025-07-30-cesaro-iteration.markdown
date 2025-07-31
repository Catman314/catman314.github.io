---
title: A Problem About Cesàro Means
author: Catman
layout: post
long: true
---

> I discuss Cesàro means and a problem I invented about them.

### Cesàro Means

Given a sequence $(a_n)$, we want to find its average. To do this, we can create the sequence of partial averages

$$s_n = \frac{1}{n}\sum_{k=1}^n a_n.$$

This is called the *Cesàro mean* operation.

An exercise I've seen in real analysis is to show that if $(a_n)$ converges, then $(s_n)$ converges to the same value.

<details><summary>
Proof
</summary>
<div markdown="1">

Suppose $(a_n)$ converges to $a$. Fix $\varepsilon > 0$. Choose $N$ so that
$|a_n - a| < \varepsilon/2$ for all $n\ge N$. Let $M$ be an upper bound of $|a_n - a|$. Then for all
$n\ge\max\\{2MN/\varepsilon, N\\}$, we have

$$
\begin{align*}
  |s_n - a| &= \left|\frac{1}{n}\sum_{k=1}^n (a_k - a)\right| \\
  &\le \frac{1}{n}\sum_{k=1}^n |a_k - a| \\
  &= \frac{1}{n}\left[\sum_{k=1}^N |a_k - a| + \sum_{k=N+1}^n |a_k - a|\right] \\
  &\le \frac{1}{n}\left[\sum_{k=1}^N M + \sum_{k=N+1}^n \frac{\epsilon}{2}\right] \\
  &\le \frac{MN}{n} + \frac{n-N}{n}\frac{\varepsilon}{2} \\
  &\le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{align*}
$$

Therefore, $(s_n)\to a$.

</div>
</details>

Also, a lot of sequences which don't converge have partial averages which converge. For example, the sequence $(a_n) = (0,1,0,1,0,1,0,1,\dots)$ doesn't converge, but it seems like the average should be $1/2$. Indeed, the sequence of partial averages converges to $1/2$.

### A Bounded Sequence Without a Cesàro Mean

Unfortunately, we can't assign an average to every bounded sequence. For example, we can create the sequence

$$0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,\dots$$

where the length of the run doubles after each switch. It's not too hard to see that the partial averages oscillate between $1/3$ and $2/3$, so the sequence actually doesn't have an average in this sense. However, by repeating the Cesàro mean operation again and again, the resulting sequence seems to be contained in smaller and smaller intervals. The limit of these intervals could be called the average!

Let $(C^k a_n)$ denote the sequence $(a_n)$ after $k$ iterations of the Cesàro mean. In the graph below, the purple points represent $(a_n)$, the blue points represent $(C^1a_n)$, and the green points represent $(C^2 a_n)$. It seems like $(C^2a_n)$ either already converges to $1/2$, or at least oscillates between two points which are really close together.

![alt text](/assets/2025-07-30-cesaro-example.png)

> **Conjecture**: For this particular sequence,
> 
> $$\lim_{k\to\infty}(\limsup(C^k a_n)) = 1/2 \\ \lim_{k\to\infty}(\liminf(C^k a_n)) = 1/2 $$

At this point I was excited at the possibility of assigning an average value to any bounded sequence! Unfortunately, after thinking about the problem on and off for a while, I came up with a sequence which oscillates between $0$ and $1$ no matter how many applications of the Cesàro mean are used. In hindsight this should have been easier to spot, but that's how hindsight works :)

### A Bounded Sequence With Nonconverging Cesàro Bounds

Below is an important corollary of the exercise.

> If $(a_n)\to a$ and $k$ is a fixed integer, then for every $\varepsilon > 0$, there is some $N$ such that for all $n\ge N$ we have
$|C^j a_n - a| < \varepsilon$.

Here is my algorithm for constructing the sequence.

* Start with $(a_1) = 0$.
* At the $k^{th}$ iteration, we do one of the following steps depending on the parity of $k$:
  * If $k$ is odd, add ones until $C^j a_n > 1 - \frac{1}{k}$ for all $j\le k$.
  * If $k$ is even, add zeros until $C^j a_n < \frac{1}{k}$ for all $j \le k$.

I expect the number of terms in each run of zeros or ones to increase extremely fast.

### A Universal Measure of Average

Can we define a measure of average which can be applied to any bounded sequence? Let $\mu(a_n)$ denote this average. Here are the natural properties I can think of:
* $\mu(a_n + b_n) = \mu(a_n) + \mu(b_n)$
* $\mu(\lambda a_n) = \lambda \mu(a_n)$
* $\mu(a_n) = \mu(a_{n+1})$
* $\lim_{k\to\infty}(\underline{\lim} (C^k a_n)) \le \mu(a_n) \le \lim_{k\to\infty}(\overline{\lim}(C^k a_n))$.

I call such an averaging operator a *Cesàro limit*

> **Question**: Can we define such an average?

#### Banach Limits

I found a weaker version of sequence averages called a *Banach limit*. According to Wikipedia, a Banach limit is an operator $\phi$ such that
* $\phi$ is linear
* If $a_n \ge 0$ for all $n$, then $\phi(a_n)\ge 0$
* $\phi(a_n) = \phi(a_{n+1})$
* If $(a_n)\to a$, then $\phi(a_n) = a$.

My Cesàro limit is a special case of a Banach limit. Apparently, any complete construction of a Banach limit requires the axiom of choice, therefore the Cesàro limit will also require AoC to construct (if it even exists).

### Conclusion

In the future, I will try to show that Cesàro limits exist. It's been put in my [conjectures]({% link conjectures.md%} ) list.
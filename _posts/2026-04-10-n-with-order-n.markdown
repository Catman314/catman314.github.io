---
title: Groups with Exactly $n$ elements of order $n$
author: Catman
layout: post
long: true
---
$\newcommand{\lra}[1]{\left\langle #1 \right\rangle}$
> For what $n$ can there exist a group with exactly $n$ elements of order $n$?

## Intro
In my abstract algebra class, we were given the following problem:
> Let $p$ be an odd prime. Show that there is no group with exactly $p$ elements of order $p$.

This problem was very fascinating to me, and I wanted to see how far I could take it. In this post, I will show exactly for which $n$ there exist groups with exactly $n$ elements of order $n$.

## Solution to the First Problem
Let $G$ be a group.

Suppose we have an element $g\in G$ with order $p$. Then the key is to look at the cyclic group $\lra{g}$, which contributes an entire $p-1$ elements with order $p$ (everything except the identity).

Looking at all these cyclic subgroup, we end up separating the elements of order $p$ into clusters of size $p-1$, as shown in this flower-like diagram:

<img src="/assets/images/2026-04-10-cyclic-subgroup-flower.png" width="50%">

If two cyclic subgroups share a common generator, they are clearly the same subgroup, so this really is a partition.

So, the number of elements with order $p$ is a multiple of $p-1$[^1]. If $p\ge 3$, we have

$$p\equiv 1 \not\equiv 0\pmod{p-1}$$

Notice that this fails when $p=2$; $2$ is indeed a multiple of $1$. But as it turns out, we can solve the case $p=2$ a different way!

## $p = 2$

If a group $G$ has two elements of order $2$, say $g$ and $h$, then
* If $G$ is abelian, then $gh$ is a third element of order 2
* If $G$ is nonabelian, then $ghg^{-1}$ is a third element of order 2

A side question: If $G$ is *finite*, then the number of elements with order $2$ is odd, which is seen by noting that
$|G|$ is even and the elements with order greater than $2$ can be paired by inverses. Is this also true when $G$ is infinite?

I suspect that something like this can be done with larger values of $p$ also.

## General $n$

Now consider any positive integer $n > 1$. The flower diagram of elements with order $n$ is still valid, but there may not be exactly $n-1$ generators in each petal.

Instead, there will be $\phi(n)$ in each cluster, where $\phi(n)$ is the number of positive integers up to $n$ relatively prime to $n$. The function $\phi$ is called *Euler's totient function*, and has some very nice properties. Importantly for us, we can use the prime factorization of $n$ to evaluate $\phi(n)$ in closed form:

$$\phi(n) = \phi(p_1^{a_1}\dots p_k^{a_k}) = n\cdot\frac{p_1-1}{p_1}\cdots\frac{p_k-1}{p_k}$$

If $G$ has exactly $n$ elements of order $n$, then we must have $\phi(n)\mid n$.

### Solving $\phi(n)\mid n$

Let $n = p_1^{k_1}\dots p_k^{a_k}$, where $p_k$ is the largest prime factor of $n$. In order for $\phi(n)\mid n$ to be true, we must have

$$\frac{p_1-1}{p_1}\cdots\frac{p_k-1}{p_k} = \frac{1}{M}$$

for some integer $M$. Notice that the prime factor $p_k$ cannot be canceled from the denominator because every term in the numerator is below $p_k$. Therefore, $M\ge p_k$.

On the other hand, we can get the reverse inequality by inserting more terms on the left product:

$$\frac{1}{p_k} = \prod_{j=2}^{p_k}\frac{j-1}{j} \le \frac{p_1-1}{p_1}\cdots\frac{p_k-1}{p_k} = \frac{1}{M} \implies M \le p_k.$$

Therefore, $M = p_k$. This is a huge restriction! Now, we have

$$\prod_{j=2}^{p_k}\frac{j-1}{j} = \frac{p_1-1}{p_1}\cdots\frac{p_k-1}{p_k},$$

so the prime factors of $n$ must include every integer from $2$ to $p_k$ in order to keep the equality. So $$p_k\in\{2,3\}$$. This means $n$ has the form $2^{j}3^{k}$, where $j > 0$.

### Finding Groups

Now suppose $n = 2^{j}3^{k}$ with $j > 0$. We want to find a group with $n$ elements of order $n$. We've seen that this is impossible with $n = 2$, but what about the other cases?

If $n = 2^{j}$ with $j > 1$, then the group $\mathbb{Z}_n\times\mathbb{Z}_2$ is what we're looking for.

If $n = 2^{j}3^{k}$ with $j,k > 0$, then the group $\mathbb{Z}_n\times\mathbb{Z}_3$ works.


## Conclusion

> If $n\in\mathbb{N}$, there exists a group with exactly $n$ elements of order $n$ if and only if
> * $n = 1$ or
> * $n > 2$ and $n = 2^{j}3^{k}$ for some $j>0,k\ge 0$.

There is still more left to discover. For example:

* If a group has elements of order 2, is that count an odd number, even when the group is infinite?
* Are there any more restrictions on the number of elements with order $n$, besides being a multiple of $\phi(n)$? The case of $n=2$ seems to indicate this.

---



[^1]: or infinite. We'll ignore that case.
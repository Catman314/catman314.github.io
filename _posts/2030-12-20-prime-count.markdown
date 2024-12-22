---
layout: post
title:  "Counting Primes Quickly"
date:   2030-12-20 15:43:00 -0500
published: false
---


## Intro
Using the sieve of Eratosthenes, we can calculate primes up to $N$ in $O(N\log\log N)$ time. This is great for finding every prime, but what if we just want to count them, or find their sum? Do we necessarily need to find every prime in order to count them?

## The Approach
Let's start running the sieve of Eratosthenes for $N = 1000$, but instead of crossing out values manually, we will just count how many values are crossed out.
* We start with every number from 2 to 1000 not crossed. There are 999 of these
* Now cross out all multiples of 2. We are left with 500 not crossed out.
* Now cross out all multiples of 3 which aren't multiples of 2. We are left with 169 not crossed out.
* Now cross out all multiples of 4 (there are none to cross out because 4 is composite).
* Now cross out all multiples of 5 which aren't multiples of 3 or 2, and so on.

In general, let $\mathbb{P}(k)$ be the set of integers which are not crossed off by any primes up to $k.$
We have

> $$a \in \mathbb{P}(k) \iff \text{ Every proper divisor of $a$ is larger than $k$}.$$

We want to find the number of elements of $\mathbb{P}(k-1) \setminus \mathbb{P}(k)$ which do not exceed $n$. Letting $\mathbb{P}_{\le n}(k)$ denote the elements of $\mathbb{P}(k)$ which don't exceed $n$, we have the following:

---

$$
\begin{align*}
  a\in \mathbb{P}(k-1) \setminus \mathbb{P}(k) &\iff \text{$k$ is the smallest proper divisor of $a$} \\
  &\iff \text{$k$ is prime and } a = kj \text{ for some $j \ge k$ such that every proper divisor of $j$ is at least $k$} \\
  &\iff \text{$k$ is prime and } a = kj \text{ for some $j \ge k$ such that $j\in\mathbb{P}(k-1)$} \\
  a\in \mathbb{P}_{\le n}(k-1) \setminus \mathbb{P}_{\le n}(k) &\iff \text{$k$ is prime and }  a = kj \text{ for some $j\ge k$ such that $j\in\mathbb{P}_{\le n/k}(k-1)$} \\
  &\iff \text{$k$ is prime and }  a = kj \text{ for some $j\in\mathbb{P}_{\le n/k}(k-1)\setminus \mathbb{P}_{\le k-1}(k-1)$ } \\
  \mathbb{P}_{\le n}(k-1) \setminus \mathbb{P}_{\le n}(k) &= \begin{cases}
    k(\mathbb{P}_{\le n/k}(k-1)\setminus \mathbb{P}_{\le k-1}(k-1)) & \text{$k$ is prime} \\
    \emptyset & \text{$k$ isn't prime}.
  \end{cases}
\end{align*}
$$

---

Here are some key properties of $\mathbb{P}_{\le n}(k)$.
* If $k$ is composite, then $\mathbb{P}_{\le n}(k) = \mathbb{P} _{\le n}(k-1).$
* $\mathbb{P}_{\le n}(\sqrt{n})$ is the set of primes not exceeding $n$.

We can do a few things from here, such as taking the cardinality or the sum of both sides. We end up with a recurrence for the prime count and prime sum respectively. In general, if $F(X) = \sum_{n\in X} f(n)$, where $f(n)$ is completely multiplicative, we can get interesting results. Letting $F(n,k) := F\left(\mathbb{P}_{\le n}(k)\right)$, we have

$$
\begin{align*}
  F(n,1) &= \sum_{i=2}^n f(i) \\
  F(n,k) &= F(n,k-1) - f(k)\left[F(n/k,k-1) - F(k-1,k-1)\right]
\end{align*}$$

for $k \le \sqrt{n}$.

If $f(n)$ can be summed quickly, the base case is solved. The only $f$ we will consider here are of the form $f(n) = n^a$, where $a$ is a positive integer.

## Dynamic Programming
We need to determine which values of $F(n,k)$ need to be computed to find $F(N,\sqrt{N})$. By experimenting a bit, we come across the result: We need to compute $F(n,k)$ only if $n = \floor{N/j}$ for some integer $j$. As an example, if $N = 70$, we need to compute $F(n,k)$ only if 

$$n\in \{1,2,3,4,5,6,7,8,10,11,14,17,23,35,70\}.$$

The numbers 1 through 8 may be covered by multiple $j$ values, but the values $10,11,14,\dots$ come from $\frac{70}{7}, \frac{70}{6}, \frac{70}{5},\dots$.

In general, the numbers from 1 to $\sqrt{N}$ always appear, and after that they start spacing out more.
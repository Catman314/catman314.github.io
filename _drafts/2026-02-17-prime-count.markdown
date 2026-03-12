---
title: Fastly Counting, Summing, and Multiplying Primes
author: Catman
layout: post
long: true
---

Credits to LucyHedgehog for posting this algorithm in the thread of Project Euler problem 10.

### The Sieve of Eratosthenes
#### Basic Algorithm
The sieve of Eratosthenes is a classic algorithm used to list every prime up to some limit $N$. The algorithm starts by listing every integer in the range $2\dots N$. Then,

* *Step 2*: Cross off all the multiples of $2$ (except $2$ itself)
* *Step 3*: Cross off all the multiples of $3$ (except $3$ itself)
* etc.

In the end, only prime numbers will survive.

#### Some Optimizations
* At a given step $k$, if $k$ is composite, crossing off multiples of $k$ is redundant. We only need to do steps where $k$ is prime.
* After step $\floor{k}$, any remaining composite number $m = d_1 d_2$ must have $d_1 > k$ and $d_2 > k$, meaning $m > k^2$. Therefore, every uncrossed integer not exceeding $k^2$ will be prime at this point. In particular, after crossing off multiples up to $k = \sqrt{N}$, we are done!
* By similar reasoning, before step $k$, every uncrossed integer below $k^2$ will be prime. We only need to cross multiples of $k$ from $k^2$ onward.


### Counting, Not Listing
Suppose we just want to count the primes up to $N$. Can we keep track without a big list? Notice that when we cross off multiples of 2, it is very easy to count how many remain.

Let $C(N,x)$ denote how many numbers remain after removing multiples up to $k$.
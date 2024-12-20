---
layout: post
title:  "Proving the Validity of the Sieve of Eratosthenes"
date:   2024-12-20 09:32:15 -0500
---


## The Sieve of Eratosthenes
The sieve of Eratosthenes is a very good way to generate every prime up to some limit $N.$ The algorithm takes an input $N$ and returns a boolean array `is_prime` with size $N+1$ such that `is_prime[n] = true` if and only if `n` is prime. Here is the algorithm written in python.
```py
def sieve(N):
  is_prime = [True]*(N+1)
  is_prime[0] = False
  is_prime[1] = False

  i = 2
  while i*i <= N:
    if is_prime[i]:
      for m in range(i*i, N+1, i):
        is_prime[m] = False
    i += 1
  return is_prime
```

### Proving Correctness
We will pretend that all indexes of `is_prime` are at least 2 (it's easy to see that indexes 0 and 1 will never change).
#### Loop Invariant
The idea is that at the start of each loop, `is_prime[n] = False` if and only if

$$\exists d, (d \mid n$$ and $$1 < d < n$$ and $$d < i).$$

This is called a *loop invariant*, and it's what we use to verify algorithms involving loops. We prove that a loop invariant holds by induction, so first consider the base case $i=2.$ Note that there is no $d$ such that $1<d<2$, so the base case is true.

For the inductive step, suppose the loop invariant is true for some $i\ge 2$. We will see what happens when we run just one iteration of the loop, and hopefully the loop invariant remains true.

#### Induction
There are two cases depending on whether `is_prime[i]` is true or false. Let's start by assuming `is_prime[i] = True`. After running the loop, our state becomes
<center>
<div markdown="1">
`is_prime[n] = False` if and only if <br/> $\exists d, (d\mid n $ and $ 1 < d < n $ and $ d < i)$ <br/> or $n=ik$ for some $k\ge i$.
</div> 
</center>

Running the loop caused that second possibility to appear. Note that if $n=ik$ where $1 < k < i,$ the first condition is satisfied with $d=k.$ We can use this to show that our state is equivalent to

<center>
<div markdown="1">
`is_prime[n] = False` if and only if <br/> $\exists d, (d\mid n $ and $ 1 < d < n $ and $ d < i+1).$
</div> 
</center>

After incrementing $i,$ we see that our loop invariant still holds. Notice that we never actually use the assumption that `is_prime[i] = True`, which means we could actually remove the `if` statement. The only reason it's there is that it decreases runtime. We still need to prove that we can skip the inner loop when `is_prime[i] = False`. In other words, if $i$ is composite, we will show that

$$\exists d, (d\mid n \text{ and } 1 < d < n \text{ and } d < i) \iff \exists d', (d'\mid n \text{ and } 1 < d' < n \text{ and } d' < i+1)$$

The forward direction is clear. To prove the backward direction, if $d' < i$ we are done, so assume that $d' = i.$ Since $i$ is composite, there is a divisor $d\mid i$ such that $1 < d < i.$ Since $d\mid i$ and $i\mid n,$ we have $d\mid n$, thus the LHS is satisfied by $d.$

To summarize, the loop invariant holds after every iteration.

#### After The Loop
The loop will terminate when $i^2 > N$. Since we are at the end, for all $n\le N$ we should have `is_prime[n] = True` if and only if $n$ is prime. We want to show that our current loop invariant is equivalent to $n$ being composite, so

<center>
<div markdown="1">
$\exists d, (d\mid n $ and $ 1 < d < n $ and $ d < i) \iff n$ is composite.
</div> 
</center>

Clearly the forward direction is true. For the backward direction, assume that $n$ is composite, so $n = d\cdot d'$ where $1 < d \le d' < n.$ Then we have $d \le \sqrt{n} < i,$ so $d$ satisfies the condition on the LHS.

QED.

### Takeaway
Proving the correctness of an algorithm can give an idea of how it works at a deep level. By looking at the loop invariant, we see exactly what happens when we use the sieve of Eratosthenes.

TO BE CONTINUED with runtime analysis
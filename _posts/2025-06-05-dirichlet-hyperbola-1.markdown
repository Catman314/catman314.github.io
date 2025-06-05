---
layout: post
title: "The Dirichlet Hyperbola Method"
tags: [notes]
series: "Dirichlet Hyperbola Method"
series-index: 0
---

## Prerequisites
A good basic understanding of multiplicative functions and their Dirichlet series is expected for this post.
I might do a prequel explaining those in the future.

## The Dirichlet Hyperbola Method
Let $R$ be an integral domain with fraction field $F$. Given functions $f,g:\mathbb{N}\to F$, recall that their *Dirichlet convolution* $h = f\star g$ is defined as

$$h(n) = \sum_{ij = n}f(i)g(j).$$

Also, if $f(1)\ne 0$, then $f$ always has a *Dirichlet inverse* $f^{-1}$ such that $f\star f^{-1} = I$, where $I(n) = [n=1]$ is the identity function for Dirichlet convolution.

One can check that $(F^{\mathbb{N}},+,\star)$ forms a ring, but addition isn't particularly interesting in this post. We will only consider the group $(F^{\mathbb{N}},\star)$ of functions with Dirichlet inverses, and it's maximal subgroup contained within $R^{\mathbb{N}}$.

We are interested in the prefix sums $F,G,H$ of $f,g,h$, respectively. We have

$$H(n) = \sum_{ij\le n} f(i)g(j).$$

This sum can be split up in many ways based on a selection of $a,b\in\mathbb{R}$ such that $ab = n$. We have

$$H(n) = \sum_{i\le a}f(i)G(n/i) + \sum_{j\le b}g(j)F(n/j) - F(a)G(b),$$

where $F(x) = F(\floor{x})$ for all $x$, and similarly $G(x) = G(\floor{x})$. This formula can be proven with the inclusion-exclusion principle, splitting the original formula into cases where $i\le a$, $j\le b$, or both.

Let's look at some examples.


### Examples

Let $f(n) = g(n) = 1$. Then $h = f\star g$ is the divisor counting function. Letting $a = b = \sqrt{n}$, the Dirichlet hyperbola method tells us

$$H(n) = 2\sum_{i\le\sqrt{n}}\floor{n/i} - \floor{\sqrt{n}}^2$$

---

Now let $f(n) = 1$ if $n$ is odd and $0$ if $n$ is even, and let $g(n) = 1$. Then $h(n)$ counts the odd divisors of $n$. We get

$$H(n) = \sum_{\substack{i\le\sqrt{n} \\ \text{$i$ odd}}}\floor{n/i} + \sum_{j\le\sqrt{n}}\floor{(n/j+1)/2} - \floor{\frac{\sqrt{n}+1}{2}}\floor{\sqrt{n}}$$

---

Now let $f(n)$ and $g(n)$ both be the odd number detectors. Then $h = f\star g$ will be the divisor count function for odd numbers, and zero for even numbers. We have

$$H(n) = 2\sum_{\substack{i\le\sqrt{n} \\ \text{$i$ odd}}} \floor{(n/i+1)/2} - \left(\floor{\frac{\sqrt{n}+1}{2}}\right)^2.$$

---

The important thing in all these examples is that we can compute these sums very quickly in $O(\sqrt{n})$ compared to the more straightforward $O(n)$ methods.

## Outro

I have explained the Dirichlet hyperbola method along with a few examples. In the next post, I will describe a general algorithm to calculate prefix sums of Dirichlet convolutions and inverses in $O(n^{2/3})$ time.
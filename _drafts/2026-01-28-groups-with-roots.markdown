---
title: Adding roots to groups
author: Catman
layout: post
long: true
---

I want to see if groups can be extended by adding new elements in a way so that $n^{th}$ roots all exist. The most famous example of this is extending $\mathbb{R}$ to $\mathbb{C}$ by including $\sqrt{-1}$. Can this be done with any group?

### Example: $\mathbb{Z}_2$

The simplest group to start with is $\mathbb{Z}_2$. Just to make things nicer, I shall interpret this as the group $\{1,-1\}$ under multiplication.

If $n$ is odd, then there is no problem; every element is its own $n^{th}$ root. But if $n$ is even, then no element will have $-1$ as its square. So we can try inserting $\sqrt{-1} = i$. After combining $i$ with all the group elements, we end up with the group $\{1,i,-1,-i\}$.

But now $i$ has no square root, so we should add a new element to handle this. Ultimately, we end up with a picture like this

![adding more and more sqrts](/assets/2026-01-28-roots-of-unity.png)

After applying this process infinitely, we get a group where square roots exist. It turns out that any $n^{th}$ root already exists as well.

### Generalizing

Given some group $G$, can we extend it to a group in which all elements have roots? I do not know. This seems especially mind bending in the non-abelian case. Even thinking about extending a small group like $D_3$ gets complicated quickly.
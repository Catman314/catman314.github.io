---
title: "Cesàro Means: Binary Sequences"
author: Catman
layout: post
long: true
---

I've recently come back to thinking about Cesàro means, and decided to focus more on the specific example I mentioned in [the previous post](2025-07-30-cesaro-iteration.markdown), a binary sequence $(a_n)$ with runs that double over time. It is rather easy to see that the sequence $(Ca_n)$ oscillates between $1/3$ and $2/3$. In that post, I conjectured that iterating the Cesaro operation will tighten these bounds arbitrarily around $1/2$, so that the Cesaro limit is $1/2$. In this new post, I will show an approach which, while not quite formal, suggests the upper limit $\overline{\lim}(C^2a_n) = 2^{2/3}/3 \approx 0.529133$, as well as further limits which converge quickly to $1/2$.


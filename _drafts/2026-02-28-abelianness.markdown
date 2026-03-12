---
title: Probability of Group Elements Commuting
author: Catman
layout: post
long: true
---

> The probability that two group elements commute is $c/|G|$, where $c$ is the number of conjugacy classes. In this sense, groups with lots of conjugate elements are "less abelian".

Let $G$ be a finite group of order $n$.


#### Examples:

$$
\begin{array}{|c|c|c|}
  G & c/G \\\hline\hline
  S_n & p(n)/n! & \frac{1}{2}, \frac{5}{24}, \frac{7}{120} \\\hline
  D_{n} & \frac{2n+9+3(-1)^n}{8n} \\\hline
  Q_8 & 5/8
\end{array}
$$

Some questions:
* What is the best upper bound? (nonabelian)
* Which fractions appear as probabilities?


Fun fact: $Z(G)$ can't have order $|G|/p$ for any prime $p$. Thus, $|Z(G)| \le |G|/4$. So you have the upper bound $\frac{1}{4} + \frac{1}{2}\cdot\frac{3}{4} = \frac{5}{8}$.
---
title: Commuting Probability of a Group
author: Catman
layout: post
long: true
---

<div style="display: none; max-height: 0px;">$\newcommand{\Cl}{\mathrm{Cl}}$</div>
> The probability that two group elements commute is
> $c/|G|$, where $c$ is the number of conjugacy classes. In this sense, groups with lots of conjugate elements are "less abelian".

## The Formula

Let $G$ be a finite group of order $n$. Let $C(g)$ denote the center of an element $g\in G$, and let $\Cl(g)$ be the conjugacy class of $g$. With respect to the action of $G$ on itself by conjugation, $C(g)$ is the stabilizer of $g$ and $\Cl(g)$ is the orbit of $g$.

The probability that two elements of $G$ commute is given by

$$
\begin{align*}
  \frac{1}{|G|^2}\sum_{g\in G} \sum_{h\in G}[gh = hg] &= \frac{1}{|G|^2} \sum_{g\in G}|C(g)| \\
  &= \frac{1}{|G|^2} \sum_{g\in G} \frac{|G|}{|\Cl(g)|} & \text{by orbit-stabilizer theorem} \\
  &= \frac{1}{|G|}\sum_{g\in G} \frac{1}{|\Cl(g)|}
\end{align*}
$$

Within each conjugacy class $C\subseteq G$, the sum simplifies to
$|C|\cdot \frac{1}{|C|} = 1$. Therefore, the overall sum is just the number of conjugacy classes of $G$. Denoting this by $c$, the probability of two elements commuting is

$$c /|G|$$



### Examples

$$
\begin{array}{|c|c|c|}
  G & c/|G| \\\hline\hline
  S_n & p(n)/n! & \frac{1}{2}, \frac{5}{24}, \frac{7}{120}, \cdots \to 0 \\\hline
  D_{n} & \frac{2n+9+3(-1)^n}{8n} \\\hline
  Q_8 & 5/8
\end{array}
$$

## Which Fractions Appear?

First let's get an upper bound for when $G$ is a nonabelian group. Recall that $[G:Z(G)]$ can't be prime because $G/Z(G)$ is never cyclic, so at most $1/4$ of the elements are in a conjugacy class with one element. The remaining $3/4$ could be split up into pairs at best, which gives us an upper bound of $5/8$. For example, this is achieved by $Q_8$ with these conjugacy classes:

$$\{1\}, \{-1\}, \{i, -i\}, \{j, -j\}, \{k, -k\}.$$

In fact this happens if and only if $[G:Z(G)] = 4$, because every element $x\in G - Z(G)$ satisfies $[G:C_G(x)] = 2$, so the conjugacy classes all have 2 elements.

I wonder if this can be extended to higher indexes of $[G:Z(G)]$, but I can't think of an easy way to tell whether a group is isomorphic to some quotient $G/Z(G)$ (the quotient can't be cyclic; are there any other things it can't be?)

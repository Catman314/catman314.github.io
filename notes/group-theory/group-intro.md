---
layout: default
title: "Intro to Groups"
---
$\newcommand{\End}{\mathrm{Funct}}$
{: .latex-preamble}

# Introduction to Groups

This is the definition of a group:

> A ***group*** is a set $G$ with a binary operation $*:G\times G \to G$ such that
> * The operation is *associative*; for all $a,b,c\in G$ we have $a * (b * c) = (a * b) * c$.
> * There exists an *identity* element $1\in G$ such that $a * 1 = 1 * a = a$.
> * For each element $a\in G$ there exists an *inverse* $a^{-1}$ such that $a * a^{-1} = a^{-1} * a = 1$.
{: .definition }

## Motivation
> The properties of a group form a natural framework for talking about **reversible actions**, a.k.a. symmetry.

Here are some examples:
* Sequences of Rubik's cube algorithms (other twisty puzzles also work)
* Movements which leave geometric objects invariant
  * For instance, $D_n$ for an $n$-sided regular polygon
* $GL_n(\mathbb{F})$, invertible linear transformations from $\mathbb{F}^n$ to itself.

### Why is each group axiom necessary?
* Associativity makes elements of a group behave like actions (think function composition).
* Inverses are included to make the actions reversible (the identity naturally follows).

### Why is each group axiom sufficient?
**Cayley's Theorem** says that every group is isomorphic to a group of permutations. The idea is to correspond each element $g\in G$ with the function $\varphi_g:x\mapsto gx$, which is a permutation of $G$. We have

$$(\varphi_g\circ\varphi_h)(x) = g(hx) = (gh)x = \varphi_{gh}(x),$$

and associativity is all that was needed here.
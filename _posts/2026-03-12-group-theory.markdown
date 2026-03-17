---
title: Intro to Group Theory
author: Catman
layout: post
long: true
---

I've been taking a course on abstract algebra with a big focus on group theory. In this post, I want to summarize my thoughts on the subject so far

### Definition of a Group
For reference, here is the formal definition of a group.

> A *group* is a set $G$ with an operation $\circ:G\times G\to G$ such that
> * The operation is associative.
> * There is an element $1$ called the identity, such that $1\circ g = g\circ 1 = g$ for all $g\in G$.
> * For every $g$, there is an inverse $g^{-1}$ such that $g\circ g^{-1} = g^{-1}\circ g = 1$.

### Motivation
Why is this structure so important? I think the best motivation comes from what are called *group actions*. For instance, consider all the ways you can transform a square without changing its position. Here is a diagram (called a *Cayley graph*) showing these actions.

<img src="/assets/2026-03-02-cayley-graph-dihedral.png" width="75%"/>

The top row contains the 4 rotations, and the bottom row has 4 reflections.

These transformations together form a group called $D_4$, where the operation is composition (which is associative). A very important point is that all of these transformations can be reversed. For example, if you rotate clockwise by $90^{\circ}$, then you can undo this by rotating $270^{\circ}$, and any reflection here is its own inverse.

So with this example in mind, here is a breakdown of why each group axiom is important.
* *Associativity* allows us to think of any binary operation as function composition.
* *Inverses* ensure that every transformation is reversible, in the sense that composing an element with its inverse is the same as doing nothing (the *identity*).

My first claim about associativity was quite bold and needs further explanation.

#### The Importance of Associativity

It's easy to see that function composition is an associative operation. But it actually goes the other way; any set with an associative operation is isomorphic to a set of functions under composition!

<details><summary>
<strong>Theorem: </strong> Every associative binary operation $*:S\times S\to S$ with an identity $1$ is isomorphic to a set of functions under composition (specifically, functions on $S$).
</summary>
<div markdown="1">

*Proof.*
Let $ * $ be an associative binary operation on $S$ with identity $1$. 
For each $x\in S$, let $f_x:S\to S$ be defined by $f_x(y) = x * y$.
We will show $(S,*)$ is isomorphic to
$\\{f_x\mid x\in S\\}$ under function composition. The homomorphism part really comes down to the associative property:

$$(f_{x}\circ f_{y})(z) = x * (y * z) = (x * y) * z = f_{x * y}(z)$$

Also, the map $x\mapsto f_x$ has an inverse, $f_x\mapsto f_x(1)$. That's why the identity is required in this proof.
</div>
</details>

That argument only worked when an identity exists, but we can extend any $(S,*)$ to include an identity element and essentially repeat the same argument.

An example where this would be required is the operation where $x * y = y$. The corresponding left multiplication functions would all be the same! That's the issue solved by adding an identity element.

So what we've shown is that associativity is deeply related with function composition, so I'd say it's quite an important property.
When these transformations can be inverted, we get the wonderful structure of groups.

> *Summary*: Groups can be interpreted as a collection of invertible transformations

I hope this makes groups a bit more interesting and motivated than just a collection of abstract axioms.

### More Examples

* Addition and multiplication acts on $\mathbb{R}$ by shifting and scaling by real amounts. Note that scaling by a factor of zero is not reversible, so not included in the group.
* $n\times n$ matrices are linear transformations of $\mathbb{R}^n$. The linear transformations with inverses form a group.
* A regular $n$-gon can be transformed with $n$ rotations. These rotations form a group called $\mathbb{Z}_n$.
  * You can add in the $n$ reflections, giving you the group $D_n$ which I discussed earlier.
* The move sequences of a Rubik's cube act on its positions.

### Conclusion
Group actions are cool.
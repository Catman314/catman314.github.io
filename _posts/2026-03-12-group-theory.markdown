---
title: Intro to Group Theory
author: Catman
layout: post
long: true
---

After taking a course on group theory, I've decided to write a series giving my thoughts on the subject.

### Motivating the Definition

To truly appreciate how groups work, let's first consider sets of functions. Let $\mathcal{F}$ be a collection of functions from $X$ to itself.

Naturally, we can compose these functions. It can be inconvenient if such a composition were to leave $\mathcal{F}$. So, a nice property for $\mathcal{F}$ is being *closed*, meaning that compositions of functions from $\mathcal{F}$ remain in $\mathcal{F}$.

If $\mathcal{F}$ was not closed, then you can look at the collection $\gen{\mathcal{F}}$ of all ways to compose functions of $\mathcal{F}$. I'll call the *closure* of $\mathcal{F}$, and you can check that this is closed.

#### Associativity

One extremely important property of function composition is associativity; for all $f,g,h\in\mathcal{F}$, we have $f\circ(g\circ h) = (f\circ g)\circ h$. In fact, associativity is the property that makes a binary operation act like function composition.

To see this, suppose we have an associative binary operation on $S$. For each $a\in S$, let $f_a:S\to S$ be the function

$$f_a(x) = a\cdot x$$

Notice that $f_a\circ f_b = f_{a\cdot b}$, so this function composition reflects the original operation.

To summarize, whenever you see an associative operation, think about how the set's elements could act like functions.

#### Groups

To get the idea of a group, start with what we've already done with associativity and function composition.


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
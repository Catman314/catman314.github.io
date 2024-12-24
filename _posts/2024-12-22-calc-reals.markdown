---
layout: post
title:  "What are Real Numbers?"
date:   2024-12-22 09:32:15 -0500
---

This is the first post of a series on calculus.
### Intro
> We all know what real numbers are... just decimal expansions... right?

Real numbers are not just decimal expansions, for a few reasons
* There is nothing special about the number 10; we could choose any base.
* Defining addition, subtraction, multiplication and division based on just the decimal expansion is very tedious. There is a better way.

---
* TOC
{:toc}
---

I will assume the reader knows simple properties of rational numbers.

### The Reals
#### What we Want
There are some basic facts about real numbers we know intuitively. One of them is the following, called the **Archimedian Property**.
> For every real number, there is an integer larger than it.

If we restrict the real number in question to be positive, then we can rewrite it as follows:

> For every positive real number, there is a positive rational number less than it.

*Proof Idea:* For every positive real number $x$, it's reciprocal is also real, thus an integer $n$ lies above $1/x$. Therefore, $1/n < x$, and so we've found a positive rational number less than $x$. $\qquad\square$

We can use this to show the interesting conclusion that there is a rational number in *every interval*. Suppose that $x<y$ and take a number $n$ such that $1/n < y-x$. Now place the integer multiples of $1/n$ on the number line, and you'll find that they are so close together that they can't skip over the interval $(x,y)$!

#### Dedekind Cuts

What follows is the thought process that Dedekind may have had searching for a definition of the real numbers.

1. Between every pair of real numbers there will be a rational number.
2. If $x$ and $y$ are different real numbers, then the rationals greater than $x$ are different than the rationals greater than $y$
    * The different rational number would be the rational between $x$ and $y$.
3. What if we *defined* the real numbers to be these sets of "upper bound rationals"?

Now we're getting somewhere! Let's see our definition now

> **Definition of Reals:** A *real number* is a set $A$ of rational numbers such that
> * $A$ is not empty, but doesn't contain every rational.
> * If $r\in A$, then every rational bigger than $r$ is also in $A$.
> * $A$ has no smallest number.

#### Real Arithmetic
The summary here is that $\mathbb{R}$ is an ordered field. You'll notice that we run into issues with signs, which is annoying. In a future post, I might showcase another way of constructing $\mathbb{R}$ using *Cauchy Sequences*, which doesn't run into this annoying casework and can even be somewhat generalized. For now we will use Dedekind's construction.

* Ordering is simple:

$$x\le y \iff x \supseteq y.$$

* Adding $x$ and $y$ is done by collecting every possible sum of rationals from $x$ and $y$.
    * Exercise: Show that this is well defined, and adding rationals gives the expected result
* Negating $x$: Take the set of rationals $r$ such that $r+x>0$.
    * Exercise: Show that $(\mathbb{R},+)$ is a group.
* Multiplication is a bit annoying because of signs. If $x$ and $y$ are positive, then we can do the same thing as addition.
    * Exercise: Again, show that real multiplication is well defined, and multiplying rationals gives the expected result. (This may require some creativity)
    * What if $x$ or $y$ isn't positive?
    * Show that $(\mathbb{R}, +, \cdot)$ is a ring.
* Reciprocal of $x$: If $x$ is positive, take the set of rationals $r$ such that $\frac{1}{r} < x$.
    * Exercise: Define $1/x$ when $x$ is negative.
    * Show that $(\mathbb{R}, +, \cdot\)$ is an ordered field.


#### The Supremum
What we've done so far with $\mathbb{R}$ is just transferring properties of the rationals to the reals. It's time to introduce things specific to the real numbers.

<details markdown=1>
<summary>
Consider the set

$$\{1/2,2/3,3/4,4/5,5/6,\dots\}.$$

If I ask you to give me an upper bound of this set, what would you say?</summary><br/>
If your immediate thought was $1$, you have good intuition! Even though $1$ isn't in the set, it's still the *least upper bound* we can achieve.
</details>

This is the key to the real numbers: **Every set of real numbers which is bounded above has a least upper bound.** We couldn't do this with the rationals; there are sets of rational numbers who's least upper bound is irrational.

> **Theorem:** If $A$ is a nonempty set of real numbers which is bounded above, then $A$ has a least upper bound.

*Proof Sketch:* Let $S$ be the union of all upper bounds of $A$. It's easy to see that $S$ is a real number less than or equal to every upper bound of $A$. Now we only need to show that $S$ is an upper bound. 

Suppose to the contrary that there is some $a\in A$ such that $a > S$. Choose a rational $r$ such that $a > r > S$. Since $r > S$, there is some upper bound $B$ such that $r > B$. But then $a > B$, so we have a contradiction. $\qquad\square$

> **Definition:** 
* The least upper bound of $A$ is denoted $\sup A$.
* The greatest lower bound of $A$ is denoted $\inf A$ (this is also $-\sup(-A)$).


---
layout: post
title:  "What are roots?"
date:   2024-12-22 09:32:15 -0500
---

In this post, we use least upper bounds to show that $n^{th}$ roots exist. There are better ways of doing this with a bit more knowledge, but I find this a good way to get used to working with least upper bounds.

> **Problem:** Do $n^{th}$ roots always exist in the real numbers?

This is not necessarily a trivial problem, because we know that they don't always exist in $\mathbb{Q}$, e.g. $\sqrt{2}$ is irrational.

### Square Root of $2$

When solving problems, it helps to start with a simple case, so we will start by showing that $\sqrt{2}$ is a real number, i.e. there is a unique positive real number who's square is $2$.

Below is a visual for the solutions of $x^2 < 2$.
<center><img src="/assets/numline-less-sqrt2.png"/></center>
If we take the *least upper bound* of this set, we should get the point on the right marked by a circle. So we let 

$$y = \sup\{x\in\mathbb{R}\mid x^2 < 2\}.$$

We want to show that $y^2 = 2$. Our strategy will be to show that if $y^2 < 2$, then $y$ can't be an upper bound, and if $y^2 > 2$, then $y$ can't be the smallest upper bound.

---

**Assuming $y^2<2$,** we want to find some $\varepsilon>0$ such that $(y+\varepsilon)^2 < 2$. Here is how we can find $\varepsilon$:

$$
\begin{align*}
    (y+\varepsilon)^2 < 2 &\iff y^2 + 2y\varepsilon + \varepsilon^2 < 2 \\
    &\iff 2y\varepsilon + \varepsilon^2 < 2-y^2 \\
    &\impliedby (2y+1)\varepsilon < 2-y^2 & \text{Requires $\varepsilon \le 1$} \\
    &\iff \varepsilon < \frac{2-y^2}{2y+1}.
\end{align*}
$$

Notice how we strengthened the inequality in the third line. When working backwards with inequalities in real analysis, this is very common. Now we let $\varepsilon < \min\left(\frac{2-y^2}{2y+1}, 1\right)$, and we can use our work backwards to show that $(y+\varepsilon)^2 < 2$. Therefore, $y$ is not an upper bound of the solution set.

---

**Assuming $y^2 > 2$,** we want to find some $\varepsilon$ such that $0<\varepsilon<y$ and $(y - \varepsilon)^2 > 2$. Using similar reasoning, we determine that we can let $\varepsilon < \frac{y^2-2}{2y+1}$.

$$(y-\varepsilon)^2 = y^2 - \varepsilon(2y-\varepsilon) > y^2 - \varepsilon(2y+1) > 2$$

Since $x\mapsto x^2$ is increasing for positive values, $y-\varepsilon$ is an upper bound for the solution set, contradicting that $y$ is the least upper bound.

---

We've shown that $y^2 < 2$ and $y^2 > 2$ are both contradictions, so what is left? $y^2 = 2$, and so $\sqrt{2}$ exists!

### $n^{th}$ Root of $x$

Now we will solve the general problem, which can be restated like this:

> Given an integer $n>1$ and a positive real number $x$, does there exists a positive real number $y$ such that $y^n = x$?

We will follow the same strategy, letting $$y = \sup\{t\in\mathbb{R}\mid t^n < x\}$$

---

**Assuming $y^n < x$,** we want to find an $\varepsilon>0$ such that $(y+\varepsilon)^n < x$. We will work backwards, where each statement implies the *previous one*.

$$
\begin{align*}
    (y+\varepsilon)^n &< x \\
    \sum_{k=0}^n \binom{n}{k}y^k\varepsilon^{n-k} &< x \\
    \sum_{k=0}^{n-1}\binom{n}{k}y^k\varepsilon^{n-k} &< x-y^n \\
    \varepsilon\sum_{k=0}^{n-1}\binom{n}{k}y^k &< x-y^n & \text{Requires $\varepsilon \le 1$} \\
    \varepsilon &< \frac{x-y^n}{\sum_{k=0}^{n-1}\binom{n}{k}y^k}.
\end{align*}
$$

We ended up showing that setting $\varepsilon < \min\left(1,\frac{x-y^n}{\sum_{k=0}^{n-1}\binom{n}{k}y^k}\right)$ is sufficient for $(y+\varepsilon)^n < x$, and so $y$ is not an upper bound of the solution set.

---

**Assuming $y^n > x$,** we want some $\varepsilon$ such that $0 < \varepsilon < y$ and $(y-\varepsilon)^n > x$. Again working backwards, we have

$$
\begin{align*}
    (y-\varepsilon)^n &> x \\
    \sum_{k=0}^n \binom{n}{k}y^k(-\varepsilon)^{n-k} &> x \\
    -\sum_{k=0}^{n-1}\binom{n}{k}y^k(-\varepsilon)^{n-k} &< y^n - x \\
    \sum_{k=0}^{n-1}\binom{n}{k}y^k\varepsilon^{n-k} &< y^n - x & \text{Took absolute value of LHS terms} \\
    \varepsilon\sum_{k=0}^{n-1}\binom{n}{k}y^k &< y^n - x & \text{Requires $\varepsilon \le 1$} \\
    \varepsilon &< \frac{y^n - x}{\sum_{k=0}^{n-1}\binom{n}{k}y^k},
\end{align*}
$$

so as long as $\varepsilon$ satisfies this, we have $(y-\varepsilon)^n > x$. Since $t\mapsto t^n$ is increasing, this shows $y-\varepsilon$ is an upper bound of the solution set, contradicting that $y$ is the least upper bound.

---

Since $y^n\not< x$ and $y^n\not> x$, we have $y^n = x$. Therefore, $n^{th}$ roots of positive real numbers exist! $\qquad \square$

I find this to be a very good problem for understanding how inequalities are manipulated in real analysis. The method of working backwards is quite useful.
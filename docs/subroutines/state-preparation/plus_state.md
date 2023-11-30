title: Single-qubit $|+\rangle$ state
---

## Description

Prepare $|+\rangle$, i.e. state with equal superposition of $\ket{0}$ and $\ket{1}$:

$$
|+\rangle = \frac{1}{\sqrt{2}} \left(\ket{0} + \ket{1}\right) 
$$

## Circuit

```openqasm

include "stdgates.inc";

qubit[1] q;
h q[0];
```

# Papers to review

Grouped by topic, roughly easiest to hardest within each group. Tick a paper off
when you've reviewed it, and put your notes in [../notes/](../notes/).

Links go to the free arXiv version where there is one.

**Suggested first five:** Preskill (NISQ), Shor, Grover, Bennett (teleportation), Fowler (surface codes).

## Foundations

- [ ] **[Simulating Physics with Computers](https://doi.org/10.1007/BF02650179)** — Feynman, 1982. The talk that started the field: nature is quantum, so simulating it needs a quantum computer.
- [ ] **[Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels](https://doi.org/10.1103/PhysRevLett.70.1895)** — Bennett et al., 1993. The original teleportation protocol. Matches [code/teleportation](../../code/teleportation/).

## Algorithms

- [ ] **[Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027)** — Shor, 1995. Factoring in polynomial time, the result that made the world pay attention.
- [ ] **[A Fast Quantum Mechanical Algorithm for Database Search](https://arxiv.org/abs/quant-ph/9605043)** — Grover, 1996. Square-root speedup for search. Short and readable. Matches [code/grover](../../code/grover/).
- [ ] **[Quantum Algorithm for Solving Linear Systems of Equations](https://arxiv.org/abs/0811.3171)** — Harrow, Hassidim, Lloyd, 2008. The "HHL" algorithm, basis of much quantum machine learning.
- [ ] **[How to Factor 2048 Bit RSA Integers in 8 Hours Using 20 Million Noisy Qubits](https://arxiv.org/abs/1905.09749)** — Gidney & Ekerå, 2019. A realistic cost estimate for breaking RSA.
- [ ] **[How to Factor 2048 Bit RSA Integers with Less than a Million Noisy Qubits](https://arxiv.org/abs/2505.15917)** — Gidney, 2025. The same estimate, cut 20x. Read right after the 2019 paper.

## Error correction and fault tolerance

- [ ] **[Good Quantum Error-Correcting Codes Exist](https://arxiv.org/abs/quant-ph/9512032)** — Calderbank & Shor, 1995. Proof that quantum error correction can work in principle.
- [ ] **[Fault-Tolerant Quantum Computation with Constant Error](https://arxiv.org/abs/quant-ph/9611025)** — Aharonov & Ben-Or, 1996. The threshold theorem: below a certain error rate, arbitrarily long computations are possible.
- [ ] **[Fault-Tolerant Quantum Computation by Anyons](https://arxiv.org/abs/quant-ph/9707021)** — Kitaev, 1997. Topological quantum computing and the toric code. Mathematically demanding.
- [ ] **[Surface Codes: Towards Practical Large-Scale Quantum Computation](https://arxiv.org/abs/1208.0928)** — Fowler et al., 2012. The standard tutorial on the surface code. Long, but the best entry point.
- [ ] **[High-Threshold and Low-Overhead Fault-Tolerant Quantum Memory](https://arxiv.org/abs/2308.07915)** — Bravyi et al. (IBM), 2023. qLDPC codes that need far fewer qubits than the surface code.

## Near-term (NISQ) algorithms

- [ ] **[Quantum Computing in the NISQ Era and Beyond](https://arxiv.org/abs/1801.00862)** — Preskill, 2018. Coined "NISQ." The best overview of where the field stands. Start here.
- [ ] **[A Variational Eigenvalue Solver on a Quantum Processor](https://arxiv.org/abs/1304.3061)** — Peruzzo et al., 2013. Introduced VQE for chemistry.
- [ ] **[A Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028)** — Farhi, Goldstone, Gutmann, 2014. Introduced QAOA for optimization.
- [ ] **[Noisy Intermediate-Scale Quantum (NISQ) Algorithms](https://arxiv.org/abs/2101.08448)** — Bharti et al., 2021. Big review of everything run on today's machines.
- [ ] **[Quantum Machine Learning](https://arxiv.org/abs/1611.09347)** — Biamonte et al., 2016. Overview of what quantum computers might do for machine learning.

## Hardware milestones

- [ ] **[Quantum Supremacy Using a Programmable Superconducting Processor](https://doi.org/10.1038/s41586-019-1666-5)** — Arute et al. (Google), 2019. The first quantum supremacy claim, on 53 qubits.
- [ ] **[Quantum Computational Advantage Using Photons](https://arxiv.org/abs/2012.01625)** — Zhong et al. (USTC), 2020. The photonic Jiuzhang advantage claim.
- [ ] **[Logical Quantum Processor Based on Reconfigurable Atom Arrays](https://arxiv.org/abs/2312.03982)** — Bluvstein et al. (Harvard/QuEra), 2023. Algorithms on 48 logical qubits.
- [ ] **[Quantum Error Correction Below the Surface Code Threshold](https://arxiv.org/abs/2408.13687)** — Google Quantum AI, 2024. Willow: errors drop as the code grows, the key sign error correction works.

## Recent (2025–2026)

- [ ] **[Observation of Constructive Interference at the Edge of Quantum Ergodicity](https://research.google/blog/a-verifiable-quantum-advantage/)** — Google Quantum AI, Nature, 2025. "Quantum Echoes": a quantum advantage whose answer can be checked. Link is Google's summary, which links the paper.
- [ ] **[Reinforcement Learning Control of Quantum Error Correction](https://www.nature.com/articles/s41586-026-10759-2)** — Nature, 2026. Machine learning keeps an error-corrected processor calibrated while it runs.
- [ ] **[Demonstrating Real-Time and Low-Latency Quantum Error Correction with Superconducting Qubits](https://www.nature.com/articles/s41467-026-73331-6)** — Nature Communications, 2026. Real-time decoding on Rigetti hardware, fast enough to keep up with the qubits.

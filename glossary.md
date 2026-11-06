# Glossary

| Term | Meaning |
|---|---|
| **Qubit** | The basic unit of quantum information. Like a bit, but it can be in a combination of 0 and 1 at once. |
| **Superposition** | A qubit being in a weighted combination of 0 and 1. Measuring it gives 0 or 1 with probabilities set by those weights. |
| **Measurement** | Reading a qubit. It forces the qubit into a definite 0 or 1 and destroys the superposition. |
| **Entanglement** | A link between qubits where their measurement results are correlated in ways no classical system can match. |
| **Bell state** | The simplest entangled state of two qubits, e.g. both always measured the same. |
| **Gate** | An operation on one or more qubits, the quantum version of a logic gate. |
| **Hadamard (H) gate** | Turns a 0 or 1 into an equal superposition. |
| **CNOT gate** | Flips a target qubit only if a control qubit is 1. The usual way to create entanglement. |
| **Circuit** | A sequence of gates applied to qubits, ending in measurements. |
| **Amplitude** | The complex number attached to each possible outcome. Its squared size is the probability. |
| **Interference** | Amplitudes adding up or cancelling out. Quantum algorithms use it to boost right answers and suppress wrong ones. |
| **Decoherence** | A qubit losing its quantum behavior through unwanted contact with its surroundings. |
| **Fidelity** | How close an actual result or operation is to the ideal one, from 0 to 1. |
| **Noise** | Any unwanted disturbance that causes errors in a quantum computation. |
| **Physical qubit** | A real qubit in hardware, which makes errors. |
| **Logical qubit** | One reliable qubit built from many physical qubits using error correction. |
| **Quantum error correction** | Spreading information across several qubits so errors can be detected and fixed without measuring the data directly. |
| **Surface code** | The leading error-correction scheme, using a 2D grid of qubits. |
| **NISQ** | "Noisy intermediate-scale quantum": today's machines, with many qubits but too much noise for full error correction. |
| **Quantum advantage** | A quantum computer doing a task faster or better than any classical computer can. "Quantum supremacy" is an older term for the same idea. |
| **Quantum annealing** | A different style of quantum computing aimed at optimization problems, used by D-Wave. |
| **Simulator** | Classical software that imitates a quantum computer. Exact, but slows down exponentially as qubits are added. |

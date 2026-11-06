"""Teleport a qubit's state from qubit 0 to qubit 2.

Real teleportation measures qubits 0 and 1 and sends the results to whoever holds
qubit 2, who then applies corrections. Here the corrections are done with
controlled gates instead, which gives the same final state and lets us check it
directly with a statevector.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace

# The state to teleport: an arbitrary rotation of |0>.
theta, phi = 1.1, 0.7

qc = QuantumCircuit(3)
qc.ry(theta, 0)
qc.rz(phi, 0)

# Share an entangled pair between qubits 1 and 2.
qc.h(1)
qc.cx(1, 2)

# Entangle the message qubit with qubit 1.
qc.cx(0, 1)
qc.h(0)

# Corrections on qubit 2, controlled by qubits 1 and 0.
qc.cx(1, 2)
qc.cz(0, 2)

print(qc.draw())

# Compare qubit 2's state with the original message state.
original = QuantumCircuit(1)
original.ry(theta, 0)
original.rz(phi, 0)
expected = Statevector(original)

received = partial_trace(Statevector(qc), [0, 1])
fidelity = np.real(expected.conjugate().data @ received.data @ expected.data)

print(f"Fidelity between original and teleported state: {fidelity:.6f}")  # expect 1.0

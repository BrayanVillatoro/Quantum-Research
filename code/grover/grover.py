"""Grover's search on 3 qubits: find the one marked item out of 8."""

import math
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

n = 3
marked = "101"   # the item we're searching for

def oracle(qc):
    """Flip the sign of the marked state's amplitude."""
    # Qiskit reads bitstrings right to left, so reverse to match qubit order.
    zeros = [i for i, bit in enumerate(reversed(marked)) if bit == "0"]
    qc.x(zeros)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(zeros)

def diffuser(qc):
    """Reflect every amplitude about the average, boosting the marked one."""
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))

qc = QuantumCircuit(n)
qc.h(range(n))   # start in an equal superposition of all 8 items

# About (pi/4) * sqrt(N) rounds are optimal.
rounds = math.floor(math.pi / 4 * math.sqrt(2 ** n))
for _ in range(rounds):
    oracle(qc)
    diffuser(qc)

qc.measure_all()
print(qc.draw())

counts = StatevectorSampler().run([qc], shots=1000).result()[0].data.meas.get_counts()

# Expect the marked item to come up about 95% of the time.
print(f"Searching for {marked} with {rounds} rounds")
print(dict(sorted(counts.items(), key=lambda kv: -kv[1])))

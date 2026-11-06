"""Create a Bell state: two qubits that always measure the same value."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)       # put qubit 0 in an equal superposition of 0 and 1
qc.cx(0, 1)   # entangle: flip qubit 1 whenever qubit 0 is 1
qc.measure_all()

print(qc.draw())

result = StatevectorSampler().run([qc], shots=1000).result()
counts = result[0].data.meas.get_counts()

# Expect about half '00' and half '11', and never '01' or '10'.
print(counts)

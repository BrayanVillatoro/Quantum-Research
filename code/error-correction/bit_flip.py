"""The 3-qubit bit-flip code: protect one qubit by copying it onto three.

An error flips one of the three data qubits. Two extra qubits check whether
pairs of data qubits agree (the "syndrome"), which reveals which qubit flipped
without reading the data itself. A correction then flips it back.
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.primitives import StatevectorSampler

def run(error_on):
    data = QuantumRegister(3, "data")
    check = QuantumRegister(2, "check")
    out = ClassicalRegister(1, "out")
    qc = QuantumCircuit(data, check, out)

    # Logical |1>: encode by copying data[0] onto data[1] and data[2].
    qc.x(data[0])
    qc.cx(data[0], data[1])
    qc.cx(data[0], data[2])

    # The error.
    if error_on is not None:
        qc.x(data[error_on])

    # Syndrome: check[0] = data0 XOR data1, check[1] = data1 XOR data2.
    qc.cx(data[0], check[0])
    qc.cx(data[1], check[0])
    qc.cx(data[1], check[1])
    qc.cx(data[2], check[1])

    # Correct, using the syndrome to pick which qubit to flip back.
    qc.x(check[1])
    qc.ccx(check[0], check[1], data[0])   # syndrome 10 -> data0 flipped
    qc.x(check[1])
    qc.ccx(check[0], check[1], data[1])   # syndrome 11 -> data1 flipped
    qc.x(check[0])
    qc.ccx(check[0], check[1], data[2])   # syndrome 01 -> data2 flipped
    qc.x(check[0])

    # Decode and read the logical qubit.
    qc.cx(data[0], data[2])
    qc.cx(data[0], data[1])
    qc.measure(data[0], out[0])

    return StatevectorSampler().run([qc], shots=200).result()[0].data.out.get_counts()

# Every case should read back '1', the value we encoded.
for error_on in [None, 0, 1, 2]:
    label = "no error" if error_on is None else f"flip on data qubit {error_on}"
    print(f"{label:>22}: {run(error_on)}")

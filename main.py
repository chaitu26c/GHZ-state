from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.primitives import BackendSampler
import matplotlib.pyplot as plt
from qiskit.circuit.library import Initialize
from qiskit.quantum_info import Statevector


qc = QuantumCircuit(3,3)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)


qc.cx(0,1)
qc.cx(0,2)


qc.measure([0, 1, 2], [0, 1, 2])


# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
# Run the circuit and get results
job = simulator.run(compiled_circuit)  # Removed the `assemble()` step
result = job.result()

# Get measurement results
counts = result.get_counts(qc)
print("Measurement results:", counts)

# Draw the circuit
qc.draw(output='mpl')
plt.show()

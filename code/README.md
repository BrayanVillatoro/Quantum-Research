# Code

Simulations, experiments, and quantum programs. Each project gets its own folder.

## Setup

```
pip install -r requirements.txt
```

## Examples

Run any of them with `python <folder>/<file>.py`. They all run on a local simulator.

| Folder | What it shows |
|---|---|
| [bell-state/](bell-state/) | Entangling two qubits so they always measure the same |
| [teleportation/](teleportation/) | Moving a qubit's state to another qubit using entanglement |
| [grover/](grover/) | Finding a marked item faster than checking one by one |
| [error-correction/](error-correction/) | The 3-qubit bit-flip code catching and fixing an error |

To run on a real IBM quantum computer, see [../industry/hardware-access.md](../industry/hardware-access.md).

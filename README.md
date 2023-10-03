# Info

This Python library facilitates parsing Verilog netlists.  It has ONLY ever been tested on flattened gate-level netlists, so I wouldn't expect it to work out of the box on anything else.

---

### Installation

If you have virtualenv/pip installed (recommended), just do `$ pip install git+https://github.com/KyeongMin5307/PyVerilog.git`
    
---

- `verilogParse.py`

    This file is based on http://pyparsing.wikispaces.com/file/view/verilogParse.py .
    It has been modified to (1) build our Netlist datastructure during parsing and (2) to allow wires with names like "input45"

The rest of the files build the Netlist datastructure.

---

Below example shows how to read and link netlists. It demonstrates both 
reading from Verilog (`n1`) and YAML (`n2`), and then verifies that
the a few of the netlist properties match.

Make sure that your current directory includes the `test` directory
in this repository.

- Example Usage:

    ```python
    from pyverilog.Netlist import Netlist
    
    nl1 = Netlist()
    nl2 = Netlist()
    
    nl1.readYAML("test/gates.yml")
    nl2.readYAML("test/gates.yml")
    
    nl1.readVerilog("test/Iface_test.gv")
    nl2.readYAML("test/Iface_test.yml")
    
    nl1.link("Iface_test")
    nl2.link("Iface_test")
    
    nl1.topMod
    # 'Iface_test'
    nl2.topMod
    # 'Iface_test'
    
    mod1 = nl1.mods[nl1.topMod]
    mod2 = nl2.mods[nl2.topMod]
    
    set(mod1.ports.keys()) == set(mod2.ports.keys())
    # True
    set(mod1.cells.keys()) == set(mod2.cells.keys())
    # True
    set(mod1.nets.keys()) == set(mod2.nets.keys())
    # True
    ```

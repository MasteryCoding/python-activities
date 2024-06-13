class LogicGate:
    def output(self, a, b = None):
        # input a is required 
        # input b is optional
        return None
    
class BufferGate(LogicGate):
    def output(self, a, b=None):
        return a
    
class NotGate(LogicGate):
    def output(self, a, b=None):
        if (a): return 0
        else: return 1
    
class AndGate(LogicGate):
    def output(self, a, b=None):
        return a and b
    
class OrGate(LogicGate):
    def output(self, a, b=None):
        return a or b
    
class NANDGate(LogicGate):
    def output(self, a, b=None):
        and_gate = AndGate()
        not_gate = NotGate()
        return not_gate.output(and_gate.output(a, b))
    
def test_logic_gate():
    logic_gate = LogicGate()
    print(logic_gate.output(0))
    print(logic_gate.output(1))
    
def test_buffer_gate():
    buffer_gate = BufferGate()
    print(buffer_gate.output(0))
    print(buffer_gate.output(1))

def test_not_gate():
    not_gate = NotGate()
    print(not_gate.output(0))
    print(not_gate.output(1))

def test_and_gate():
    and_gate = AndGate()
    print(and_gate.output(0, 0))
    print(and_gate.output(1, 0))
    print(and_gate.output(0, 1))
    print(and_gate.output(1, 1))

def test_or_gate():
    or_gate = OrGate()
    print(or_gate.output(0, 0))
    print(or_gate.output(1, 0))
    print(or_gate.output(0, 1))
    print(or_gate.output(1, 1))

def test_nand_gate():
    nand_gate = NANDGate()
    print(nand_gate.output(0, 0))
    print(nand_gate.output(1, 0))
    print(nand_gate.output(0, 1))
    print(nand_gate.output(1, 1))

test_nand_gate()






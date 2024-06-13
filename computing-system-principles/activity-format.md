# Logics Gates Activity

## Introduction

## Overview

In this activity we're going to build a collection of logic gates to simulate how a computer chip works. Remember a logic gate is an electrical component that accepts 1 or more binary inputs (0 or 1), and outputs a binary result.


### Step 1: The Logic Gate Class

To build our logic gates, we're going to use **inheritance**.

#### Hint: Remember inheritance is where child classes can inherit functionality from a parent class.

The first thing to do is create the parent class for all of our logic gates: the Logic Gate class. You can use the starter code below:

```py
class LogicGate:
    def output(self, a, b = None):
        # input a is required 
        # input b is optional
        return None
```

#### Test Code

To test this code and make sure it works properly you can create an instance of the LogicGate class and make sure that when you call `output` it returns `None`.

```py
def test_logic_gate():
    logic_gate = LogicGate()
    print(logic_gate.output(0))
    print(logic_gate.output(1))
```

#### Solution

```py
class LogicGate:
    def output(self, a, b = None):
        # input a is required 
        # input b is optional
        return None
    
logic_gate = LogicGate()
print(logic_gate.output(0))
print(logic_gate.output(1))
```

### Step 2: The Buffer Gate

Now that we have a base class we can start creating some more logic gates. We'll start with the simples logic gate: the **Buffer** gate. The buffer gate takes in a single binary input, and returns the same binary output.

Create a new class called `BufferGate` which inherits from `LogicGate` and then write the `output` method.

Below is the starter code for the `BufferGate` class:

```py
class LogicGate:
    def output(self, a, b = None):
        # input a is required 
        # input b is optional
        return None
```

#### Test Code

Once you're ready to test your code you can run the code below which should output 0 and 1.

```py
buffer_gate = BufferGate()
print(buffer_gate.output(0))
print(buffer_gate.output(1))
```

#### Solution

```py
class LogicGate:
    def output(self, a, b = None):
        # input a is required 
        # input b is optional
        return None
    
class BufferGate(LogicGate):
    def output(self, a, b=None):
        return a
    
buffer_gate = BufferGate()
print(buffer_gate.output(0))
print(buffer_gate.output(1))
```

### Step 3: NOT Gate

For our next logic gate we'll create the NOT gate or the Inverter. This gate will take a single binary input and return the opposite binary output. Make sure your output is in 0s and 1s.

```py
class NotGate(LogicGate):
    def output(self, a, b=None):
        # return the opposite of a
        pass
```

#### Test Code

```py
def test_not_gate():
    not_gate = NotGate()
    print(not_gate.output(0))
    print(not_gate.output(1))
```

#### Solution

```py
class NotGate(LogicGate):
    def output(self, a, b=None):
        if (a): return 0
        else: return 1
```

### Step 4: AND Gate

Now that we have an idea of how to create new gates, let's create the AND gate. The AND gate takes in two binary inputs, and returns true (1), only if both inputs are true (1) as well.

Here's the starter code for the AND gate:

```py
class AndGate(LogicGate):
    def output(a, b=None):
        # return 1 if a and b are both 1
        # otherwise return 0
        pass
```

#### Test Code

The code below should output:

`
0
0
0
1
`

**Test code**
```py
def test_and_gate():
    and_gate = AndGate()
    print(and_gate.output(0, 0))
    print(and_gate.output(1, 0))
    print(and_gate.output(0, 1))
    print(and_gate.output(1, 1))
```

#### Solution

```py
    
class AndGate(LogicGate):
    def output(self, a, b=None):
        return a and b
```

### Step 5: OR Gate

For our next gate we'll build the OR gate. The OR gate takes in two binary inputs and returns true if either one of them is true.

```py
class OrGate(LogicGate):
    def output(self, a, b=None):
        # return a OR b
        pass
```

#### Test code

The code below should output: `0, 1, 1, 1`
```py
def test_or_gate():
    or_gate = OrGate()
    print(or_gate.output(0, 0))
    print(or_gate.output(1, 0))
    print(or_gate.output(0, 1))
    print(or_gate.output(1, 1))
```

#### Solution

```py
    
class OrGate(LogicGate):
    def output(self, a, b=None):
        return a or b
```

### Step 6: Chaining Logic Gates Together

At this point we should have 4 working logic gates:
- buffer gate
- not gate
- and gate
- or gate

So now we try chaining them together to see what kind of results we get. We'll create another new type of logic gate: The NAND gate. The NAND gate acts as an inversion of an AND gate returning true only if both inputs are NOT true. To build this gate we'll use two other gates. Can you guess which ones?

```py
class NANDGate(LogicGate):
    def output(self, a, b=None):
        # return a value by using two other logic gates
        # should return the opposite of an AND gate
        pass
```

### Test Code 

The code below should return the following: `1, 1, 1, 0`

```py
def test_nand_gate():
    nand_gate = NANDGate()
    print(nand_gate.output(0, 0))
    print(nand_gate.output(1, 0))
    print(nand_gate.output(0, 1))
    print(nand_gate.output(1, 1))
```

### Solution

```py
class NANDGate(LogicGate):
    def output(self, a, b=None):
        and_gate = AndGate()
        not_gate = NotGate()
        return not_gate.output(and_gate.output(a, b))
```

## Conclusion

In this activity we created several logic gates to simulate the work that a computer chip does with electrical signals. We only created a few of the essential logic gates to get started but there are even more you can build on our own:

- The NOR Gate: returns the opposite of an OR Gate.
- The XOR Gate: The exclusive OR gate which only returns true if one of the signals is true (but not both).

For some future fun try mixing the gates together to see what you get.
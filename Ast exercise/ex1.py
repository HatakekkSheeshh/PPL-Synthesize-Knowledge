from abc import ABC, abstractmethod

class Expr(ABC):
    @abstractmethod
    def printPrefix(self) -> str:
        pass
    @abstractmethod
    def eval(self) -> float:
        pass

class IntLit(Expr):
    def __init__(self, intlit: int):
        self.intlit = intlit
    
    def printPrefix(self) -> str :
        return str(self.intlit)
    def eval(self) -> float:
        return float(self.intlit)

class FloatLit(Expr):
    def __init__(self, floatlit: float):
        self.floatlit = floatlit
    
    def printPrefix(self) -> str :
        return str(self.floatlit)
    def eval(self) -> float :
        return float(self.floatlit)

class BinExp(Expr):
    def __init__(self, left: Expr, op: str, right: Expr):
        self.op = op
        self.left = left
        self.right = right
    
    def printPrefix(self) -> str :
        return f"{self.op} {self.left.printPrefix()} {self.right.printPrefix()}"
    def eval(self):
        lf: float = self.left.eval()
        rt: float = self.right.eval()
        if (self.op == "+"):
            return lf + rt
        elif (self.op == "-"):
            return lf - rt
        elif (self.op == "*"):
            return lf * rt
        elif (self.op == "/"):
            return lf / rt

class UnExp(Expr):
    def __init__(self, op: str, arg: Expr):
        self.op = op
        self.arg = arg
    
    def printPrefix(self) -> str :
        return f"{self.op}. {self.arg.printPrefix()}"
    def eval(self):
        if (self.op == "+"):
            return float(self.arg.eval())
        elif (self.op == "-"):
            return float(-self.arg.eval())

t = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*",IntLit(2)))
x3 = BinExp(IntLit(1), "+",IntLit(1))
print(t.printPrefix())
print(x3.printPrefix())

print(t.eval())
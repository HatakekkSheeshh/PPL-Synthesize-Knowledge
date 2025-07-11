from abc import ABC, abstractmethod

class Expr(ABC):
    @abstractmethod
    def printPrefix(self) -> str:
        pass

class IntLit(Expr):
    def __init__(self, intlit: int):
        self.intlit = intlit
    
    def printPrefix(self) -> str :
        return str(self.intlit)


class FloatLit(Expr):
    def __init__(self, floatlit: float):
        self.floatlit = floatlit
    
    def printPrefix(self) -> str :
        return str(self.floatlit)

class BinExp(Expr):
    def __init__(self, left: Expr, op: str, right: Expr):
        self.left = left
        self.op = op
        self.right = right
    
    def printPrefix(self) -> str :
        return f"{self.op} {self.left.printPrefix()} {self.right.printPrefix()}"

class UnExp(Expr):
    def __init__(self, op: str, arg: Expr):
        self.op = op
        self.arg = arg
    
    def printPrefix(self) -> str :
        return f"{self.op}. {self.arg.printPrefix()}"


t = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*",IntLit(2)))
x3 = BinExp(IntLit(1), "+",IntLit(1))
print(t.printPrefix())
print(x3.printPrefix())
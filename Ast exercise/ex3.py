from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitBinExp(self, exp) -> object :
        pass

    @abstractmethod
    def visitUnExp(self, exp) -> object :
        pass

    @abstractmethod
    def visitIntLit(self, exp) -> object :
        pass

    @abstractmethod
    def visitFloatLit(self, exp) -> object :
        pass

class Eval(Visitor):
    def visitBinExp(self, exp) -> float :
        lt = exp.left.accept(self)
        rt = exp.right.accept(self)
        if exp.op == "+":
            return lt + rt
        elif exp.op == "-":
            return lt - rt
        elif exp.op == "*":
            return lt * rt
        elif exp.op == "/":
            return lt / rt
        else:
            return -1
    
    def visitUnExp(self, exp) -> float :
        arg = exp.arg.accept(self)
        if exp.op == "+":
            return arg
        elif exp.op == "-":
            return (-arg)
        return -1

    def visitIntLit(self, exp) -> int :
        return int(exp.intlit)

    def visitFloatLit(self, exp) -> float :
        return float(exp.floatlit)


class PrintPrefix(Visitor):
    def visitBinExp(self, exp) -> str :
        lt = exp.left.accept(self)
        rt = exp.right.accept(self)
        op = exp.op
        return f"{op} {lt} {rt}"
    
    def visitUnExp(self, exp) -> str :
        arg = exp.arg.accept(self)
        op = exp.op
        return f"{op}. {arg}"
    
    def visitIntLit(self, exp) -> str :
        return str(exp.intlit)

    def visitFloatLit(self, exp) -> str :
        return str(exp.floatlit)

class PrintPostfix(Visitor):
    def visitBinExp(self, exp) -> str :
        lt = exp.left.accept(self)
        rt = exp.right.accept(self)
        op = exp.op
        return f"{lt} {rt} {op}"
    
    def visitUnExp(self, exp) -> str :
        arg = exp.arg.accept(self)
        op = exp.op
        return f"{arg} {op}."
    
    def visitIntLit(self, exp) -> str :
        return str(exp.intlit)

    def visitFloatLit(self, exp) -> str :
        return str(exp.floatlit)    

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) :
        pass

class IntLit(Expr):
    def __init__(self, intlit: int):
        self.intlit = intlit
    
    def accept(self, visitor: Visitor) -> object :
        return visitor.visitIntLit(self)

class FloatLit(Expr):
    def __init__(self, floatlit: float):
        self.floatlit = floatlit
    
    def accept(self, visitor: Visitor) -> object :
        return visitor.visitFloatLit(self)


class BinExp(Expr):
    def __init__(self, left: Expr, op: str, right: Expr):
        self.op = op
        self.left = left
        self.right = right
    
    def accept(self, visitor: Visitor) -> object :
        return visitor.visitBinExp(self)
    

class UnExp(Expr):
    def __init__(self, op: str, arg: Expr):
        self.op = op
        self.arg = arg
    
    def accept(self, visitor: Visitor) -> object :
        return visitor.visitUnExp(self)


t = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*",IntLit(2)))
x3 = BinExp(IntLit(1), "+",IntLit(1))

print(t.accept(PrintPrefix()))
print(t.accept(PrintPostfix()))
print(t.accept(Eval()))
class MultiplyNodes:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()
    
class AddNodes:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

class NumNode:
    def __init__(self, num) -> None:
        self.num = num
    
    def eval(self):
        return self.num


def Main():
    # Evaluating basic expression : 
        # (5+4)*6+3
    x = NumNode(5)
    y = NumNode(4)
    p = AddNodes(x,y)
    t = MultiplyNodes(p,NumNode(6))
    root = AddNodes(t, NumNode(3))
    print(root.eval())

if __name__=='__main__':
    Main() 
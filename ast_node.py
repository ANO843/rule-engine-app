class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # Left child (ASTNode)
        self.right = right     # Right child (ASTNode)
        self.value = value     # Value for operands

    def __repr__(self):
        return f"ASTNode(type={self.type}, value={self.value})"


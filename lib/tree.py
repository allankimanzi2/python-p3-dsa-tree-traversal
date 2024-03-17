class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Check if the root is None
        if self.root is None:
            return None
        
        # Depth-first traversal to find the node with the specified id
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if current_node['id'] == id:
                return current_node
            # Add children to the stack for further traversal
            for child in current_node.get('children', []):
                stack.append(child)
        
        # If the node with the specified id is not found, return None
        return None

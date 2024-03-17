class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        
        if self.root is None:
            return None
        
        
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            if current_node['id'] == id:
                return current_node
            
            for child in current_node.get('children', []):
                stack.append(child)
        
        
        return None

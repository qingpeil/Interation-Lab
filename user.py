class User:
    def __init__(self, user_id, dictionary_of_nodes):
       self.user_id=user_id
       self.dictionary_of_nodes=dictionary_of_nodes
    def add_node(self, key, node):
        dictionary_of_nodes={key:node}
    def get_next_node(self, current_node, input_choice_index):
        return self.dictionary_of_nodes[current_node.get_next_node_key(self, input_choice_index)]





class Node:  # each interaction round with user
    
    def __init__(
            self,
            question,
            array_of_options,
            key
    ):

        self._question = question
        self._key = key
        self._array_of_options = array_of_options

    def get_next_node_key(self, input_choice_index):
        return self.array_of_options[input_choice_index].next_node_key

    @property
    def array_of_options(self):
        return self._array_of_options


if __name__ == "__main__":
    node = Node("hello", ["Hi", "Hello"], "greeting")
    print(len(node.array_of_options))

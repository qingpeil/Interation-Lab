class Node:  # each interaction round with user
    def __init__(self, question, number_of_options, array_of_options, key):
        self.question = question
        self.number_of_options = number_of_options
        self.key = key
        array_of_options = array_of_options

        def get_next_node_key(self, input_choice_index):
            return self.array_of_options[input_choice_index].next_node_key
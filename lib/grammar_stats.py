class GrammarStats:
    def __init__(self):
        self.check_history = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == "":
            raise Exception("Can't grammar check an empty text")
        self.check_history.append(text[0].isupper() and text[-1] in ".?!")
        return self.check_history[-1]

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.check_history == []:
            raise Exception("No texts have been checked yet")
        return round(sum(self.check_history) * 100 / len(self.check_history), 0)

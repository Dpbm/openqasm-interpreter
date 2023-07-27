class Error:
    def __init__(self, source:str, error:Exception):
        self.source = source
        self.error = error
        self.error_message = str(error)

    def show(self):
        print(f"Failed on {self.source}")
        print(f"Error: {self.error_message}")


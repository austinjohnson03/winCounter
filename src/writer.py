class Writer:
    def __init__(self, output_path):
        self.output_path = output_path

    def write(self, data):
        with open(self.output_path, 'w') as f:
            f.write(data)

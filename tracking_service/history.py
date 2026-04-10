class History:
    def __init__(self):
        self.records = []

    def add_record(self, data):
        self.records.append(data)

    def get_history(self):
        return self.records

    def last_record(self):
        if self.records:
            return self.records[-1]
        return None
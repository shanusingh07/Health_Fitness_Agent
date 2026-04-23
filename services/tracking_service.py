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


def track_progress(user, current_weight, previous_weight):
    change = current_weight - previous_weight

    if change < 0:
        status = "Weight Loss 📉"
    elif change > 0:
        status = "Weight Gain 📈"
    else:
        status = "No Change"

    return {
        "previous_weight": previous_weight,
        "current_weight": current_weight,
        "change": change,
        "status": status
    }

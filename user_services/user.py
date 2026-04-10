class User:
    def __init__(self, age, weight, height, goal, diet):
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.diet = diet

    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "goal": self.goal,
            "diet": self.diet
        }

    def __repr__(self):
        return f"User(age={self.age}, weight={self.weight}, height={self.height}, goal='{self.goal}', diet='{self.diet}')"
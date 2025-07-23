class Distance:
    conversion_to_meters = {
        'см': 0.01,
        'м': 1.0,
        'км': 1000.0
    }

    def __init__(self, value, measure):
        if measure not in self.conversion_to_meters:
            raise ValueError(f"Неподдерживаемая мера: {measure}")
        self.value = value
        self.measure = measure

    def to_meters(self):
        return self.value * self.conversion_to_meters[self.measure]

    def __str__(self):
        return f"{self.value} {self.measure}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        result_value = total_meters / self.conversion_to_meters[self.measure]
        return Distance(result_value, self.measure)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_meters = self.to_meters() - other.to_meters()
        if diff_meters < 0:
            raise ValueError("Результат не может быть отрицательным")
        result_value = diff_meters / self.conversion_to_meters[self.measure]
        return Distance(result_value, self.measure)

    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

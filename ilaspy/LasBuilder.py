class LasBuilder:
    def __init__(self):
        self.explicit_hypotheses: list[str] = []

    def __str__(self):
        explicit_hypotheses: str = "\n".join(self.explicit_hypotheses)
        return explicit_hypotheses

    def add_mode_bias(self, mode_bias: str):
        raise NotImplementedError()

    def add_explicit_hypothesis(self, length: int, rule: str):
        self.explicit_hypotheses.append(f"{length} ~ {rule.strip()}.")

    def to_string(self):
        return self.__str__()

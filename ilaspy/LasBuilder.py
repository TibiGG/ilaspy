class LasBuilder:
    def __init__(self):
        self.explicit_hypotheses: ExplicitHypothesisBuilder = ExplicitHypothesisBuilder()

    def __str__(self):
        explicit_hypotheses: str = self.explicit_hypotheses.to_string()
        return explicit_hypotheses

    def add_mode_bias(self, mode_bias: str):
        raise NotImplementedError()

    def add_explicit_hypothesis(self, length: int, rule: str):
        """
        By definition from https://doc.ilasp.com/specification/explicit_hypothesis_space.html:
        An explicity definition is of the form: length ~ rule
        :param length:
        :param rule: a normal rule, choice rule, hard constraint or weak constraint
        :return:
        """
        self.explicit_hypotheses.add(length, rule)

    def to_string(self):
        return self.__str__()


class ExplicitHypothesisBuilder():
    def __init__(self):
        self.explicit_hypotheses: list[(int, str)] = []

    def add(self, length: int, rule: str):
        self.explicit_hypotheses.append((length, rule.strip()))

    def __str__(self):
        self.sort()
        return "\n".join([f"{length} ~ {rule}." for (length, rule) in self.explicit_hypotheses])

    def to_string(self):
        return self.__str__()

    def sort(self):
        self.explicit_hypotheses = sorted(self.explicit_hypotheses)

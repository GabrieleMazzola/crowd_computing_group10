from explanation.satisfaction.satisfaction import Satisfaction


def satisfaction_level(score):
    if score < 0.17:
        return Satisfaction.VERY_WEAK
    if 0.17 <= score < 0.34:
        return Satisfaction.WEAK
    if 0.34 <= score < 0.51:
        return Satisfaction.INDIFFERENT
    if 0.51 <= score < 0.68:
        return Satisfaction.MEDIUM
    if 0.68 <= score < 0.85:
        return Satisfaction.STRONG
    else:
        return Satisfaction.VERY_STRONG

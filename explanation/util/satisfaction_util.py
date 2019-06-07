from explanation.satisfaction.satisfaction import Satisfaction
import math

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


def satisfaction_level_user(score, len_list, original_length):
    score = score - original_length + len_list
    if len_list % 2 == 0:
        maximum = len_list * len_list/2
    else:
        maximum = len_list * math.floor(len_list/2) + math.floor(len_list/2)

    interval = maximum*1.0/len_list

    if score < interval:
        return Satisfaction.VERY_STRONG
    if interval <= score < 2*interval:
        return Satisfaction.STRONG
    if 2*interval <= score < 3*interval:
        return Satisfaction.MEDIUM
    if 3*interval <= score < 4*interval:
        return Satisfaction.INDIFFERENT
    if 4*interval <= score < 5*interval:
        return Satisfaction.WEAK
    else:
        return Satisfaction.VERY_WEAK

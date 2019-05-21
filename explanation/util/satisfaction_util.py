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

def satisfaction_level_user(score, len_list):
    # if len_list % 2 == 0:
    #     max_sat = len_list*int(len_list/2)
    # else:
    #     max_sat = len_list*int(len_list/2) + int(len_list/2)
    print()
    if score < len_list:
        print("very strong")
        return Satisfaction.VERY_STRONG
    if len_list <= score < 2*len_list:
        print("strong")
        return Satisfaction.STRONG
    if 2*len_list <= score < 3*len_list:
        print("medium")
        return Satisfaction.MEDIUM
    if 3*len_list <= score < 4*len_list:
        print("indifferent")
        return Satisfaction.INDIFFERENT
    if 4*len_list <= score < 5*len_list:
        print("weak")
        return Satisfaction.WEAK
    else:
        print("very weak")
        return Satisfaction.VERY_WEAK

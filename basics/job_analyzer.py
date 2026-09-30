def cal_sal(base_sal, bonus_rate = .1):
    total_sal = base_sal * (1 + bonus_rate)
    return (total_sal)

def cal_bonus(total_sal, base_sal):
    return (total_sal - base_sal) / base_sal
def calculate_payout(User, percent_dict, base_cost = 10000):
    comp_part = []
    comp_dw = 0
    for participant in percent_dict:
        if participant != User:
            comp_part.append((participant, (.985 * base_cost * percent_dict[participant] * (1-percent_dict[User])**2) / (1-percent_dict[User])))
            comp_dw += (.015 * base_cost * percent_dict[participant] * (1-percent_dict[User])**2) / (1-percent_dict[User])
    cost = base_cost * (1 - percent_dict[User])**2
    return cost, comp_dw, comp_part

if __name__ == '__main__':
    calculate_payout('citi', {'citi': .333, 'jpm': .111, 'boa': .555}, .05)
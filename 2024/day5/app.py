import sys
sys.path.append('C:/Code/Advent-of-Code/2024/utils')
from utils import read_txt_file_as_string

Rules = read_txt_file_as_string('2024/day5/rules.txt').split('\n')
Updates = read_txt_file_as_string('2024/day5/updates.txt').split('\n')
TestRules = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''.split('\n')
TestUpdates = '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''.split('\n')

def sort_out_numerical_order_rules(rules):
    nonNumericalRules = []
    for rule in rules:
        if rule[0] < rule[1]:
            nonNumericalRules.append(rule)
    return nonNumericalRules


def clean_rules(rules):
    clean_rules = []
    for rule in rules:
        rule = rule.split('|')
        clean_rules.append([int(rule[0]), int(rule[1])])
    return clean_rules

def clean_updates(updates):
    clean_updates = []
    for update in updates:
        clean_updates.append([int(number) for number in update.split(',')])
    return clean_updates


def check_update(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return 0
    return update[int(len(update)/2)]
    
def sum_all_correct_updates(rules, updates):
    sum = 0
    for update in updates:
        sum += check_update(rules, update)
    return sum



if __name__=="__main__":
    #rules, updates = TestRules, TestUpdates
    rules, updates = Rules, Updates
    rules = clean_rules(rules)
    updates = clean_updates(updates) 
    print(sum_all_correct_updates(rules, updates))


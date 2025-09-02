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

# Unused function used to find each rule where the first number is smaller than the second and return them as a list.
def sort_out_numerical_order_rules(rules):
    nonNumericalRules = []
    for rule in rules:
        if rule[0] < rule[1]:
            nonNumericalRules.append(rule)
    return nonNumericalRules

# Converts the rules from a string in the "xx|yy" format to a list in the [[xx, yy]] format
def clean_rules(rules):
    clean_rules = []
    for rule in rules:
        rule = rule.split('|')
        clean_rules.append([int(rule[0]), int(rule[1])])
    return clean_rules

# Converts the updates string into a list where each element is a line from update string as list containing integers
def clean_updates(updates):
    clean_updates = []
    for update in updates:
        clean_updates.append([int(number) for number in update.split(',')])
    return clean_updates

# Takes on line from the updates 
# 1. Loops through the rules 
# 2. Checks if both numbers of the rule are contained within this line of the update
# 3. Checks if the indexes matching the numbers in the rule has the same order as the rule
# 4. If the order is incorrect 0 will be returned otherwise the middle page number of the update is added
def check_update(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return 0
    return update[int(len(update)/2)]

# Loops through the update list and runs each line in the check_update function to then sum up the result    
def sum_all_correct_updates(rules, updates):
    sum = 0
    for update in updates:
        sum += check_update(rules, update)
    return sum

def order_update(rules, update):
    medianPage = 0
    while medianPage == 0:
        medianPage = check_update(rules, update)
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                ruleIndexLeft = update.index(rule[0])
                ruleIndexRight = update.index(rule[1])
                if  ruleIndexLeft > ruleIndexRight:
                    update =  [rule[0]] + update[:ruleIndexLeft] + update[ruleIndexLeft+1:]
    return update[int(len(update)/2)]


def sum_all_incorrect_updates(rules, updates):
    sum = 0
    for update in updates:
        if check_update(rules, update)==0:
            sum += order_update(rules, update)
    return sum


if __name__=="__main__":
    #rules, updates = TestRules, TestUpdates
    rules, updates = Rules, Updates
    rules = clean_rules(rules)
    updates = clean_updates(updates) 
    # print(sum_all_correct_updates(rules, updates))
    print(sum_all_incorrect_updates(rules, updates))


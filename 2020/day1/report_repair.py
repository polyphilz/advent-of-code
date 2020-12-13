from functools import reduce


def find_invalid_expense_pair(expenses, target_value):
    seen_expenses = set()
    for expense in expenses:
        if target_value - expense in seen_expenses:
            return target_value - expense, expense
        seen_expenses.add(expense)
    return 0, 0


def find_invalid_expense_triplet(expenses, target_value):
    for i in range(len(expenses) - 2):
        exp1 = expenses[i]
        intermediate_target_sum_value = target_value - exp1
        seen_expenses = set()
        for j in range(i + 1, len(expenses)):
            exp2 = expenses[j]
            exp3 = intermediate_target_sum_value - exp2
            if exp3 in seen_expenses:
                return exp1, exp2, exp3
            seen_expenses.add(exp2)
    return 0, 0, 0


def product_of_expenses(*expenses):
    return reduce(
        lambda running_product, expense: running_product * expense, expenses, 1
    )


def main():
    TARGET_SUM_VALUE = 2020

    with open("report_repair_input.txt", "r") as f:
        expenses = list(map(lambda expense: int(expense), f.readlines()))

        # Part 1
        exp1, exp2 = find_invalid_expense_pair(expenses, TARGET_SUM_VALUE)
        print(product_of_expenses(exp1, exp2))

        # Part 2
        exp1, exp2, exp3 = find_invalid_expense_triplet(expenses, TARGET_SUM_VALUE)
        print(product_of_expenses(exp1, exp2, exp3))


if __name__ == "__main__":
    main()

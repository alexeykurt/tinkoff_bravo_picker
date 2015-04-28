# encoding=utf-8
import operator
import sys
from itertools import combinations
from optparse import OptionParser


def get_all_combinations(array):
    for x in range(1, len(array) + 1):
        for comb in combinations(array, x):
            yield comb


def pick_max_value_combination(array, max_value):
    filtered_combs = []
    for comb in get_all_combinations(array):
        value = sum(comb)
        if value == max_value:
            return value, comb
        if value < max_value:
            filtered_combs.append((value, comb))
    return max(filtered_combs, key=operator.itemgetter(0))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-p', '--points', dest='points', action='store', type=int, help=u'Количество баллов Браво')
    parser.add_option('-t', '--transactions', dest='transactions_string', action='store', help=u'Операции для компенсации (суммы)')
    (options, args) = parser.parse_args()
    if not options.points:
        print u'Укажите кол-во баллов Браво ключом -p'
        sys.exit(1)
    if not options.transactions_string:
        print u'Укажите операции для компенсации в виде сумм через запятую ключом -t'
        sys.exit(1)
    
    try:
        transactions = map(int, options.transactions_string.split(','))
    except ValueError:
        print u'Операции для компенсации: суммы через запятую'
        sys.exit(1)

    value, combination = pick_max_value_combination(transactions, int(options.points))
    print u'Можно компенсировать {0} баллов Браво'.format(value)
    print u'Для этого компенсируйте эти суммы: {0}'.format(', '.join(map(str, combination)))

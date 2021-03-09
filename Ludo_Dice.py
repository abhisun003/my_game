import random

a = 'y'

while a == 'y':
    n= random.randint(1,6)
    if n==1:
        print('|-----------|')
        print('|           |')
        print('|     *     |')
        print('|           |')
        print('|-----------|')
    if n == 2:
        print('|-----------|')
        print('| *         |')
        print('|           |')
        print('|         * |')
        print('|-----------|')
    if n == 3:
        print('|-----------|')
        print('| *         |')
        print('|     *     |')
        print('|         * |')
        print('|-----------|')
    if n == 4:
        print('|-----------|')
        print('| *       * |')
        print('|           |')
        print('| *       * |')
        print('|-----------|')
    if n == 5:
        print('|-----------|')
        print('| *       * |')
        print('|     *     |')
        print('| *       * |')
        print('|-----------|')
    if n == 6:
        print('|-----------|')
        print('| *   *   * |')
        print('|           |')
        print('| *   *   * |')
        print('|-----------|')

    a = input("press y or Y to roll again and any other key to exit:").lower()
    print('\n')
    

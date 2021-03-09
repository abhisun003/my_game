from numpy.random import choice 
a = 'y'

while a == 'y':
    m= list(range(1,7))
    no= choice(m,1,p=[0.19, 0.19, 0.19, 0.19, 0.19, 0.05])
    n=no[0]
    # print(n)

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
    
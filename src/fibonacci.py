import argparse


class fib_num():
    '''
    Calculates the fibonacci of the given number
    '''

    def __init__(self):
        self.des_num = []
        self.des_num = self.get_cmd_input()  # des_num = desirable number
        msg = ''
        if self.des_num[1]:
            msg = 'All fibonacci numbers up to the fibonacci number of {0} are\n'.format(
                self.des_num[0])
        else:
            msg = 'The fibonacci number of {0} is '.format(self.des_num[0])
        print(msg + str(self.fibonacci_calc(self.des_num[0], self.des_num[1])))

    def get_cmd_input(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            'number', help="Give a number on which you want to calculate the fibonacci")
        self.parser.add_argument(
            '-f', '--full', help="some test", action='store_true')
        self.args = self.parser.parse_args()
        return [int(self.args.number), bool(self.args.full)]

    def fibonacci_calc(self, num, des_flag):
        if des_flag:
            return self.fib_lister(num)
        else:
            return self.fib_solo(num)

    def fib_lister(self, list_num):
        retVal = []
        retVal.append(0)
        retVal.append(1)
        for i in range(2, list_num+1):
            retVal.append(retVal[i - 1] + retVal[i - 2])
        return retVal

    def fib_solo(self, solo_num):
        if solo_num == 0:
            return 0
        elif solo_num == 1:
            return 1
        else:
            return self.fib_solo(solo_num - 1) + self.fib_solo(solo_num - 2)


if __name__ == "__main__":
    fib_num()

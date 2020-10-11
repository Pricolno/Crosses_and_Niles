class Crosses_and_Niles:
    field = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    player = [-1, -1]
    now_move = 0
    symbols = ['x', 'o']
    winner = 'Игра ещё не закончилась'

    def print_field(self):
        for line in self.field:
            for cell in line:
                if cell == ' ':
                    print('_', end=' ')
                else:
                    print(cell, end=' ')
            print()
        print()
        return

    def do_move(self, x, y):
        if not self.check_in_field(x, y):
            print('Укажите верные координаты клетки\n')
            return

        if not (self.field[y][x] == ' '):
            print('Клетка занята, попробуйте сходить в другую')
            return

        self.field[y][x] = self.symbols[self.now_move]

        self.now_move = (self.now_move + 1) % 2

        finish_game, who_is_winner = self.check_game_over(x, y)
        if finish_game:
            if who_is_winner == ' ':
                self.winner = 'Ничья'
                return
            self.winner = self.player[who_is_winner]
            return

    def check_in_field(self, x_check, y_check):
        return 0 <= x_check < 3 and 0 <= y_check < 3

    def check_game_over(self, x, y):
        to_move = [[(1, 1), (-1, -1)],
                   [(1, 0), (-1, 0)],
                   [(0, 1), (0, -1)],
                   [(1, -1), (-1, 1)]]

        for two_direct in to_move:
            count_cell = {'o': 0, 'x': 0, ' ': 0}
            count_cell[self.symbols[self.now_move]] += 1

            for direct in two_direct:
                x_now, y_now = x, y
                while True:
                    x_now += direct[0]
                    y_now += direct[1]
                    if self.check_in_field(x_now, y_now):
                        count_cell[self.field[y_now][x_now]] += 1
                    else:
                        break
            if count_cell['o'] == 3:
                return True, 1
            if count_cell['x'] == 3:
                return True, 0

        all_cell_are_occupied = True
        for line in self.field:
            for cell in line:
                if cell == ' ':
                    all_cell_are_occupied = False

        if all_cell_are_occupied:
            return True, ' '
        else:
            return False, ' '

    def who_goes_there(self):
        if self.winner == 'Игра ещё не закончилась':
            print('Ходит ', self.player[self.now_move])
        else:
            print('Игра завершилась')
        return

    def who_is_winner(self):
        print(self.winner)

    def ask_game_over(self):
        if self.winner == 'Игра ещё не закончилась':
            print('Игра ещё не закончилась')
        else:
            print('Игра закончилась,', end=' ')
            if self.winner == 'Ничья':
                print('ничья')
            else:
                print('победил ', self.winner)


if __name__ == '__main__':
    crosses_and_niles = Crosses_and_Niles()
    print('Вы играете в игру Крестики-Нолики, назовите ваши имена в друх разных строчках')
    crosses_and_niles.player[0] = input()
    crosses_and_niles.player[1] = input()
    print('Первый игрок: ', crosses_and_niles.player[0], 'ходит крестиком')
    print('Второй игрок: ', crosses_and_niles.player[1], 'ходит ноликом')
    crosses_and_niles.print_field()
    while crosses_and_niles.winner == 'Игра ещё не закончилась':
        print('Введите команду\n1 x y - Cделать ход текущим игроком в клетку (x, y) 1 <= x,y <= 3')
        print('2 - Узнать, завершина ли игра')
        print('3 - Узнать кто победил')
        print('4 - Узнать чей сейчас ход')
        crosses_and_niles.print_field()
        request = list(map(int, input().split()))
        if request[0] == 1:
            crosses_and_niles.do_move(request[1] - 1, request[2] - 1)
        elif request[0] == 2:
            crosses_and_niles.ask_game_over()
        elif request[0] == 3:
            crosses_and_niles.who_is_winner()
        elif request[0] == 4:
            crosses_and_niles.who_goes_there()

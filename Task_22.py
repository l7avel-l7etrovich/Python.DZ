# 22. Создайте программу для игры с конфетами человек против человека.

#   Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#   Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#   Все конфеты оппонента достаются сделавшему последний ход. 
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""

from random import randint


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sweets = 0

    def take_sweets(self, maxx: int = 28) -> int:
        """
        Controls how many sweest player will take
        :param maxx: - maximum value
        :return: - number for counting
        """
        number = int(input(f"{self.name}, how many sweets will you take from the table? "))
        if number < 1 or number > maxx:
            number = int(input(f"{self.name}, you enter wrong number, try again: "))
        self.sweets += number
        return number

    def give_sweets(self) -> int:
        """Processes giveaway after loosing"""
        number = self.sweets
        self.sweets = 0
        return number

    def win(self) -> None:
        """Prints winning message"""
        print(f'Player {self.name} wins!!! All these sweeeeety sweets are yours, fatass!')

    def lose(self) -> None:
        """Prints losing message"""
        print(f'Player {self.name} lose. At least you will stay healthier')


class Bot(Player):

    def take_sweets(self, maxx: int = 28) -> int:
        """
        Controls how many sweest bot will take
        :param maxx: - maximum value
        :return: - number for counting
        """
        number = randint(1, maxx)
        self.sweets += number
        print(f'Bot took {number} sweets')
        return number

    def win(self) -> None:
        """Prints winning message"""
        print(f'Bot wins!!! Destroy all the sweets!')

    def lose(self) -> None:
        """Prints losing message"""
        print(f'Bot loses. But he remembers your name and your browser history.')


class Cheetbot(Bot):
    def lose(self) -> None:
        """Prints losing message"""
        print(
            "Cheetbot has suddenly eaten all his sweets. You will not get them."
            "\nSweets are digital, so yes it it possible")

    def give_sweets(self) -> int:
        """Processes giveaway after loosing"""
        self.sweets = 0
        number = self.sweets
        return number

    def cheet_take_sweets(self, number) -> int:
        """
        Controls how many sweest bot will take
        :param maxx: - maximum value
        :return: - number for counting
        """
        self.sweets += number
        print(f'Bot took {number} sweets')
        return number


class Game:
    def __init__(self, player1, player2, game_mode) -> None:
        self.table_sweets = 100
        self.game_mode = game_mode
        self.player1 = Player(name=player1)
        if self.game_mode == 0:
            self.player2 = Player(name=player2)
        elif self.game_mode == 1:
            self.player2 = Bot(name=player2)
        elif self.game_mode == 2:
            self.player2 = Cheetbot(name=player2)
        self.players = [self.player1, self.player2]
        self.index0 = 0
        self.index1 = 0

    def print_sweets_count(self) -> None:
        """Prints counts of sweets for players and table"""
        print(
            f'\nSweets on the table: {self.table_sweets}, {self.player1.name} has {self.player1.sweets} '
            f'sweets, {self.player2.name} has {self.player2.sweets} sweets\n')

    def lottery(self) -> None:
        """Decides who will turn first"""
        print('Lottery for first start says:')
        points_player1 = 0
        points_player2 = 0
        while points_player2 == points_player1:
            points_player1 = randint(1, 6)
            points_player2 = randint(1, 6)
            if points_player1 > points_player2:
                self.index0 = 0
                self.index1 = 1
                print(f'{self.player1.name} starts first!')
                break
            else:
                self.index0 = 1
                self.index1 = 0
                print(f'{self.player2.name} starts first!')
                break

    def finish(self, index: int) -> None:
        """Process finishing of the game pvp"""
        self.players[index].sweets += self.players[not index].give_sweets()
        self.players[index].win()
        self.players[not index].lose()
        self.print_sweets_count()
        quit()

    def bot_finish(self) -> None:
        """Process finishing of the game with bots"""
        self.player2.sweets += self.player1.give_sweets()
        self.player2.win()
        self.player1.lose()
        self.print_sweets_count()
        quit()

    def player_turn(self, index) -> None:
        """Processes game mechanic"""
        if self.players[index].__class__ == Player:
            if self.table_sweets < 28 and self.table_sweets != 0:
                number = self.players[index].take_sweets(self.table_sweets)
            else:
                number = self.players[index].take_sweets()

            self.table_sweets -= number
            self.print_sweets_count()
            if self.table_sweets == 0:
                self.finish(index)

        elif self.players[index].__class__ == Bot:
            if self.table_sweets < 28 and self.table_sweets != 0:
                number = self.player2.take_sweets(self.table_sweets)
            else:
                number = self.player2.take_sweets()
            self.table_sweets -= number
            self.print_sweets_count()
            if self.table_sweets == 0:
                self.bot_finish()

        elif self.players[index].__class__ == Cheetbot:
            if self.table_sweets < 28 and self.table_sweets != 0:
                number = self.player2.cheet_take_sweets(self.table_sweets)
            else:
                number = self.player2.take_sweets()
            self.table_sweets -= number
            self.print_sweets_count()
            if self.table_sweets == 0:
                self.bot_finish()

    def start(self) -> None:
        """Processes starting of the game"""
        self.lottery()
        self.print_sweets_count()
        while self.table_sweets > 0:
            self.player_turn(self.index0)
            self.player_turn(self.index1)


def main() -> None:
    game_mode = input('How would you like to play? pvp or bot or cheetbot? ')
    match game_mode:
        case 'pvp':
            player1_name = input("Enter Player1 name: ")
            player2_name = input("Enter Player2 name: ")
            game = Game(player1_name, player2_name, 0)
            game.start()
        case 'bot':
            player1_name = input("Enter Player1 name: ")
            player2_name = 'Bot'
            game = Game(player1_name, player2_name, 1)
            game.start()
        case 'cheetbot':
            player1_name = input("Enter Player1 name: ")
            player2_name = '!CheetBot!'
            game = Game(player1_name, player2_name, 2)
            game.start()
        case _:
            print('Wrong type of game!')


if __name__ == '__main__':
    main()
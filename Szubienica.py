import sys
import random
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

from PyQt5 import QtCore


class MainWindow (QWidget):

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(30, 20, 500, 200)
        self.setWindowTitle("szubienica")
        main_grid = QGridLayout()
        self.setLayout(main_grid)
        main_grid.addLayout(self.second_group(), 0, 0)

    def second_group(self):
        layout = QGridLayout()

        self.label_welcome_game = QLabel("Witaj w grze szubienica, Wybierz poziom trudności")
        self.label_welcome_game.setAlignment(Qt.AlignCenter)
        easy_button = QPushButton("Easy")
        medium_button = QPushButton("Medium")
        hard_button = QPushButton("Hard")

        layout.addWidget(self.label_welcome_game, 0, 0, 1, 3)
        layout.addWidget(easy_button, 1, 0)
        layout.addWidget(medium_button, 1, 1)
        layout.addWidget(hard_button, 1, 2)

        easy_button.clicked.connect(self.lvl_easy)
        medium_button.clicked.connect(self.lvl_medium)
        hard_button.clicked.connect(self.lvl_hard)

        return layout

    def show_new_window_game(self):
        self.w = SecondWindow()
        self.w.show()
        self.hide()

    def lvl_easy(self):
        self.number_of_tries = 15
        self.show_new_window_game()

    def lvl_medium(self):
        self.number_of_tries = 10
        self.show_new_window_game()

    def lvl_hard(self):
        self.number_of_tries = 7
        self.show_new_window_game()


class SecondWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(30, 20, 800, 300)
        self.setWindowTitle("szubienica")
        main_grid = QGridLayout()
        self.setLayout(main_grid)

        # main_grid.addLayout(self.first_group(), 0, 0)
        main_grid.addLayout(self.second_group(), 0, 0)

        return main_grid

    # def first_group(self):
    #
    #     layout_drawing = QGridLayout()
    #     self.label = QLabel(self)
    #     self.pixmap = QPixmap('unnamed.png')
    #     self.label.setPixmap(self.pixmap)
    #     self.label.resize(self.pixmap.width(), self.pixmap.height())
    #     self.show()
    #     layout_drawing.addWidget(self.label)
    #     return layout_drawing

    def second_group(self):

        self.number_of_tries = main_window.number_of_tries

        self.main_layout = QGridLayout()
        draw_word_button = QPushButton("Losuj słowo")
        self.main_layout.addWidget(draw_word_button, 0, 0)
        self.used_letters_list = []

        draw_word_button.clicked.connect(draw_word_button.hide)
        draw_word_button.clicked.connect(self.draw_a_word)
        draw_word_button.clicked.connect(self.add_buttons)

        return self.main_layout

    def add_buttons(self):
        self.used_letters_string = ""
        self.label_letters_used = QLabel("Used letters:\n " + self.used_letters_string, self)
        self.main_layout.addWidget(self.label_letters_used, 0, 0)
        self.label_attempts_remains = QLabel("Pozostało: " + str(self.number_of_tries) + " prób", self)
        self.main_layout.addWidget(self.label_attempts_remains, 0, 0)
        self.label_attempts_remains.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.main_layout.addLayout(self.buttons(), 2, 0)

    def buttons(self):

        self.layout_buttons = QGridLayout()

        self.button_q = QPushButton("Q")
        self.button_q.clicked.connect(partial(self.clicked_btn, 'Q'))
        self.button_w = QPushButton("W")
        self.button_w.clicked.connect(partial(self.clicked_btn, 'W'))
        self.button_e = QPushButton("E")
        self.button_e.clicked.connect(partial(self.clicked_btn, 'E'))
        self.button_r = QPushButton("R")
        self.button_r.clicked.connect(partial(self.clicked_btn, 'R'))
        self.button_t = QPushButton("T")
        self.button_t.clicked.connect(partial(self.clicked_btn, 'T'))
        self.button_y = QPushButton("Y")
        self.button_y.clicked.connect(partial(self.clicked_btn, 'Y'))
        self.button_u = QPushButton("U")
        self.button_u.clicked.connect(partial(self.clicked_btn, 'U'))
        self.button_i = QPushButton("I")
        self.button_i.clicked.connect(partial(self.clicked_btn, 'I'))
        self.button_o = QPushButton("O")
        self.button_o.clicked.connect(partial(self.clicked_btn, 'O'))
        self.button_p = QPushButton("P")
        self.button_p.clicked.connect(partial(self.clicked_btn, 'P'))
        self.button_a = QPushButton("A")
        self.button_a.clicked.connect(partial(self.clicked_btn, 'A'))
        self.button_s = QPushButton("S")
        self.button_s.clicked.connect(partial(self.clicked_btn, 'S'))
        self.button_d = QPushButton("D")
        self.button_d.clicked.connect(partial(self.clicked_btn, 'D'))
        self.button_f = QPushButton("F")
        self.button_f.clicked.connect(partial(self.clicked_btn, 'F'))
        self.button_g = QPushButton("G")
        self.button_g.clicked.connect(partial(self.clicked_btn, 'G'))
        self.button_h = QPushButton("H")
        self.button_h.clicked.connect(partial(self.clicked_btn, 'H'))
        self.button_j = QPushButton("J")
        self.button_j.clicked.connect(partial(self.clicked_btn, 'J'))
        self.button_k = QPushButton("K")
        self.button_k.clicked.connect(partial(self.clicked_btn, 'K'))
        self.button_l = QPushButton("L")
        self.button_l.clicked.connect(partial(self.clicked_btn, 'L'))
        self.button_z = QPushButton("Z")
        self.button_z.clicked.connect(partial(self.clicked_btn, 'Z'))
        self.button_x = QPushButton("X")
        self.button_x.clicked.connect(partial(self.clicked_btn, 'X'))
        self.button_c = QPushButton("C")
        self.button_c.clicked.connect(partial(self.clicked_btn, 'C'))
        self.button_v = QPushButton("V")
        self.button_v.clicked.connect(partial(self.clicked_btn, 'V'))
        self.button_b = QPushButton("B")
        self.button_b.clicked.connect(partial(self.clicked_btn, 'B'))
        self.button_n = QPushButton("N")
        self.button_n.clicked.connect(partial(self.clicked_btn, 'N'))
        self.button_m = QPushButton("M")
        self.button_m.clicked.connect(partial(self.clicked_btn, 'M'))

        self.layout_buttons.addWidget(self.button_q, 0, 0)
        self.layout_buttons.addWidget(self.button_w, 0, 1)
        self.layout_buttons.addWidget(self.button_e, 0, 2)
        self.layout_buttons.addWidget(self.button_r, 0, 3)
        self.layout_buttons.addWidget(self.button_t, 0, 4)
        self.layout_buttons.addWidget(self.button_y, 0, 5)
        self.layout_buttons.addWidget(self.button_u, 0, 6)
        self.layout_buttons.addWidget(self.button_i, 0, 7)
        self.layout_buttons.addWidget(self.button_o, 0, 8)
        self.layout_buttons.addWidget(self.button_p, 0, 9)
        self.layout_buttons.addWidget(self.button_a, 1, 0)
        self.layout_buttons.addWidget(self.button_s, 1, 1)
        self.layout_buttons.addWidget(self.button_d, 1, 2)
        self.layout_buttons.addWidget(self.button_f, 1, 3)
        self.layout_buttons.addWidget(self.button_g, 1, 4)
        self.layout_buttons.addWidget(self.button_h, 1, 5)
        self.layout_buttons.addWidget(self.button_j, 1, 6)
        self.layout_buttons.addWidget(self.button_k, 1, 7)
        self.layout_buttons.addWidget(self.button_l, 1, 8)
        self.layout_buttons.addWidget(self.button_z, 2, 1)
        self.layout_buttons.addWidget(self.button_x, 2, 2)
        self.layout_buttons.addWidget(self.button_c, 2, 3)
        self.layout_buttons.addWidget(self.button_v, 2, 4)
        self.layout_buttons.addWidget(self.button_b, 2, 5)
        self.layout_buttons.addWidget(self.button_n, 2, 6)
        self.layout_buttons.addWidget(self.button_m, 2, 7)

        return self.layout_buttons

    def clicked_btn(self, value):
        sender = self.sender().text()
        self.letter = sender
        self.add_letter()

    def win(self):
        self.label_win = QLabel("Wygrałeś \n Odgadnięte słowo to:" + self.random_word)
        self.label_win.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_win, 3, 0)
        self.hide_buttons()
        self.game_again = QPushButton("Grasz dalej kurwa ten?")
        self.main_layout.addWidget(self.game_again, 4,0)
        self.game_again.clicked.connect(self.new_game_win)

    def loose(self):

        self.label_game_over = QLabel("Game over \n poprawne słowo to:" + self.random_word)
        self.number_of_tries -= 1
        self.label_game_over.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_game_over, 3, 0)
        self.hide_buttons()
        self.game_again = QPushButton("Grasz dalej kurwa ten?")
        self.main_layout.addWidget(self.game_again, 4,0)
        self.game_again.clicked.connect(self.new_game_loose)



    def new_game_win(self):
        if main_window.number_of_tries == 15 or main_window.number_of_tries == 10:
            main_window.label_welcome_game.setText("Może coś trudniejszego?")
        else:
            main_window.label_welcome_game.setText("Wybierz poziom trudności")
        main_window.show()
        self.close()


    def new_game_loose(self):
        if main_window.number_of_tries == 10 or main_window.number_of_tries == 7:
            main_window.label_welcome_game.setText("Może coś łatwiejszego?")
        else:
            main_window.label_welcome_game.setText("Wybierz poziom trudności")
        main_window.show()
        self.close()



    def hide_buttons(self):
        self.button_q.setDisabled(True)
        self.button_w.setDisabled(True)
        self.button_e.setDisabled(True)
        self.button_r.setDisabled(True)
        self.button_t.setDisabled(True)
        self.button_y.setDisabled(True)
        self.button_u.setDisabled(True)
        self.button_i.setDisabled(True)
        self.button_o.setDisabled(True)
        self.button_p.setDisabled(True)
        self.button_a.setDisabled(True)
        self.button_s.setDisabled(True)
        self.button_d.setDisabled(True)
        self.button_f.setDisabled(True)
        self.button_g.setDisabled(True)
        self.button_h.setDisabled(True)
        self.button_j.setDisabled(True)
        self.button_k.setDisabled(True)
        self.button_l.setDisabled(True)
        self.button_z.setDisabled(True)
        self.button_x.setDisabled(True)
        self.button_c.setDisabled(True)
        self.button_v.setDisabled(True)
        self.button_b.setDisabled(True)
        self.button_n.setDisabled(True)
        self.button_m.setDisabled(True)

    def add_letter(self):
        letter = self.letter
        if self.number_of_tries > 1:
            if letter in self.random_word:
                new = ""
                for i in range(len(self.random_word)):
                    if letter == self.random_word[i]:
                        new += letter
                    else:
                        new += self.hide_word[i]
                self.hide_word = new
                self.label_word.hide()
                self.label_word = QLabel(self.hide_word, self)
                self.main_layout.addWidget(self.label_word, 0, 0)
                self.label_word.setAlignment(Qt.AlignCenter)
            else:
                if letter not in self.used_letters_list:
                    self.number_of_tries -= 1

            if letter not in self.used_letters_list:

                self.used_letters_list.append(letter)
                self.used_letters_string = " ".join(self.used_letters_list)

                self.label_word.hide()
                self.label_letters_used.hide()

                self.label_word = QLabel(self.hide_word, self)
                self.label_letters_used = QLabel("Used letters:\n " + self.used_letters_string, self)

                self.attempts = str(self.number_of_tries)

                self.main_layout.addWidget(self.label_word, 0, 0)
                self.label_word.setAlignment(Qt.AlignCenter)
                self.main_layout.addWidget(self.label_letters_used, 0, 0)

            if self.hide_word == self.random_word:
                self.win()


        else:
            self.loose()


        self.label_attempts_remains.hide()
        self.label_attempts_remains = QLabel("Pozostało: " + str(self.number_of_tries) + " prób", self)
        self.main_layout.addWidget(self.label_attempts_remains, 0, 0)
        self.label_attempts_remains.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

    def draw_a_word(self):
        words = open('wordlist.txt')
        draw = words.read().split()
        random_number = random.randint(1, 7776)
        self.random_word = draw[random_number]
        self.random_word = self.random_word.upper()
        self.hide_word = len(self.random_word) * "_"

        self.label_word = QLabel(self.hide_word, self)
        self.main_layout.addWidget(self.label_word, 0, 0)
        self.label_word.setAlignment(Qt.AlignCenter)

        self.attempts = str(self.number_of_tries + 1)
        self.label_attempts_remains = QLabel(self.attempts, self)
        print(self.random_word)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

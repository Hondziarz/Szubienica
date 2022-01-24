import sys
import random
from functools import partial

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
import wordlist



class MainWindow (QWidget):


    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):

        self.setGeometry(30, 20, 500, 200)
        self.setWindowTitle("szubienica")
        main_grid = QGridLayout()
        self.setLayout(main_grid)
        main_grid.addLayout(self.secondgroup(), 0, 0)

    def secondgroup(self):
        uklad_t = QGridLayout()


        label1 = QLabel("Witaj w grze szubienica, Wybierz poziom trudności")
        label1.setAlignment(Qt.AlignCenter)
        easy_button = QPushButton("Easy")
        medium_button = QPushButton("Medium")
        hard_button = QPushButton("Hard")

        uklad_t.addWidget(label1, 0, 0,1,3)
        uklad_t.addWidget(easy_button, 1, 0)
        uklad_t.addWidget(medium_button, 1, 1)
        uklad_t.addWidget(hard_button, 1, 2)


        easy_button.clicked.connect(partial(self.clicked_btn,15))
        medium_button.clicked.connect(partial(self.clicked_btn, 11))
        hard_button.clicked.connect(partial(self.clicked_btn, 7))

        return uklad_t



    def clicked_btn(self, value):
        sender = self.sender().text()
        self.letter = sender
        self.game = SecondWindow()
        self.game.show()



    def show_new_window_game(self):
        self.w = SecondWindow()
        self.w.show()





class SecondWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(30, 20, 800,300)
        self.setWindowTitle("szubienica")
        main_grid = QGridLayout()
        self.setLayout(main_grid)

        # main_grid.addLayout(self.firstgroup(), 0, 0)
        main_grid.addLayout(self.secondgroup(), 0, 0)

        return main_grid



    # def firstgroup(self):
    #
    #     uklad_x = QGridLayout()
    #     self.label = QLabel(self)
    #     self.pixmap = QPixmap('unnamed.png')
    #     self.label.setPixmap(self.pixmap)
    #     self.label.resize(self.pixmap.width(), self.pixmap.height())
    #     self.show()
    #     uklad_x.addWidget(self.label)
    #     return uklad_x

    def secondgroup(self):
        self.attempt = 10



        self.uklad1 = QGridLayout()
        draw_word_button = QPushButton("Losuj słowo")
        self.textedit = QLineEdit()
        self.uklad1.addWidget(draw_word_button,0,0)
        self.used_letters = []





        draw_word_button.clicked.connect(draw_word_button.hide)
        draw_word_button.clicked.connect(self.draw_a_word)


        draw_word_button.clicked.connect(self.addbuttons)

        return self.uklad1

    def addbuttons(self):
        self.uklad1.addLayout(self.buttons(), 2, 0)

    def buttons(self):

        self.uklad = QGridLayout()

        button_q = QPushButton("Q")
        button_q.clicked.connect(partial(self.clicked_btn, 'Q'))
        button_w = QPushButton("W")
        button_w.clicked.connect(partial(self.clicked_btn, 'W'))
        button_e = QPushButton("E")
        button_e.clicked.connect(partial(self.clicked_btn, 'E'))
        button_r = QPushButton("R")
        button_r.clicked.connect(partial(self.clicked_btn, 'R'))
        button_t = QPushButton("T")
        button_t.clicked.connect(partial(self.clicked_btn, 'T'))
        button_y = QPushButton("Y")
        button_y.clicked.connect(partial(self.clicked_btn, 'Y'))
        button_u = QPushButton("U")
        button_u.clicked.connect(partial(self.clicked_btn, 'U'))
        button_i = QPushButton("I")
        button_i.clicked.connect(partial(self.clicked_btn, 'I'))
        button_o = QPushButton("O")
        button_o.clicked.connect(partial(self.clicked_btn, 'O'))
        button_p = QPushButton("P")
        button_p.clicked.connect(partial(self.clicked_btn, 'P'))
        button_a = QPushButton("A")
        button_a.clicked.connect(partial(self.clicked_btn, 'A'))
        button_s = QPushButton("S")
        button_s.clicked.connect(partial(self.clicked_btn, 'S'))
        button_d = QPushButton("D")
        button_d.clicked.connect(partial(self.clicked_btn, 'D'))
        button_f = QPushButton("F")
        button_f.clicked.connect(partial(self.clicked_btn, 'F'))
        button_g = QPushButton("G")
        button_g.clicked.connect(partial(self.clicked_btn, 'G'))
        button_h = QPushButton("H")
        button_h.clicked.connect(partial(self.clicked_btn, 'H'))
        button_j = QPushButton("J")
        button_j.clicked.connect(partial(self.clicked_btn, 'J'))
        button_k = QPushButton("K")
        button_k.clicked.connect(partial(self.clicked_btn, 'K'))
        button_l = QPushButton("L")
        button_l.clicked.connect(partial(self.clicked_btn, 'L'))
        button_z = QPushButton("Z")
        button_z.clicked.connect(partial(self.clicked_btn, 'Z'))
        button_x = QPushButton("X")
        button_x.clicked.connect(partial(self.clicked_btn, 'X'))
        button_c = QPushButton("C")
        button_c.clicked.connect(partial(self.clicked_btn, 'C'))
        button_v = QPushButton("V")
        button_v.clicked.connect(partial(self.clicked_btn, 'V'))
        button_b = QPushButton("B")
        button_b.clicked.connect(partial(self.clicked_btn, 'B'))
        button_n = QPushButton("N")
        button_n.clicked.connect(partial(self.clicked_btn, 'N'))
        button_m = QPushButton("M")
        button_m.clicked.connect(partial(self.clicked_btn, 'M'))

        self.uklad.addWidget(button_q, 1, 0)
        self.uklad.addWidget(button_w, 1, 1)
        self.uklad.addWidget(button_e, 1, 2)
        self.uklad.addWidget(button_r, 1, 3)
        self.uklad.addWidget(button_t, 1, 4)
        self.uklad.addWidget(button_y, 1, 5)
        self.uklad.addWidget(button_u, 1, 6)
        self.uklad.addWidget(button_i, 1, 7)
        self.uklad.addWidget(button_o, 1, 8)
        self.uklad.addWidget(button_p, 1, 9)
        self.uklad.addWidget(button_a, 2, 0)
        self.uklad.addWidget(button_s, 2, 1)
        self.uklad.addWidget(button_d, 2, 2)
        self.uklad.addWidget(button_f, 2, 3)
        self.uklad.addWidget(button_g, 2, 4)
        self.uklad.addWidget(button_h, 2, 5)
        self.uklad.addWidget(button_j, 2, 6)
        self.uklad.addWidget(button_k, 2, 7)
        self.uklad.addWidget(button_l, 2, 8)
        self.uklad.addWidget(button_z, 3, 1)
        self.uklad.addWidget(button_x, 3, 2)
        self.uklad.addWidget(button_c, 3, 3)
        self.uklad.addWidget(button_v, 3, 4)
        self.uklad.addWidget(button_b, 3, 5)
        self.uklad.addWidget(button_n, 3, 6)
        self.uklad.addWidget(button_m, 3, 7)





        return self.uklad

    def clicked_btn(self, value):
        sender = self.sender().text()
        self.letter = sender
        self.add_word()



    def add_word(self):
        letter = self.letter




        if self.attempt > 1:


            if letter not in self.used_letters:

                self.used_letters.append(letter)
                str1 = " "
                self.x = str1.join(self.used_letters)
                self.label_letters_used = QLabel("Used letters:\n " + self.x, self)
                self.label_word.hide()
                self.label_letters_used.hide()
                self.label_letters_used.show()
                self.uklad.addWidget(self.label_letters_used, 0, 0, 1, 3)

                self.label_word = QLabel(self.hide_word, self)


                self.attempts = str(self.attempt)


                self.uklad.addWidget(self.label_word, 0, 4, 1, 5)

            if letter in self.random_word:


                new = ""
                for i in range(len(self.random_word)):
                    if letter == self.random_word[i]:
                        new += letter

                    else:
                        new += self.hide_word[i]
                self.hide_word = new
                self.label_word.hide()
                self.label_word = QLabel(self.hide_word,self)
                self.uklad.addWidget(self.label_word, 0, 4,1,5)
            else:
                self.attempt = self.attempt -1

        else:
            print("skonczyly ci sie literki")
            self.label_game_over = QLabel("Game over \n poprawne słowo to:" +self.random_word)
            self.attempt -= 1
            self.label_game_over.setAlignment(Qt.AlignCenter)
            self.uklad.addWidget(self.label_game_over,5,3,1,4)


        self.label_attempts_remains.hide()
        self.proby = str(self.attempt)
        self.label_attempts_remains = QLabel("Pozostało: " + self.proby + " prób", self)
        self.uklad.addWidget(self.label_attempts_remains, 0, 8, 1, 3)








    def draw_a_word(self):
        words = open('words.txt')
        losowanie = words.read().split()
        random_number = random.randint(1, 466550)
        self.random_word = losowanie[random_number]
        self.random_word = self.random_word.upper()
        self.hide_word = len(self.random_word) * "_"

        self.label_word = QLabel(self.hide_word,self)
        self.label_word.setAlignment(Qt.AlignCenter)
        self.uklad1.addWidget(self.label_word, 0, 0)

        self.attempts = str(self.attempt+1)
        self.label_attempts_remains = QLabel(self.attempts, self)


        return self.random_word










if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = MainWindow()
    okno.show()
    sys.exit(app.exec_())

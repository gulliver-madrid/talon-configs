from talon import actions, Module

mod = Module()

@mod.action_class
class Actions:
    def go_up_speed(n: int):
        "Go up n lines"
        for i in range(n):
            actions.edit.up()

    def go_down_speed(n: int):
        "Go down n lines"
        for i in range(n):
            actions.edit.down()

    def go_right_speed(n: int):
        "Go right n characters"
        for i in range(n):
            actions.edit.right()

    def go_left_speed(n: int):
        "Go left n characters"
        for i in range(n):
            actions.edit.left()

    def go_word_right_speed(n: int):
        "Go right n words"
        for i in range(n):
            actions.edit.word_right()

    def go_word_left_speed(n: int):
        "Go left n words"
        for i in range(n):
            actions.edit.word_left()

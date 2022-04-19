from pynput.mouse import Button, Controller


def MouseMove():
    mouse = Controller()
    print('The current pointer position is {0}', format(mouse.position))

    mouse.position = (1113.16259765625, 383.0130615234375)
    print('The current pointer position is {0}', format(mouse.position))

    mouse.move = (50, -50)

    mouse.press(Button.left)
    mouse.release(Button.left)

    mouse.click(Button.left, 2)
    mouse.scroll(0, 2)
    print('The current pointer position is {0}', format(mouse.position))


MouseMove()

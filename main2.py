from hex import Hex
game=Hex((1, -1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0))

hei=1
while True:
    game.print_board()
    game.do_action((int(input("i: ")), int(input("j: "))))
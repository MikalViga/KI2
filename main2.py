from hexKI import Hex
game=Hex((1,1,2,2,1,0,0,0,0,0))

while True:
    game.print_board()

    print("disjoint", (game.get_ds_red()))
    game.do_action((int(input("i: ")), int(input("j: "))))
    if game.is_final_state():
        game.print_board()
        break

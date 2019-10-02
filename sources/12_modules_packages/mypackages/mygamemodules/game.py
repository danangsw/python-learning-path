# game.py
# import draw module

# The Python script game.py will implement the game. It will use the function draw_game from the file draw.py

import draw

if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def play_game():
    return "game.play_game()"

def main():
    result = play_game()
    draw.draw_game(result)
    pass

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
    pass

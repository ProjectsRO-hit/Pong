from display import Display
from paddle import Paddle

#import screen
screen_build = Display()
screen = screen_build.make_screen()
screen_build.draw_divider()

#make paddle
paddle = Paddle()
paddle.make_paddle()

#move paddle up
screen_build.screen.listen()
screen_build.screen.onkeypress(paddle.move_up, "Up")
screen_build.screen.onkeypress(paddle.move_down, "Down")

game_on = True

while game_on:
    screen_build.screen.update()


#delete screen
screen_build.exit_screen()
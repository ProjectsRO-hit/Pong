from display import Display
from paddle import Paddle

#import screen
screen_build = Display()
screen = screen_build.make_screen()
screen_build.draw_divider()

#make paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


#move paddles
screen_build.screen.listen()
screen_build.screen.onkeypress(r_paddle.move_up, "Up")
screen_build.screen.onkeypress(r_paddle.move_down, "Down")
screen_build.screen.onkeypress(l_paddle.move_up, "w")
screen_build.screen.onkeypress(l_paddle.move_down, "s")


game_on = True

while game_on:
    screen_build.screen.update()


#delete screen
screen_build.exit_screen()
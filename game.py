from display import Display
from paddle import Paddle

#import screen
screen_build = Display()
screen = screen_build.make_screen()
screen_build.draw_divider()

#make paddle
paddle = Paddle()
paddle.make_paddle()

#delete screen
screen_build.exit_screen()
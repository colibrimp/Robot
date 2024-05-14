import pygame

pygame.init()

FPS = 8
clock = pygame.time.Clock()

# size background
HB = 560
WB = 1120
screen = pygame.display.set_mode((WB, HB))
bg_img = pygame.image.load("img/fon4.jpg").convert_alpha()

# icon
pygame.display.set_caption("Robot Pancho :-) [github.com/colibrimp]")
my_icon = pygame.image.load("img/icon_robot.png")
pygame.display.set_icon(my_icon)

# Player Robot Pancho
robot = [
    pygame.image.load("img/robot/robot2.png").convert_alpha(),
    pygame.image.load("img/robot/robot1.png").convert_alpha()
    ]

# size of robot
HR = -240
WR = 200


x = 100
y = 400

jump_robot = False
jump_count = 10



bg_x = 0

robot_count = 0


def move_robot():
    global robot_count

    if robot_count == 1:
        robot_count = 0
    else:
        robot_count += 1


# Move background
def move_fon():
    global bg_x
    screen.blit(bg_img, (bg_x, 0))
    screen.blit(bg_img, (bg_x + 1120, 0))
    bg_x -= 1
    if bg_x == -1120:
        bg_x = 0



def jump():
    global jump_count
    global jump_robot
    global y
    if jump_count >= -10:
        if jump_count < 0:
            y -= (jump_count ** 2) / 2
        else:

            y += (jump_count ** 2) / 2
        jump_count -= 1
    else:
        jump_robot = False
        jump_count = 10


# Monster
monster = [
    pygame.image.load("img/monster/m1.png").convert_alpha(),
    pygame.image.load("img/monster/m2.png").convert_alpha(),
    pygame.image.load("img/monster/m3.png").convert_alpha()
    ]

monster_x = WB
monster_y = 300



start = True
while start:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            start = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            move_robot()
            x += 20
        elif keys[pygame.K_a]:
            move_robot()
            x -= 20



        # jump
        if jump_robot == False:
            if keys[pygame.K_SPACE]:
                jump_robot = True
        else:
            if jump_count >= -10:
                y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 1
            else:
                jump()




    move_fon()

    screen.blit(robot[robot_count], (x, y, WR, HR))


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()





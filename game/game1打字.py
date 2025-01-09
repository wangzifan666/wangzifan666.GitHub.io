import sys
import random
import time
import pygame
from pygame.locals import *

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("打字速度游戏")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255, 255, 255
yellow = 255, 255, 0

# 游戏状态变量
key_flag = False
game_over = True
correct_answer = random.randint(97, 122)
score = 0
high_score = 0
start_time = 0
clock_start = 0
seconds = 11
current = 0

# 背景颜色
colors = [(0, 100, 0), (50, 50, 150), (100, 0, 100), (0, 150, 150)]
bg_color = random.choice(colors)

def print_text(font, x, y, text, color=white):
    img_text = font.render(text, True, color)
    screen.blit(img_text, (x, y))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if not game_over and event.key == correct_answer:
                correct_answer = random.randint(97, 122)
                score += 1
                clock_start = time.time()  # 重置单局倒计时
                if score > high_score:
                    high_score = score  # 更新最高分
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:  # 按下 Enter 键开始游戏
        if game_over:
            game_over = False
            score = 0
            start_time = time.time()  # 记录游戏总计时开始时间
            clock_start = time.time()  # 单局倒计时开始时间
            seconds = 11
            bg_color = random.choice(colors)  # 重置背景颜色

    # 清屏并设置背景色
    screen.fill(bg_color)

    # 当前时间
    current_time = time.time()
    # 总计时
    if game_over:
        elapsed_time = 0  # 游戏未开始，总时间为 0
    else:
        elapsed_time = current_time - start_time  # 总计时
        current = current_time - clock_start if not game_over else 0  # 单局计时

    # 显示提示信息
    print_text(font1, 0, 0, "How fast can you?")
    print_text(font1, 0, 30, "Complete within 10 seconds")
    print_text(font1, 0, 60, f"Total Time: {int(elapsed_time)}")
    print_text(font1, 400, 30, f"High Score: {high_score}", yellow)

    if elapsed_time >= 60:  # 游戏结束条件
        game_over = True
        print_text(font1, 0, 120, "Game Over! Final Score: " + str(score))
    else:
        if not game_over:
            # 单局倒计时结束，重新生成字母
            if seconds - current < 0:
                correct_answer = random.randint(97, 122)
                clock_start = time.time()  # 重置单局倒计时
                bg_color = random.choice(colors)  # 更改背景颜色

            # 显示计时条
            time_bar_width = max(0, int(600 * (seconds - current) / 10))
            pygame.draw.rect(screen, yellow, (0, 490, time_bar_width, 10))

        # 显示游戏信息
        print_text(font1, 0, 80, "Time: " + str(int(seconds - current)))
        print_text(font1, 0, 100, "Score: " + str(score))

    if game_over:
        print_text(font1, 0, 160, "...Press Enter to start the game...")

    # 显示目标字母（大写形式）
    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    pygame.display.update()
    clock.tick(60)


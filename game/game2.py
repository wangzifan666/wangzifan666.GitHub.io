import pygame
import random
import time

# 初始化pygame
pygame.init()

# 设置窗口尺寸
WIDTH, HEIGHT = 400, 600
FPS = 60

# 游戏颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 游戏配置
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 20
BLOCK_SPEED = 5

# 初始化游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('别踩白块')

# 创建游戏时钟
clock = pygame.time.Clock()

# 玩家初始位置
player_x = WIDTH // 2 - BLOCK_WIDTH // 2
player_y = HEIGHT - BLOCK_HEIGHT - 10
player_speed = 10

# 块的列表
blocks = []

# 游戏状态
game_over = False

# 生成一个白块
def generate_block():
    x = random.randint(0, WIDTH - BLOCK_WIDTH)
    return pygame.Rect(x, 0, BLOCK_WIDTH, BLOCK_HEIGHT)

# 处理玩家输入
def handle_input():
    global player_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - BLOCK_WIDTH:
        player_x += player_speed

# 更新块的位置
def update_blocks():
    global game_over
    for block in blocks:
        block.y += BLOCK_SPEED
        if block.y >= HEIGHT:
            blocks.remove(block)
        if block.colliderect(pygame.Rect(player_x, player_y, BLOCK_WIDTH, BLOCK_HEIGHT)):
            game_over = True
            break

# 画出游戏元素
def draw():
    screen.fill(BLACK)
    # 绘制玩家
    pygame.draw.rect(screen, RED, (player_x, player_y, BLOCK_WIDTH, BLOCK_HEIGHT))
    # 绘制白块
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)
    pygame.display.update()

# 主游戏循环
def game_loop():
    global game_over
    last_block_time = time.time()
    
    while not game_over:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # 玩家输入
        handle_input()

        # 每0.5秒生成一个新的白块
        if time.time() - last_block_time >= 0.5:
            blocks.append(generate_block())
            last_block_time = time.time()

        # 更新块的位置
        update_blocks()

        # 画出游戏画面
        draw()

        # 控制游戏帧率
        clock.tick(FPS)

    # 游戏结束
    print("Game Over")
    pygame.quit()

# 启动游戏
if __name__ == "__main__":
    game_loop()

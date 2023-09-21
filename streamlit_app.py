pip install pygame
import pygame
import sys
from pygame.locals import *
import random

# Pygameの初期化
pygame.init()

# 画面の幅と高さ
WIDTH, HEIGHT = 800, 600

# 画面の作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# タイトル
pygame.display.set_caption("動く球体")

# 色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 球体の位置と速度
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.uniform(1, 5)
ball_speed_y = random.uniform(1, 5)

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 球体の位置を更新
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 画面外に出た場合、反射させる
    if ball_x < 0 or ball_x > WIDTH:
        ball_speed_x *= -1
    if ball_y < 0 or ball_y > HEIGHT:
        ball_speed_y *= -1

    # 画面を白でクリア
    screen.fill(WHITE)

    # 球体を描画
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # 画面更新
    pygame.display.update()

    # フレームレートを制御
    pygame.time.delay(20)


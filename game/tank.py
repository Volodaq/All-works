import pgzrun
import random

WIDTH = 800
HEIGHT = 600

tank = Actor('tank_up', (400, 300))  # Игрок
bullets = []  # Список пуль
enemies = []  # Список противников
explosions = []  # Список взрывов

# Создаем противников
for _ in range(5):
    enemy = Actor('tank_enemy', (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))
    enemies.append(enemy)


def draw():
    screen.clear()
    tank.draw()

    # Отрисовываем пули
    for bullet in bullets:
        bullet.draw()

    # Отрисовываем противников
    for enemy in enemies:
        enemy.draw()

    # Отрисовываем взрывы
    for explosion in explosions:
        explosion.draw()


def update():
    move_tank()  # Функция для перемещения танка

    # Обновляем пули
    for bullet in bullets:
        bullet.x += bullet.vx
        bullet.y += bullet.vy

        # Проверка на выход за пределы экрана
        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets.remove(bullet)

        # Проверка столкновений пули с танками противников
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)  # Удаляем противника
                bullets.remove(bullet)  # Удаляем пулю
                create_explosion(enemy.x, enemy.y)  # Создаем взрыв

    # Анимация взрывов
    for explosion in explosions:
        explosion.image = 'explosion2'  # Меняем изображение взрыва
        explosions.remove(explosion)  # Удаляем взрыв после отрисовки


def on_key_down(key):
    if key == keys.SPACE:
        shoot()


def move_tank():
    if keyboard.left:
        tank.x -= 5
        tank.angle = 180  # Поворачиваем танк влево
    elif keyboard.right:
        tank.x += 5
        tank.angle = 0  # Поворачиваем танк вправо
    elif keyboard.up:
        tank.y -= 5
        tank.angle = 90  # Поворачиваем танк вверх
    elif keyboard.down:
        tank.y += 5
        tank.angle = 270  # Поворачиваем танк вниз


def shoot():
    # Создаем пулю
    bullet = Actor('bullet', (tank.x, tank.y))

    # Определяем направление пули
    if tank.angle == 0:
        bullet.vx = 5  # Вправо
        bullet.vy = 0
    elif tank.angle == 180:
        bullet.vx = -5  # Влево
        bullet.vy = 0
    elif tank.angle == 90:
        bullet.vx = 0  # Вверх
        bullet.vy = -5
    elif tank.angle == 270:
        bullet.vx = 0  # Вниз
        bullet.vy = 5

    bullets.append(bullet)  # Добавляем пулю в список


def create_explosion(x, y):
    explosion = Actor('explosion1', (x, y))  # Спрайт взрыва
    explosions.append(explosion)


pgzrun.go()

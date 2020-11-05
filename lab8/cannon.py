from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self, x=40.0, y=450.0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.angle = 0
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.lifetimer = 2    # in seconds

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self, g, recovery_factor):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        Args:
        g - ускорение свободного падения
        recovery_factor - во столько раз увеличится модуль скорости после столкновения, число (0;1)
        """
        x = self.x
        y = self.y
        vx = self.vx
        vy = self.vy
        r = self.r

        vy += 250 * g * delta_time    # 250 pixels : 1 meter
        x += vx * delta_time
        y += vy * delta_time

        if x > 800 - r:
            x = 800 - r
            vx = -vx * recovery_factor
        if x < r:
            x = r
            vx = -vx * recovery_factor
        if y > 600 - r:
            y = 600 - r
            vy = -vy * recovery_factor
        if y < r:
            y = r
            vy -= vy * recovery_factor

        canv.move(self.id, vx * delta_time, vy * delta_time + 250 * g * delta_time**2 / 2)

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (self.r + obj.r) ** 2:
            return True
        return False

class Gun():
    def __init__(self):
        self.fire_power = 10
        self.fire_on = False
        self.angle = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7) 

    def fire_start(self, event):
        self.fire_on = True

    def fire_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r = 15
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = 20 * self.fire_power * math.cos(self.angle)
        new_ball.vy = 20 * self.fire_power * math.sin(self.angle)
        balls += [new_ball]
        self.fire_on = False
        self.fire_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            x = event.x
            y = event.y
            if x < 21:
                x = 21
            self.angle = math.atan((y - 450) / (x - 20))
        
        if self.fire_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.fire_power, 20) * math.cos(self.angle),
                    450 + max(self.fire_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.fire_on:
            if self.fire_power < 100:
                self.fire_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = True
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        self.live = False
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        pass



gun = Gun()
target = Target()
screen1 = canv.create_text(400, 300, text='', font='28')

FPS = 100
delta_time = 1 / FPS

def new_game(event=''):
    global gun, target, screen1, balls, bullet
    target.new_target()
    bullet = 0    # number of wasted bullets
    balls = []
    canv.bind('<Button-1>', gun.fire_start)
    canv.bind('<ButtonRelease-1>', gun.fire_end)
    canv.bind('<Motion>', gun.targetting)
  
    target.live = True
    while target.live or balls:
        for ball in balls:
            ball.move(9.8, 0.8)
            ball.lifetimer -= delta_time
            if ball.lifetimer <= 0:
                balls.remove(ball)
                canv.delete(ball.id)
            if ball.hit_test(target) and target.live:
                target.live = False
                target.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(delta_time)
        gun.targetting()
        gun.power_up()
    canv.delete(Target)
    canv.itemconfig(screen1, text='')
    root.after(750, new_game)


new_game()

tk.mainloop()
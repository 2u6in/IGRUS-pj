from cs1graphics import *
from time import *

paper = Canvas()

paper.setBackgroundColor('light blue')
paper.setWidth(1000)
paper.setHeight(500)
paper.setTitle('catstealfish')
timeDelay = 0.1
sleep(timeDelay)

cat = Layer()
shop = Layer()
shop2 = Layer()
fish = Layer()
person = Layer()


def draw_obj():
    head = Circle(50, Point(250, 200))
    head.setFillColor('black')
    cat.add(head)

    ear1 = Polygon(Point(180, 130), Point(200, 200), Point(250, 170))
    ear1.setFillColor('black')
    cat.add(ear1)

    ear2 = Polygon(Point(320, 130), Point(290, 230), Point(260, 170))
    ear2.setFillColor('black')
    cat.add(ear2)

    eye1 = Circle(15, Point(220, 205))
    eye1.setFillColor('yellow')
    cat.add(eye1)

    eye2 = Circle(15, Point(280, 205))
    eye2.setFillColor('yellow')
    cat.add(eye2)

    body = Rectangle(130, 65, Point(300, 280))
    body.setFillColor('black')
    body.setDepth(60)
    cat.add(body)

    leg1 = Rectangle(20, 60, Point(245, 320))
    leg1.setFillColor('black')
    cat.add(leg1)
    leg2 = Rectangle(20, 60, Point(270, 320))
    leg2.setFillColor('black')
    cat.add(leg2)
    leg3 = Rectangle(20, 60, Point(330, 320))
    leg3.setFillColor('black')
    cat.add(leg3)
    leg4 = Rectangle(20, 60, Point(355, 320))
    leg4.setFillColor('black')
    cat.add(leg4)

    tail = Rectangle(15, 70, Point(357, 213))
    tail.setFillColor('black')
    cat.add(tail)

    paper.add(cat)

    cat.moveTo(600, 100)
    cat.setDepth(10)


def draw_shop():
    pan = Rectangle(450, 120, Point(750, 350))
    pan.setFillColor("chocolate4")
    pan.setDepth(300)
    shop.add(pan)
    colum = Rectangle(15, 150, Point(580, 220))
    colum.setFillColor("chocolate4")
    colum.setDepth(310)
    shop.add(colum)
    colum2 = Rectangle(15, 150, Point(930, 220))
    colum2.setFillColor("chocolate4")
    colum2.setDepth(310)
    shop.add(colum2)

    roof = Layer()

    top_y = 130
    bottom_y = 220
    bottom_left_x = 550
    bottom_right_x = 980

    top_width = 300
    top_left_x = (bottom_left_x + bottom_right_x) / 2 - top_width / 2
    top_right_x = (bottom_left_x + bottom_right_x) / 2 + top_width / 2

    stripe_count = 9
    for i in range(stripe_count):
        ratio1 = i / stripe_count
        ratio2 = (i + 1) / stripe_count

        top_x1 = top_left_x + (top_right_x - top_left_x) * ratio1
        top_x2 = top_left_x + (top_right_x - top_left_x) * ratio2

        bottom_x1 = bottom_left_x + (bottom_right_x - bottom_left_x) * ratio1
        bottom_x2 = bottom_left_x + (bottom_right_x - bottom_left_x) * ratio2

        stripe = Polygon(
            Point(top_x1, top_y),
            Point(top_x2, top_y),
            Point(bottom_x2, bottom_y),
            Point(bottom_x1, bottom_y)
        )

        stripe.setFillColor("blue" if i % 2 == 0 else "white")
        stripe.setDepth(250)
        roof.add(stripe)

    roof.moveTo(-10, -40)
    shop.add(roof)
    paper.add(shop)


def draw_shop2():
    pan = Rectangle(450, 120, Point(750, 350))
    pan.setFillColor("chocolate4")
    pan.setDepth(300)
    shop2.add(pan)
    colum = Rectangle(15, 150, Point(580, 220))
    colum.setFillColor("chocolate4")
    colum.setDepth(310)
    shop2.add(colum)
    colum2 = Rectangle(15, 150, Point(930, 220))
    colum2.setFillColor("chocolate4")
    colum2.setDepth(310)
    shop2.add(colum2)

    roof2 = Layer()

    top_y = 130
    bottom_y = 220
    bottom_left_x = 550
    bottom_right_x = 980

    top_width = 300
    top_left_x = (bottom_left_x + bottom_right_x) / 2 - top_width / 2
    top_right_x = (bottom_left_x + bottom_right_x) / 2 + top_width / 2

    stripe_count = 9
    for i in range(stripe_count):
        ratio1 = i / stripe_count
        ratio2 = (i + 1) / stripe_count

        top_x1 = top_left_x + (top_right_x - top_left_x) * ratio1
        top_x2 = top_left_x + (top_right_x - top_left_x) * ratio2

        bottom_x1 = bottom_left_x + (bottom_right_x - bottom_left_x) * ratio1
        bottom_x2 = bottom_left_x + (bottom_right_x - bottom_left_x) * ratio2

        stripe = Polygon(
            Point(top_x1, top_y),
            Point(top_x2, top_y),
            Point(bottom_x2, bottom_y),
            Point(bottom_x1, bottom_y)
        )

        stripe.setFillColor("red" if i % 2 == 0 else "white")
        stripe.setDepth(250)
        roof2.add(stripe)

    roof2.moveTo(-10, -40)
    shop2.add(roof2)
    paper.add(shop2)
    shop2.moveTo(-500, 0)
    shop2.setDepth(450)


def draw_fish():

    body = Ellipse(60, 30, Point(750, 320))
    body.setFillColor("lightgray")
    body.setBorderColor("black")
    fish.add(body)

    tail = Polygon(Point(780, 320), Point(800, 305), Point(800, 335))
    tail.setFillColor("lightgray")
    tail.setBorderColor("black")
    fish.add(tail)

    fish.setDepth(20)
    paper.add(fish)
    fish.moveTo(-80, -40)


def draw_person():
    head = Circle(50)
    head.setFillColor("white")
    body = Rectangle(70, 150, Point(0, 100))
    body.setFillColor("white")
    body.setDepth(100)

    leg1 = Rectangle(20, 40, Point(-20, 190))
    leg1.setFillColor("white")
    leg1.setDepth(110)

    leg2 = Rectangle(20, 40, Point(20, 190))
    leg2.setFillColor("white")
    leg2.setDepth(110)

    apron = Rectangle(60, 100, Point(0, 110))
    apron.setFillColor("pink")
    apron.setBorderColor("hotpink")
    apron.setDepth(90)

    strap_left = Rectangle(5, 20, Point(-18, 50))
    strap_left.setFillColor("pink")
    strap_left.setBorderColor("hotpink")
    strap_left.setDepth(90)

    strap_right = Rectangle(5, 20, Point(18, 50))
    strap_right.setFillColor("pink")
    strap_right.setBorderColor("hotpink")
    strap_right.setDepth(90)

    person.add(head)
    person.add(body)
    person.add(leg1)
    person.add(leg2)
    person.add(apron)
    person.add(strap_left)
    person.add(strap_right)

    paper.add(person)
    person.moveTo(750, 200)
    person.setDepth(300)


def show_animation():
    for i in range(16):
        sleep(timeDelay)
        cat.move(-11, 0)
    fish.setDepth(10)
    fish.move(-10, 55)

    person.move(0, -20)
    sleep(timeDelay)
    person.move(0, 20)

    for i in range(5):
        sleep(timeDelay)
        cat.move(-60, 0)
        fish.move(-60, 0)

    while (True):

        for i in range(30):
            sleep(timeDelay)
            cat.move(-60, 0)
            fish.move(-60, 0)
            person.move(-60, 0)

        cat.moveTo(1000, 100)
        fish.moveTo(500, 10)
        person.moveTo(1600, 200)
        person.setDepth(10)


draw_obj()
draw_shop()
draw_fish()
draw_shop2()
draw_person()
ground = Rectangle(1000, 100)
paper.add(ground)
ground.setFillColor("gray")
ground.moveTo(500, 450)
ground.setDepth(500)

show_animation()

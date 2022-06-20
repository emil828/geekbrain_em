# Lesson 5

class Stationary:
    def __init__(self, title='Может рисовать'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой', self.title)


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом', self.title)


class Handler(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером', self.title)


st = Stationary()
st.draw()

pen = Pen('Parker')
pen.draw()

pencil = Pencil('Pencil')
pencil.draw()

marker = Handler('Luxor')
marker.draw()



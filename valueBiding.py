from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=5).bind_value(demo, 'number')
    ui.toggle({1: 'Ayrton Senna', 2: 'Hamilton', 3: 'Sergio Perez', 4: 'Niki Lauda', 5: 'Max Verstappen'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()
from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic', on_click=lambda: ui.notify('hiciste clic'))
with ui.row():
    ui.checkbox('yes sir', on_change=show)
    ui.switch('claro que chi', on_change=show)
ui.radio(['Jujutsu Kaisen', 'One punch man', 'Evangelion'], value='Jujutsu Kaisen', on_change=show).props('inline')
with ui.row():
    ui.input('Introduce texto', on_change=show)
    ui.select(['chi', 'ño'], value='chi', on_change=show)
ui.link('Hay mas, con confianza :)...', '/documentation').classes('mt-8')

ui.run()
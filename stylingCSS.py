from nicegui import ui

ui.icon('thumb_up', color='#a46dfc').classes('text-6xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Yael').style('color: #a46dfc; font-family: Lobster')
    ui.label('Ayrton Senna').classes('font-serif')
    ui.label('Mexico').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()
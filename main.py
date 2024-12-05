#!/usr/bin/env python3
from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(0, 0, 0)
    scene.stl('/stl/Dragoon_All.stl').move(z=1).scale(0.03).material(color='#a46dfc')

ui.run()
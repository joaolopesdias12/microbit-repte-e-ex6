def on_forever():
    led.plot_bar_graph(input.temperature(), 50, True)
basic.forever(on_forever)

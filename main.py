elapsed2 = 0
start = 0
elapsed = 0

def on_button_a():
    global elapsed2
    elapsed2 = input.running_time() - start
    basic.show_number(Math.idiv(elapsed, 1000))
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    global start
    start = input.running_time()
    basic.show_number(0)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    global elapsed
    elapsed = input.running_time() - start
input.on_button_event(Button.B, input.button_event_click(), on_button_b)
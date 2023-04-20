let elapsed2 = 0
let start = 0
let elapsed = 0
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    elapsed2 = input.runningTime() - start
    basic.showNumber(Math.idiv(elapsed, 1000))
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    start = input.runningTime()
    basic.showNumber(0)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    elapsed = input.runningTime() - start
})

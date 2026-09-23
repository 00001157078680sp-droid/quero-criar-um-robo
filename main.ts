function andar_e_correr () {
    IANNY_KAELLY_RODRIGUES_DE_OLIVEIRA = [0, 1]
    game.addLife(11)
}
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("E B A D G E G F ", 119), music.PlaybackMode.UntilDone)
    control.waitForEvent(4, 90)
})
let IANNY_KAELLY_RODRIGUES_DE_OLIVEIRA: number[] = []
led.unplot(4, 1)
led.plot(3, 1)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    serial.writeLine("" + (control.eventValue()))
    radio.sendNumber(3 * 9)
})

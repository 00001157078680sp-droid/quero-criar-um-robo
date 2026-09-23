def andar_e_correr():
    global IANNY_KAELLY_RODRIGUES_DE_OLIVEIRA
    IANNY_KAELLY_RODRIGUES_DE_OLIVEIRA = [0, 1]
    game.add_life(11)

def on_button_pressed_b():
    music.play(music.string_playable("E B A D G E G F ", 119),
        music.PlaybackMode.UNTIL_DONE)
    control.wait_for_event(4, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

IANNY_KAELLY_RODRIGUES_DE_OLIVEIRA: List[number] = []
led.unplot(4, 1)
led.plot(3, 1)

def on_forever():
    serial.write_line("" + str((control.event_value())))
    radio.send_number(3 * 9)
basic.forever(on_forever)

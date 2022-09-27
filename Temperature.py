Current_Temperature = 0
# Created by: Owen Whalley
# Created on: 2022/09/27
#
# Finding current temperature and refreshing every second.

def on_forever():
    global Current_Temperature
    Current_Temperature = input.temperature()
    basic.show_number(Current_Temperature)
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)
 

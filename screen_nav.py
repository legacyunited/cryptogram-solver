screen_helper = """

ScreenManager:
    WelcomeScreen:
    HomeScreen:

<WelcomeScreen>:
    name: 'welcome'
    Image:
        source: 'media/wallpaper2.jpg'
    MDFloatingActionButton:
        icon: "location-enter"
        on_press: root.manager.current = 'home'
        halign: "center"

<HomeScreen>:
    name: 'home'
    Image:
        source: 'media/wallpaper3.jpg'
    MDLabel:
        text: 'you are home'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        color: 'white'
    MDFloatingActionButton:
        icon: "android"
        on_press: root.manager.current = 'welcome'
        halign: "center"

"""
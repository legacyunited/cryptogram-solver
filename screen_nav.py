screen_helper = """
ScreenManager:
    WelcomeScreen:
    HomeScreen:
    TransitionScreen:
    ResultScreen:


<WelcomeScreen>:
    name: 'welcome'
    Image:
        source: 'media/wallpaper2.jpg'
    MDRaisedButton:
        text: "Get Started"
        pos_hint: {"center_x": 0.5, "center_y":0.3}
        size_hint: (0.5,0.1)
        font_size: '20sp'
        elevation_normal: 10
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.current = 'home'
        

<HomeScreen>:
    name: 'home'
    Camera:
        id: camera
        resolution: (280, 180)
    MDFloatingActionButton:
        icon: "camera"
        pos_hint: {"center_x": 0.5, "center_y":0.2}
        shadow_pos: 0, 0
        elevation_normal: 8
        on_press:
            root.manager.transition.direction = 'left'
            root.capture()

<TransitionScreen>:
    name: 'transition'
    Image:
        id: image
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDProgressBar:
        id: progress
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        size_hint_x: 0.5
        type: "indeterminate"
    MDRaisedButton:
        text: "Back"
        pos_hint: {"center_x": 0.28, "center_y":0.15}
        size_hint: (0.4,0.1)
        font_size: '20sp'
        elevation_normal: 10
        md_bg_color: (255/255.0,193/255.0,0/255.0,1)
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'home'
    MDRaisedButton:
        text: "Let's Decrypt"
        pos_hint: {"center_x": 0.72, "center_y":0.15}
        size_hint: (0.4,0.1)
        font_size: '20sp'
        elevation_normal: 10
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'result'

<ResultScreen>:
    name: "result"
    Image:
        id: image
        pos_hint: {"center_x":0.5, "center_y":0.8}
    MDProgressBar:
        id: pb
        height: "2dp"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        size_hint_x: 0.6
    MDLabel:
        id: label
        pos_hint: {"center_x":0.5, "center_y":0.56}
        halign: 'center'
        valign: 'top'
        theme_text_color: 'Hint'
    MDLabel:
        id: h1
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: 'center'
        text: "Encrypted Text"
        bold: True
        font_size: '20sp'
        color: (0,99,251,1)
    MDLabel:
        id: label2
        pos_hint: {"center_x":0.5, "center_y":0.44}
        halign: 'center'
        text: "This is how the text should look life if it is super long, although the limit is unknown to humanity."
    MDSeparator:
        id: separator
        height: "4dp"
        pos_hint: {"center_x":0.5, "center_y":0.32}
        size_hint_x: 0.6
    MDLabel:
        id: h2
        pos_hint: {"center_x":0.5, "center_y":0.28}
        halign: 'center'
        text: "Decrypted Result"
        bold: True
        font_size: '20sp'
        color: (0,99,255,1)
    MDLabel:
        id: label3
        pos_hint: {"center_x":0.5, "center_y":0.22}
        halign: 'center'
        text: "This is how the resultant text should look life, although the limit is unknown to humanity."
    MDRaisedButton:
        id: start_over
        text: "Capture More"
        size_hint: (0,0)
        pos_hint: {"center_x": 0.5, "center_y":0.08}
        font_size: '15sp'
        elevation_normal: 10
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'home'

"""
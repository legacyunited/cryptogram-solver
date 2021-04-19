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
        angle: 90
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
        pos_hint: {"center_x":0.5, "center_y":0.82}
    MDLabel:
        id: label
        pos_hint: {"center_x":0.5, "center_y":0.65}
        halign: 'center'
        valign: 'top'
        theme_text_color: 'Hint'
        font_size: '12sp'
    MDProgressBar:
        id: pb
        height: "2dp"
        pos_hint: {"center_x":0.5, "center_y":0.63}
        size_hint_x: 0.9
    MDTextField:
        id: label2
        hint_text: "Encrypted Text"
        helper_text: "Verify the encrypted text."
        pos_hint: {"center_x":0.5, "center_y":0.51}
        size_hint: (0.85, None)
        height: 7
        multiline : True
        text_color: (117,117,114,1)
        helper_text: "Validate text before submitting"
        helper_text_mode: "persistent"
    MDRoundFlatButton:
        id: solve
        text: "Solve"
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        pos_hint: {"center_x":0.5, "center_y":1.5}
        visible: False
        on_press:
            root.decrypt()
    MDSeparator:
        id: separator
        height: "4dp"
        pos_hint: {"center_x":0.5, "center_y":0.32}
        size_hint_x: 0.6
    MDLabel:
        id: h2
        pos_hint: {"center_x":0.5, "center_y":0.29}
        halign: 'center'
        text: "Decrypted Result"
        bold: True
        font_size: '20sp'
        color: (0,99,255,1)
    MDLabel:
        id: label3
        pos_hint: {"center_x":0.5, "center_y":0.20}
        halign: 'center'
        size_hint_x: 0.85
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

#commented image resolution
'''
size_hint: 0.88, 0.32
        allow_stretch: True
'''
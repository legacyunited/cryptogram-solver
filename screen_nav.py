screen_helper = """
ScreenManager:
    WelcomeScreen:
    HomeScreen:
    TransitionScreen:
    LoadingScreen:
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
        on_press: root.manager.current = 'home'

<HomeScreen>:
    name: 'home'
    Camera:
        id: camera
        resolution: (160, 200)
    MDFloatingActionButton:
        icon: "camera"
        pos_hint: {"center_x": 0.5, "center_y":0.2}
        shadow_pos: 0, 0
        elevation_normal: 8
        on_press: root.capture()

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
        text: "Let's Decrypt"
        icon: "arrow_back"
        pos_hint: {"center_x": 0.5, "center_y":0.15}
        size_hint: (0.5,0.1)
        font_size: '20sp'
        elevation_normal: 10
        on_press: root.manager.current = 'loading'

<LoadingScreen>:
    name: "loading"
    MDSpinner:
        size_hint: (None, None)
        size: (dp(15), dp(15))
        palette: [[0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1], [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1], [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1], [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1]]
    MDRaisedButton:
        text: "Let's Decrypt"
        icon: "done_all"
        pos_hint: {"center_x": 0.5, "center_y":0.15}
        size_hint: (0.5,0.1)
        font_size: '20sp'
        elevation_normal: 10
        on_press: root.manager.current = 'result'


<ResultScreen>:
    name: "result"
    Label:
        text: "Geronimo!"


"""
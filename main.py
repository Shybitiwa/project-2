from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from threading import Timer
from kivy.clock import mainthread
import webbrowser
from kivy.core.text import LabelBase
from kivy.core.window import Window
from plyer import notification

# import os

# tools_path = os.path.dirname(__file__)
# icons_path = os.path.join(tools_path, "Nordhin.ttf")
# LabelBase.register(name="amhFont", fn_regular="washrab.ttf")

# Window.size = (345, 620)


class MainApp(MDApp):
    def build(self):
        self.title = "ReadNow"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("kivyFile.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elJuSIds = [
            "eScience",
            "eMath",
            "eArt",
            "eSocialStudies",
            "eMusic",
            "eSport",
            "eEnglish",
            "eForeignLanguage",
        ]
        self.hiSIds = [
            "hBiology",
            "hPhysics",
            "hChemistry",
            "hMath",
            "hArt",
            "hGeography",
            "hHistory",
            "hCivics",
            "hSport",
            "hEnglish",
            "hForeignLanguage",
        ]
        self.naHiSIds = [
            "nBiology",
            "nMath",
            "nChemistry",
            "nEarthScience",
            "nEnvironmentScience",
            "nSport",
            "nForeignLanguage",
            "nPhyics",
            "nIct",
            "nEnglish",
        ]
        self.SoHiSIds = [
            "sAnthropologySociology",
            "sMath",
            "sGeography",
            "sEconomics",
            "sGovernmentCivics",
            "sSport",
            "sEnglish",
            "sHistory",
            "sForeignLanguage",
            "sPhyics",
            "sCurrentEvents",
        ]
        self.sIds = [self.elJuSIds, self.hiSIds, self.naHiSIds, self.SoHiSIds]
        self.paused = True
        self.currentSlider = 0
        self.numberOfSliders = 0
        self.idNumber = 0
        self.CValue = 60

    def backButton(self):
        self.root.ids.SM.transition.direction = "right"
        self.root.ids.SM.current = "main"

    def jumpToScreen(self, Screen):
        self.root.ids.SM.transition.direction = "left"
        self.root.ids.SM.current = Screen

    def reloadSliders(self, screenCode, NS, SV):
        self.paused = False
        self.pauseButton(screenCode, NS)
        self.idNumber = screenCode
        self.numberOfSliders = NS
        self.currentSlider = 0
        SV = self.CValue
        for i in range(self.numberOfSliders):
            self.root.ids[self.sIds[self.idNumber][self.currentSlider]].value = SV
            self.root.ids[self.sIds[self.idNumber][self.currentSlider]].max = SV
            self.currentSlider += 1

    def pauseButton(self, screenCode, NS):
        self.currentSlider = 0
        self.idNumber = screenCode
        self.numberOfSliders = NS
        self.pausedIcon = "pausedIcon" + str(self.idNumber)
        if self.paused == True:
            self.paused = False
            # this line of code is temporariliy for elJuS screen pause button only
            self.root.ids[self.pausedIcon].icon = "pause-circle-outline"
            self.action()
        elif self.paused == False:
            self.root.ids[self.pausedIcon].icon = "arrow-right-drop-circle-outline"
            self.paused = True

    def action(self):
        t = Timer(1, self.trial)
        t.start()

    # def openYt(self):
    #     webbrowser.open("https://www.youtube.com/channel/UChWJjQg-w-k_vGMTdiR6nig")

    # def openIg(self):
    #     webbrowser.open("https://www.instagram.com/shybitiwa/")

    def openAbout(self):
        self.root.ids.SM.transition.direction = "left"
        self.root.ids.SM.current = "about"

    def openItch(self):
        pass

    # def openTt(self):
    #     webbrowser.open("https://www.tiktok.com/@shybitiwa/")

    def settings(self):
        self.root.ids.SM.transition.direction = "left"
        self.root.ids.SM.current = "settings"

    def help(self):
        self.root.ids.SM.transition.direction = "left"
        self.root.ids.SM.current = "help"

    def changeMin(self):
        # self.root.ids.myL.text = self.root.ids.minL.text
        self.CValue = self.root.ids.minL.text
        try:
            self.reloadSliders(0, 8, self.CValue)
            self.reloadSliders(1, 11, self.CValue)
            self.reloadSliders(2, 10, self.CValue)
            self.reloadSliders(3, 11, self.CValue)
            self.root.ids.ErrorL.text = "Changed to " + str(self.CValue) + " seconds"
        except:
            self.root.ids.ErrorL.text = "!!!something went wrong!!!\nNOTE: make sure you type NUMBERS only \n and dont leave a blank box"
            self.CValue = 60

    @mainthread
    def trial(self):
        if self.paused == False:
            if self.root.ids[self.sIds[self.idNumber][self.currentSlider]].value > 0:
                self.root.ids[self.sIds[self.idNumber][self.currentSlider]].value -= 1
                self.action()
            # the below code will run if the above slider is zero..so to pass to the next
            elif self.root.ids[self.sIds[self.idNumber][self.currentSlider]].value <= 0:
                if self.numberOfSliders - 1 == self.currentSlider:
                    pass
                else:
                    SMessage = self.sIds[self.idNumber][self.currentSlider][1:]
                    notification.notify(
                        title="ReadNow",
                        message="Congradulation you have finished your "
                        + SMessage
                        + " Session",
                    )
                    self.currentSlider += 1
                    self.action()


class ContentNavigationDrawer(MDBoxLayout):
    pass


MainApp().run()

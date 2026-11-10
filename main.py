from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

try:
    import arabic_reshaper
    from bidi.algorithm import get_display

    def ar(text):
        try:
            return get_display(arabic_reshaper.reshape(text))
        except Exception:
            return text
except Exception:
    def ar(text):
        return text

KV = '''
#:import dp kivy.metrics.dp

<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: 0.055, 0.09, 0.17, 1
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(120)
            padding: dp(18)
            canvas.before:
                Color:
                    rgba: 0.10, 0.20, 0.34, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: app.t("مدرسة سلم النجاح")
                font_size: "26sp"
                bold: True
                color: 0.98, 0.75, 0.30, 1

            Label:
                text: app.t("نظام الإدارة المدرسية")
                font_size: "15sp"
                color: 0.78, 0.85, 0.95, 1

        ScrollView:
            GridLayout:
                cols: 2
                padding: dp(14)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height

                Button:
                    text: app.t("إدارة الطلاب")
                    font_size: "19sp"
                    background_normal: ""
                    background_color: 0.12, 0.31, 0.48, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("إدارة الطلاب")

                Button:
                    text: app.t("الحضور والانصراف")
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.12, 0.38, 0.34, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("الحضور والانصراف")

                Button:
                    text: app.t("الدروس والدرجات")
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.32, 0.25, 0.48, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("الدروس والدرجات")

                Button:
                    text: app.t("الشؤون المالية")
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.42, 0.29, 0.12, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("الشؤون المالية")

                Button:
                    text: app.t("المعلمون والموظفون")
                    font_size: "17sp"
                    background_normal: ""
                    background_color: 0.20, 0.30, 0.45, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("المعلمون والموظفون")

                Button:
                    text: app.t("المساعد الذكي")
                    font_size: "19sp"
                    background_normal: ""
                    background_color: 0.35, 0.20, 0.38, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("المساعد الذكي")

                Button:
                    text: app.t("تقارير الإدارة")
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.12, 0.35, 0.40, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("تقارير الإدارة")

                Button:
                    text: app.t("الإعدادات")
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.27, 0.31, 0.38, 1
                    size_hint_y: None
                    height: dp(110)
                    on_release: app.show_info("الإعدادات")

<InfoScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(18)
        canvas.before:
            Color:
                rgba: 0.055, 0.09, 0.17, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: root.section
            font_size: "25sp"
            bold: True
            color: 1, 0.78, 0.35, 1

        Label:
            text: app.t("هذه الوحدة قيد التطوير والتجهيز")
            font_size: "17sp"
            color: 0.8, 0.85, 0.9, 1

        Button:
            text: app.t("العودة")
            size_hint_y: None
            height: dp(55)
            background_normal: ""
            background_color: 0.12, 0.38, 0.55, 1
            on_release: app.go_home()
'''


class MainScreen(Screen):
    pass


class InfoScreen(Screen):
    section = StringProperty("")


class SuccessLadderApp(App):

    def t(self, text):
        return ar(text)

    def build(self):
        self.title = "مدرسة سلم النجاح"
        Builder.load_string(KV)
        manager = ScreenManager()
        manager.add_widget(MainScreen(name="home"))
        manager.add_widget(InfoScreen(name="info"))
        return manager

    def show_info(self, section):
        screen = self.root.get_screen("info")
        screen.section = ar(section)
        self.root.current = "info"

    def go_home(self):
        self.root.current = "home"


if __name__ == "__main__":
    SuccessLadderApp().run()


import os
import json
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

DATA_FILE = "school_data.json"

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
            height: dp(145)
            padding: dp(18)
            spacing: dp(8)
            canvas.before:
                Color:
                    rgba: 0.10, 0.20, 0.34, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:
                text: "SUCCESS LADDER"
                font_size: "25sp"
                bold: True
                color: 0.98, 0.75, 0.30, 1

            Label:
                text: "مدرسة سُلَّم النجاح"
                font_size: "24sp"
                bold: True
                color: 1, 1, 1, 1

            Label:
                text: "نظام الإدارة المدرسية الذكية"
                font_size: "14sp"
                color: 0.78, 0.85, 0.95, 1

        ScrollView:
            GridLayout:
                cols: 2
                padding: dp(14)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height

                Button:
                    text: "👨‍🎓\\nإدارة الطلاب"
                    font_size: "19sp"
                    background_normal: ""
                    background_color: 0.12, 0.31, 0.48, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("إدارة الطلاب")

                Button:
                    text: "📷\\nالحضور والانصراف"
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.12, 0.38, 0.34, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("الحضور والانصراف")

                Button:
                    text: "📚\\nالدروس والدرجات"
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.32, 0.25, 0.48, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("الدروس والدرجات")

                Button:
                    text: "💰\\nالشؤون المالية"
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.42, 0.29, 0.12, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("الشؤون المالية")

                Button:
                    text: "👩‍🏫\\nالمعلمون والموظفون"
                    font_size: "17sp"
                    background_normal: ""
                    background_color: 0.20, 0.30, 0.45, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("المعلمون والموظفون")

                Button:
                    text: "🤖\\nالمساعد الذكي"
                    font_size: "19sp"
                    background_normal: ""
                    background_color: 0.35, 0.20, 0.38, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("المساعد الذكي")

                Button:
                    text: "📊\\nتقارير الإدارة"
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.12, 0.35, 0.40, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("تقارير الإدارة")

                Button:
                    text: "⚙️\\nالإعدادات"
                    font_size: "18sp"
                    background_normal: ""
                    background_color: 0.27, 0.31, 0.38, 1
                    size_hint_y: None
                    height: dp(125)
                    on_release: app.show_info("الإعدادات")

        Label:
            text: "SUCCESS LADDER © 2026"
            size_hint_y: None
            height: dp(38)
            color: 0.65, 0.72, 0.82, 1
            font_size: "12sp"

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
            text: "مرحباً بك في نظام مدرسة سُلَّم النجاح"
            font_size: "19sp"
            color: 1, 1, 1, 1

        Label:
            text: "هذه الوحدة قيد التطوير والتجهيز."
            font_size: "16sp"
            color: 0.8, 0.85, 0.9, 1

        Button:
            text: "العودة إلى لوحة الإدارة"
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

    def build(self):
        self.title = "مدرسة سُلَّم النجاح"
        Builder.load_string(KV)

        manager = ScreenManager()
        manager.add_widget(MainScreen(name="home"))
        manager.add_widget(InfoScreen(name="info"))
        return manager

    def show_info(self, section):
        screen = self.root.get_screen("info")
        screen.section = section
        self.root.current = "info"

    def go_home(self):
        self.root.current = "home"

if __name__ == "__main__":
    SuccessLadderApp().run()

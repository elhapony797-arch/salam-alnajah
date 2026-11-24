
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

APP_URL = "https://elhapony797-arch.github.io/salam-alnajah/app.html"


class QimmaApp(App):

    def build(self):
        self.title = "قمة"
        self.webview = None

        self.root_layout = BoxLayout(
            orientation="vertical"
        )

        self.message = Label(
            text="جارٍ تشغيل نظام قمة...",
            font_size="20sp",
            color=(1, 0.78, 0.35, 1)
        )

        self.root_layout.add_widget(self.message)

        Window.bind(on_keyboard=self.on_keyboard)

        if platform == "android":
            Clock.schedule_once(self.open_webview, 1)
        else:
            self.message.text = "تطبيق قمة مخصص لنظام Android"

        return self.root_layout

    def open_webview(self, dt):
        try:
            from jnius import autoclass
            from android.runnable import run_on_ui_thread

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            WebView = autoclass(
                "android.webkit.WebView"
            )

            WebViewClient = autoclass(
                "android.webkit.WebViewClient"
            )

            WebChromeClient = autoclass(
                "android.webkit.WebChromeClient"
            )

            FrameLayoutParams = autoclass(
                "android.widget.FrameLayout$LayoutParams"
            )

            ViewGroup = autoclass(
                "android.view.ViewGroup"
            )

            activity = PythonActivity.mActivity

            self.webview = WebView(activity)

            settings = self.webview.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            settings.setLoadsImagesAutomatically(True)
            settings.setJavaScriptCanOpenWindowsAutomatically(True)

            self.webview.setWebViewClient(WebViewClient())
            self.webview.setWebChromeClient(WebChromeClient())

            self.webview.loadUrl(APP_URL)

            content = activity.findViewById(
                autoclass("android.R$id").content
            )

            params = FrameLayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.MATCH_PARENT
            )

            @run_on_ui_thread
            def show_page():
                content.addView(self.webview, params)

            show_page()

        except Exception as error:
            self.message.text = (
                "تعذر تشغيل نظام قمة:\n" + str(error)
            )

    def on_keyboard(self, window, key, *args):
        if key == 27:
            if platform == "android" and self.webview is not None:
                self.go_back()
                return True

        return False

    def go_back(self):
        if self.webview is None:
            self.stop()
            return

        try:
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def navigate_back():
                if self.webview.canGoBack():
                    self.webview.goBack()
                else:
                    self.stop()

            navigate_back()

        except Exception:
            self.stop()


if __name__ == "__main__":
    QimmaApp().run()

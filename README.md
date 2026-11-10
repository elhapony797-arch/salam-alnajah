import traceback

try:
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.clock import Clock
    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    WebView = autoclass("android.webkit.WebView")
    WebViewClient = autoclass("android.webkit.WebViewClient")
    LayoutParams = autoclass("android.view.ViewGroup$LayoutParams")
    activity = autoclass("org.kivy.android.PythonActivity").mActivity

    URL = "https://elhapony797-arch.github.io/salam-alnajah/"

    class Browser:
        webview = None

        @run_on_ui_thread
        def create(self):
            self.webview = WebView(activity)
            s = self.webview.getSettings()
            s.setJavaScriptEnabled(True)
            s.setDomStorageEnabled(True)
            self.webview.setWebViewClient(WebViewClient())
            activity.setContentView(self.webview, LayoutParams(-1, -1))
            self.webview.loadUrl(URL)

    class WebApp(App):
        def build(self):
            Clock.schedule_once(lambda dt: Browser().create(), 0.5)
            return Label(text="...")

    WebApp().run()

except Exception:
    err = traceback.format_exc()
    from kivy.app import App
    from kivy.uix.label import Label

    class ErrApp(App):
        def build(self):
            return Label(text=err, font_size="11sp")

    ErrApp().run()

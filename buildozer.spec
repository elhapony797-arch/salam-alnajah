
[app]

title = Success Ladder - مدرسة سلم النجاح
package.name = successladder
package.domain = org.elhapony
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

android.api = 33
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1

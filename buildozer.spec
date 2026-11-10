
[app]
title = مدرسة سلم النجاح
package.name = successladder
package.domain = org.elhapony

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

version = 1.0.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 23
android.ndk = 25b
android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/icon.png

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1

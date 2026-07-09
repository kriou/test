[app]
title = tvbox
package.name = tk
package.domain = com.github.tvbox.osc.tk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.0.1
# NDK28 对 cython 版本要求更高，更换兼容组合，去掉内置cython避免编译冲突
requirements = python3,kivy,kivymd,libiconv,libffi

entrypoint = main.py

android.accept_sdk_license = True
android.minapi = 21
android.api = 34
# 更换稳定NDK26b，28容易出现工具链下载/编译失败
android.ndk = 26b
android.ndk_api = 21
exclude_patterns = **/test/*, **/tests/*

android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2

p4a.bootstrap = sdl2
android.permissions = INTERNET
android.aab = False

[buildozer]
log_level = 2
warn_on_root = 1

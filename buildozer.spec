#应用中文名称可直接填写
title = tvboxtk
package.name = tvbox
#release模式禁止org.test，替换为自定义反向域名
package.domain = com.github.tvbox.osc.tk
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
#如需打包图片文件夹取消注释
#source.include_patterns = image/*
version = 0.0.1
#锁定cython0.29.33规避long整型报错
requirements = python3,kivy,kivymd,libiconv,libffi,cython==0.29.33

#图标与启动页（有文件再取消注释）
#icon.filename = icon.png
#presplash.filename = presplash.png
#fullscreen = 0
#orientation = portrait
entrypoint = main.py

#Android SDK编译基础配置
android.accept_sdk_license = True
android.minapi = 21
android.api = 34
android.ndk = 28
android.ndk_api = 21
exclude_patterns = **/test/*, **/tests/*

#Gradle版本锁定
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2

#渲染后端
p4a.bootstrap = sdl2

#网络权限
android.permissions = INTERNET

# 关闭自动生成AAB，打包命令配合 --no-aab 输出纯APK
android.aab = False

# 签名全部注释，由Github Actions环境变量控制，不要写死路径密码
#android.keystore = xxx.keystore
#android.keystore_storepass = android
#android.keystore_keypass = android
#android.keystore_alias = DomainName.PackageName

[buildozer]
log_level = 2
warn_on_root = 1

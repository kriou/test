[app]
title = TestApp
package.name = testapp
package.domain = com.test
version = 1.0

source.dir = .
# 打包第三方文件夹
source.include_dirs = third_lib
source.include_exts = py,png,jpg,kv,json,txt
source.exclude_dirs = .github,.git

requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET

android.api = 24
android.ndk = 25b
# 锁定稳定构建工具
android.build_tools = "34.0.0"
# CI自动同意所有SDK许可证（核心！消除交互弹窗）
android.accept_sdk_license = True
android.jdk_version = 17

[app]
title = PythonApp
package.name = myapp
package.domain = org.myapp
version = 1.0

source.dir = .
source.include_dirs = third_lib
source.include_exts = py,png,jpg,kv,json,txt
source.exclude_dirs = .github,.git

requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET, READ_MEDIA_IMAGES

# 消除低API商店警告
android.api = 33
# 官方稳定NDK，消除NDK版本警告
android.ndk = 28c
# 稳定构建工具，避开37许可坑
android.build_tools = "34.0.0"
# CI自动同意SDK许可，根治build-tools文件夹找不到
android.accept_sdk_license = True
android.jdk_version = 17

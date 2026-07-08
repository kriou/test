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
android.permissions = INTERNET

# 升级API消除商店警告
android.api = 33
android.ndk = 26b
android.build_tools = "34.0.0"
android.accept_sdk_license = True
android.jdk_version = 17

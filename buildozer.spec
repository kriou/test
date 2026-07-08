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

android.api = 24
android.ndk = 25b
android.build_tools = "34.0.0"
android.accept_sdk_license = True
android.jdk_version = 17

- name: Clone Box repository
  run: |
    rm -rf ./*
    git clone -b ${{ env.TARGET_BRANCH }} ${{ env.TARGET_REPO }} ./
    ls -la

# 新增生成完整spec
- name: Generate complete buildozer.spec
  run: |
    cat > buildozer.spec <<'END_SPEC'
[app]
title = Box工具
package.name = boxapp
package.domain = com.box.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.0.1
requirements = python3,kivy,kivymd,libiconv,libffi,cython==0.29.33
entrypoint = main.py

android.accept_sdk_license = True
android.minapi = 21
android.api = 33
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
END_SPEC
    cat buildozer.spec

# 下面是缓存、Java、Python、系统依赖步骤不变

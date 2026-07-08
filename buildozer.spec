[app]
title = 整合第三方代码
package.name = myapp
package.domain = com.demo
version = 1.0

# 源码根目录为项目根目录
source.dir = .
# 强制打包 third_lib 整个文件夹
source.include_dirs = third_lib
# 需要打包的文件后缀
source.include_exts = py,png,jpg,kv,json,txt

# 排除不需要的目录（可选）
source.exclude_dirs = .github,.git,tests

# 基础依赖，不写远程git依赖
requirements = python3,kivy

orientation = portrait
android.permissions = INTERNET
android.api = 24
android.ndk = 25b
android.jdk_version = 17

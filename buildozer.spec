[app]
title = 整合第三方项目
package.name = myapp
package.domain = com.demo
version = 1.0

# 源码根目录
source.dir = .
# 打包包含第三方代码文件夹 third_code
source.include_dirs = third_code
# 需要打包的文件后缀
source.include_exts = py,png,jpg,kv,json,txt

# 只写基础运行依赖，不写git远程仓库依赖
requirements = python3,kivy

orientation = portrait
android.permissions = INTERNET
android.api = 24
android.ndk = 25b
android.jdk_version = 17

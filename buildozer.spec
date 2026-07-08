
[app]
# ====================== 基础应用信息（必填） ======================
# 手机桌面显示的APP名称
title = 我的Python程序

# 应用短包名：只能小写英文、数字，不能有空格/中文，唯一标识
package.name = pythonapp

# 应用域名标识（反向域名，随便写，格式：org.xxx / com.xxx）
package.domain = org.demo

# APP版本号，自己修改
version = 1.0

# ====================== 源码相关 ======================
# 程序代码所在目录，代码放根目录就写 .
source.dir = .

# 包含第三方文件夹代码
source.include_dirs = third_app
source.include_exts = py,png,kv

# 需要打包进安装包的文件后缀
source.include_exts = py,png,jpg,jpeg,gif,kv,ttf,json,txt

# 不需要打包的文件夹（可选）
source.exclude_dirs = tests, .github, .git

# ====================== Python依赖（重点） ======================
# 运行需要的库，多个用逗号隔开
# 基础图形必须带 python3,kivy
requirements = python3,kivy

# 举例：用到其他库就追加，例如：
# requirements = python3,kivy,requests,pillow

# ====================== 界面与屏幕设置 ======================
# portrait 竖屏；landscape 横屏；all 自动旋转
orientation = portrait

# 应用全屏 1=全屏，0=不全屏
fullscreen = 0

# ====================== Android 权限（按需开启） ======================
# 多个权限逗号分隔，不需要就删掉对应项
# INTERNET 网络读写；WRITE_EXTERNAL_STORAGE 读写文件
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# ====================== Android SDK/编译配置（不用改） ======================
# 指定Android最低兼容版本
android.api = 24
# 编译SDK版本
android.ndk = 25b
android.sdk = 24

# JDK版本，和Actions里的java17对应，不用修改
android.jdk_version = 17

# ====================== 图标/启动图（可选） ======================
# 图标路径，图片放项目根目录
# icon.filename = icon.png
# 启动页图片
# presplash.filename = splash.png

# ====================== 打包优化 ======================
# 是否开启代码混淆，debug包建议关闭
android.minify = False

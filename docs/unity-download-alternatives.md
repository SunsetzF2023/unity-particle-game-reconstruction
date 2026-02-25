# Unity Hub 下载替代方案

## 🌏 问题说明
Unity官网会根据IP地址自动跳转到中国区的"团结引擎"，这是Unity在中国的特殊版本。

## 🔧 解决方案

### 方案1: 直接下载链接 (推荐)
**Unity Hub官方下载地址**:
```
https://download.unity3d.com/download_unity/UnityHubSetup.exe
```

### 方案2: 浏览器设置
1. **Chrome/Edge**: 设置语言为英语
2. **使用VPN**: 连接到美国/欧洲节点
3. **无痕模式**: 可能避免跳转

### 方案3: 备用下载源
如果官方链接失效，可以尝试：
```
https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.exe
```

### 方案4: 团结引擎 (备选)
如果只能下载团结引擎，也可以使用：
- 团结引擎与Unity基本兼容
- 支持相同的Unity版本
- 可以正常开发我们的项目

## 📦 下载步骤

### 推荐步骤:
1. 点击直接下载链接: https://download.unity3d.com/download_unity/UnityHubSetup.exe
2. 下载完成后运行安装程序
3. 安装完成后启动Unity Hub

### 如果跳转仍然发生:
1. 复制上面的直接链接
2. 在新浏览器窗口中粘贴
3. 或者尝试无痕模式

## 🎯 安装Unity编辑器

安装Unity Hub后，在Unity Hub中安装Unity 2021.3.21f1:

1. 启动Unity Hub
2. 点击左侧 "Installs"
3. 点击 "Add"
4. 搜索 "2021.3.21f1"
5. 选择并安装

## ⚠️ 注意事项

- 团结引擎版本可能略有不同，但基本功能相同
- 如果使用团结引擎，界面可能显示中文
- Unity 2021.3.21f1 LTS版本在团结引擎中也可用

## 🔄 验证下载

下载完成后运行检查工具:
```bash
cd unity-particle-game-reconstruction\tools
python unity-setup-check.py
```

---

**建议**: 先尝试直接下载链接，如果不行再考虑其他方案。

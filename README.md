# Door2Gate - 赶飞机计算器

一个 PWA（渐进式 Web 应用）工具，帮助计算赶飞机的时间安排。

## PWA 图标生成

项目已配置 PWA 支持，需要生成图标文件：

### 方法 1：使用生成工具（推荐）

1. 在浏览器中打开 `generate-icons.html`
2. 点击"生成所有图标"按钮
3. 分别下载 `icon-192.png` 和 `icon-512.png`
4. 将文件放到项目根目录

### 方法 2：使用在线工具

1. 访问 https://realfavicongenerator.net/
2. 上传 `icon.svg` 文件
3. 下载生成的图标文件
4. 重命名为 `icon-192.png` 和 `icon-512.png`

### 方法 3：使用 Python 脚本

```bash
# 安装依赖（需要先安装 cairo 系统库）
brew install cairo  # macOS
pip install cairosvg pillow

# 生成图标
python3 generate-icons.py
```

## 文件说明

- `index.html` - 主应用文件
- `manifest.json` - PWA 配置文件
- `icon.svg` - SVG 图标源文件
- `icon-192.png` - 192x192 图标（需要生成）
- `icon-512.png` - 512x512 图标（需要生成）

## 部署

部署到 GitHub Pages 后，确保所有文件都在根目录，PWA 功能即可正常工作。


#!/usr/bin/env python3
"""
生成 PWA 所需的 PNG 图标文件
需要安装: pip install cairosvg pillow
"""

try:
    import cairosvg
    from PIL import Image
    import io
    import os
    
    # SVG 文件路径
    svg_path = 'icon.svg'
    
    # 需要生成的尺寸
    sizes = [192, 512]
    
    if not os.path.exists(svg_path):
        print(f"错误: 找不到 {svg_path} 文件")
        exit(1)
    
    # 读取 SVG 文件
    with open(svg_path, 'rb') as f:
        svg_data = f.read()
    
    # 生成不同尺寸的 PNG
    for size in sizes:
        output_path = f'icon-{size}.png'
        
        # 使用 cairosvg 将 SVG 转换为 PNG
        png_data = cairosvg.svg2png(bytestring=svg_data, output_width=size, output_height=size)
        
        # 保存 PNG 文件
        with open(output_path, 'wb') as f:
            f.write(png_data)
        
        print(f"✓ 已生成 {output_path} ({size}x{size})")
    
    print("\n所有图标已生成完成！")
    
except ImportError:
    print("错误: 需要安装依赖库")
    print("请运行: pip install cairosvg pillow")
    print("\n或者使用在线工具生成图标:")
    print("1. 访问 https://realfavicongenerator.net/")
    print("2. 上传 icon.svg 文件")
    print("3. 下载生成的图标文件")
    print("4. 将 icon-192.png 和 icon-512.png 放到项目根目录")
except Exception as e:
    print(f"生成图标时出错: {e}")
    print("\n备选方案: 使用在线工具生成图标")
    print("1. 访问 https://realfavicongenerator.net/")
    print("2. 上传 icon.svg 文件")
    print("3. 下载生成的图标文件")


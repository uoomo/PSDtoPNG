# PSDtoPNG

一个简单的工具，通过右键菜单将PSD文件转换为PNG格式（仅限Windows）。

## 功能
- 右键PSD文件，选择“PSDtoPNG”，自动生成同名PNG文件。

## 安装
1. 克隆仓库：
   ```bash
   git clone https://github.com/uoomo/PSDtoPNG.git

2. 安装依赖：
   ```bash
   pip install -r requirements.txt

3. 注册右键菜单（以管理员身份运行）
   ```bash
   python register_context_menu.py

## 卸载
移除右键菜单：
```bash
python register_context_menu.py uninstall

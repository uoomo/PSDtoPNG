import sys
import os
from psd_tools import PSDImage

def convert_psd_to_png(psd_path):
    try:
        psd = PSDImage.open(psd_path)
        base_name = os.path.splitext(psd_path)[0]
        output_path = f"{base_name}.png"
        psd.composite().save(output_path, format='PNG')
        print(f"转换成功: {output_path}")
    except Exception as e:
        print(f"转换失败: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供PSD文件路径")
        sys.exit(1)
    psd_file = sys.argv[1]
    if not os.path.exists(psd_file):
        print(f"文件不存在: {psd_file}")
        sys.exit(1)
    convert_psd_to_png(psd_file)

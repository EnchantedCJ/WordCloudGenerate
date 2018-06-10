# 词云生成小程序

Describe: Generate word cloud.  
Version: 0.1.0  
Last update: 2018.6.10  
Author: CJ

## 使用

1. 运行WordCloudGenerate.py，需要python及wordcloud和matplotlib库
2. 运行WordCloudGenerate.exe

## 文件说明

### Config  

	配置文件路径  
	- font_path: str, 字体路径
	- background_color: str, 背景颜色
	- prefer_horizontal: float, 水平文字频率
	- colormap: str, 配色(https://matplotlib.org/examples/color/colormaps_reference.html)
	- width: int, 图片宽度
	- height: int, 图片高度
	- relative_scaling: float, 取0按顺序线性变化大小，取1大小离散最大

### Input

	输入文件路径
	- FileNameList: 文件名（不含扩展名）
	- 文件1
	- 文件2
	- 文件n

### Output

	词云生成路径
  

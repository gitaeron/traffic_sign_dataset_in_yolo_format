# License

本项目所有内容均为本人 拍摄, 清洗与脱敏化处理, 标注; 

若其中部分内容(比如某张图片)侵犯了您的合法权益, 请联系我删除, 联系方式在文末.

本项目仅供学习使用, `不能作为商业化应用`, `坚决抵制某些人打包后二次贩售发布`! 

## 尤其禁止在 `csdn.net` 等相关平台 `付费发布` 本项目!

如有遇见上述情况, 请至相关平台与该二次贩售的内容发布平台举报, `请不要掏钱给这些黑商`, 谢谢合作.

> 本项目为本人所有, 使用 [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/) 授权. 
>
> 禁止商用! 禁止商用! 禁止商用!
> 
> 具体详见 License.md

---

# 关于本项目

本项目为 `交通道路路标(只准直行, 左转, 右转)` 的数据集, 使用 Yolo 通用格式制作.

- `straight_only` - 直行交通标志数据集  
    - train - 3366
    - val - 841

- `turn_left` - 左转交通标志数据集
    - train - 2000
    - val - 500

- `turn_right` - 右转交通标志数据集
    - train - 2000
    - val - 500

- `mix` - 一图多类别
    - train - 2406
    - val - 601

- `code` - 数据集处理相关代码

在 `straight_only`, `turn_left`, `turn_right` 文件夹中, 一张图片仅包含当前文件夹所代表的分类, 即 `straight_only` 中的数据集, 在一张图片中仅包含有 `straight_only traffic sign` 与它的标注, 并且不会出现其他分类.

在 `mix` 文件夹中, 一张图片内会出现 两个/多个 交通标志物(straight_only, turn_left, turn_right).

具体请打开 straight_only/images, mix/images 查看区别.

---

## 数据集目录结构

本数据集的文件夹目录结构如下:

- straight_only
    - images
        - train
        - val
    - labels
        - train
        - val
    - classes.txt

其中, `straight_only`, `turn_left`, `turn_right`这三个文件夹目录结构相同.

---

## 类别

classes有三个类:

- straight_only
- turn_left
- turn_right

---

## dataset.yaml

基础内容已包含在其中, 若要直接使用, 请修改 `path` 内容为您项目的 相对路径 或 绝对路径.

> 根据 yolov8 的官方教程, 您可以将该文件放置在任意位置, 只需在 CLI 或 Python 程序中指定 data=dataset.yaml 即可.

---

## code

该文件夹中为本人在处理数据集时所写下的代码, 目前提供了两个文件, 分别为

- random_dataset.py
    - 该程序为 以 80% / 20% 的比例分割数据集图片

- rename.py
    - 该程序为 以固定格式重命名 image & label 文件


不论哪一个文件, 请在确保理解的基础上修改后才能使用它.

---

# Contact

Aeron Atlantis - @Aeron.Atlantis@gmail.com -　[gitaeron.github.io](https://gitaeron.gtihub.io)

Project Link: https://github.com/gitaeron/gitaeron.github.io





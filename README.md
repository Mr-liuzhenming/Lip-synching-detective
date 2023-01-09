# Lip synching detective

> 注意：该工具包尚未完成

## 1.工具包简介
**Lip synching detective** 是由Python语言开发的、一个可视化的、有GUI界面的声音分析工具包，主要用于判断歌曲是否是假唱。

## 2. 工具包功能
Lip synching detective具有以下功能：

上传歌曲文件和MIDI乐谱文件
对歌曲文件进行声音分析
对MIDI乐谱进行解析
判断歌曲是否是假唱

## 3. 工具包界面
Lip synching detective的界面如下图所示：

Lip synching detective界面

界面包括以下部分：

 1. 标题栏
 2. 菜单栏
 3. 上传文件区域
 4. 分析结果显示区域
 5. 状态栏
## 4. 工具包工作流程
Lip synching detective的工作流程如下图所示：

![在这里插入图片描述](https://img-blog.csdnimg.cn/4c0b3d8e4dd941408638d9ecee9fd9ae.png)

## 5. 工具包实现
Lip synching detective的实现包括以下几个部分：

 - 上传文件功能：

Lip synching detective通过GUI界面提供的文件上传按钮，允许用户上传歌曲文件和MIDI乐谱文件。

 - MIDI文件解析功能：

Lip synching detective使用MIDI解析库解析MIDI乐谱文件，并提取出每个音符的频率和时间信息。

 - 歌曲声音分析功能：

Lip synching detective使用声音分析库分析歌曲文件，并提取出每个时间点的频率信息。

 - 歌曲假唱判断功能：

Lip synching detective通过比较歌曲文件中人声部分的频率信息和MIDI乐谱中的音符频率信息，判断歌曲是否是假唱。

## 6. 工具包文件结构
Lip synching detective的文件结构如下：

```
Lip-synching-detective/
├── main.py
├── upload_files.py
├── parse_midi.py
├── analyze_song.py
├── compare.py
├── GUI.py
├── README.md
```
## 7. 工具包使用说明
使用Lip synching detective的说明如下：

 1. 安装依赖：Lip synching detective需要MIDI解析库、声音分析库和GUI库的支持。请确保已安装这些库。

 2. 在Github中把代码下载到本地。

 3. 运行Lip synching detective：在终端中进入Lip synching detective的根目录，输入以下命令运行Lip synching detective：

```python
python main.py
```

 4. 上传文件：在GUI界面中点击“上传歌曲文件”和“上传MIDI乐谱文件”按钮，选择需要分析的歌曲文件和MIDI乐谱文件。

 5. 开始分析：点击“开始分析”按钮，Lip synching detective开始分析歌曲文件和MIDI乐谱文件。

 6. 查看结果：在GUI界面的“分析结果”区域中查看分析结果。如果分析结果为“假唱”，则表示歌曲中存在假唱；如果分析结果为“真唱”，则表示歌曲中没有假唱。

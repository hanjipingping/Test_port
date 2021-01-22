'''
// ：从根节点下面开始，查找子孙节点
* ：通配符，表示任意字符
. :表示当前路径
.. :表示父级
@ ：获取属性
@id：
[] :筛选条件
通过a标签
//a[@href = '']
通过文本内容
//a[@text = '']

查找的函数：
contains：部分匹配函数(包含)
//a[contains(@title,'bai')]   部分匹配bai
//a[contains(text(),'bai')]
//*[contains(text(),'音')]
starts-with：匹配是否是xxx开头（包含）
//*[starts-with(text(),'音')]


复杂的定位表达式：
    通过子元素的文本内容，去定位父级元素


'''
loggging

- 记录器（Logger）：提供应用程序代码直接使用的接口。
- 处理器（Handler）：将日志记录（由记录器创建）发送到适当的目的地。
- 筛选器（Filter）：提供了更细粒度的功能，用于确定要输出的日志记录。
- 格式器（Formatter）：程序在最终输出日志记录的内容格式。

logging的工作流程：以记录器Logger为对象，设置合适的处理器Handler，辅助以筛选器Filter、格式器Formatter，设置日志级别以及常用的方法，最终输出理想的日志记录给到指定目标

一个Logger可以包含多个Handler；
每个Handler可以设置自己的Filter和Formatter；

**LogRecord的属性**

![img](https://img-blog.csdnimg.cn/20200521174847446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NzE1NDkwOQ==,size_16,color_FFFFFF,t_70)

logger是暴露给代码进行日志操作的接口。需要注意的是，logger不应该直接实例化，而应通过模块级函数logging.getLogger(name)创建。如果name是具有层级结构的命名方式，则logger之间也会有层级关系。如name为foo.bar，foo.bar.baz， foo.bam 的logger是foo的子孙，默认子logger日志会向父logger传播，可以通过logger.propagate=False禁止；对具有相同名称的getLogger()的多次调用将始终返回同一Logger对象的引用。logger对象的功能包括以下三项：

向应用程序暴露info、debug等方法，用于程序运行时进行日志记录；
根据log level（默认过滤工具）或Filter对象确定要处理的日志消息；
将日志消息传递给所有感兴趣的Log Handler;


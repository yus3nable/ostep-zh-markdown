# 参考资料

[A+02]“Cooperative Task Management Without Manual Stack Management”Atul Adya, Jon Howell, Marvin Theimer, William J. Bolosky, John R. Douceur USENIX ATC ’02, Monterey, CA, June 2002这篇论文首次明确阐述了基于事件的并发的一些困难，并提出了一些简单的解决方案，同时也探讨了将两种并发管理整合到单个应用程序中的更疯狂的想法！

[FHK84]“Programming With Continuations”Daniel P. Friedman, Christopher T. Haynes, Eugene E. Kohlbecker In Program Transformation and Programming Environments, Springer Verlag, 1984这是来自编程语言世界的这个老思想的经典参考。现在在一些现代语言中越来越流行。

[N13]“Node.js Documentation”By the folks who build node.js许多很酷的新框架之一，可帮助你轻松构建Web 服务和应用程序。每个现代系统黑客都应该精通这样的框架（可能还有多个框架）。花时间在这些世界中的一个进行开发，并成为专家。

[O96]“Why Threads Are A Bad Idea (for most purposes)”John Ousterhout Invited Talk at USENIX ’96, San Diego, CA, January 1996关于线程如何与基于GUI 的应用程序不太匹配的一次很好的演讲（但是这些想法更通用）。Ousterhout 在开发Tcl/Tk 时，形成了这些观点中的大部分，Tcl/Tk 是一种很酷的脚本语言和工具包，与当时最先进的技术相比，开发基于GUI 的应用程序要容易100 倍。虽然Tk GUI 工具箱继续存在（例如在Python 中），但Tcl似乎正在慢慢死去（很遗憾）。

[PDZ99]“Flash: An Efficient and Portable Web Server”Vivek S. Pai, Peter Druschel, Willy Zwaenepoel USENIX ’99, Monterey, CA, June 1999关于如何在当今新兴的互联网时代构建Web 服务器的开创性论文。阅读它以了解基础知识，并了解作者在缺乏对异步I/O 支持时如何构建混合体系的想法。

[SR05]“Advanced Programming in the UNIX Environment”W. Richard Stevens and Stephen A. Rago Addison-Wesley, 2005 UNIX 系统编程的经典必备图书。如果你需要知道一些细节，就在这里。

[vB+03]“Capriccio: Scalable Threads for Internet Services”Rob von Behren, Jeremy Condit, Feng Zhou, George C. Necula, Eric Brewer SOSP ’03, Lake George, New York,October 2003一篇关于如何使线程在极端规模下工作的论文，这是当时正在进行的所有基于事件的工作的反驳。

[WCB01]“SEDA: An Architecture for Well-Conditioned, Scalable Internet Services”Matt Welsh, David Culler,and Eric Brewer SOSP ’01, Banff, Canada, October 2001基于事件的服务的一个不错的变通，它将线程、队列和基于事件的处理合并为一个简化的整体。其中一些想法已经进入谷歌、亚马逊等公司的基础设施。

# 参考资料

[K84]“Processes as Files”Tom J. Killian USENIX, June 1984介绍/proc 文件系统的文章，其中每个进程都可以被视为伪文件系统中的文件。这是一个聪明的想法，你仍然可以在现代UNIX 系统中看到。

[L84]“Capability-Based Computer Systems”Henry M. Levy Digital Press, 1984早期基于权限的系统的完美概述。

[P+13]“Towards Efficient, Portable Application-Level Consistency”Thanumalayan S. Pillai, Vijay Chidambaram, Joo-Young Hwang, Andrea C. Arpaci-Dusseau, and Remzi H.Arpaci-Dusseau HotDep ’13, November 2013我们自己的研究工作，表明了应用程序在将数据提交到磁盘时可能会有多少错误。特别是关于文件系统假设“溜”到应用程序中，从而导致应用程序只有在特定文件系统上运行时才能正常工作。

[SK09]“Principles of Computer System Design”Jerome H. Saltzer and M. Frans Kaashoek Morgan-Kaufmann,2009对于任何对该领域感兴趣的人来说，这是系统的代表作，是必读的。这是作者在麻省理工学院教授系统的方式。希望你阅读一遍，然后再读几遍，直至完全理解。

[SR05]“Advanced Programming in the UNIX Environment”W. Richard Stevens and Stephen A. Rago Addison-Wesley, 2005我们可能引用了这本书几十万次。如果你想成为一个出色的系统程序员，这本书对你很有用。

# 参考资料

[A+11]“vIC: Interrupt Coalescing for Virtual Machine Storage Device IO”Irfan Ahmad, Ajay Gulati, Ali Mashtizadeh USENIX ’11对传统和虚拟化环境中的中断合并进行了极好的调查。

[C01]“An Empirical Study of Operating System Errors”Andy Chou, Junfeng Yang, Benjamin Chelf, Seth Hallem, Dawson Engler SOSP ’01首批系统地研究现代操作系统中有多少错误的文章之一。除了其他漂亮的研究结果之外，作者展示了设备驱动程序的bug 数是主线内核代码中的bug 数的7 倍。

[CK+08]“The xv6 Operating System”Russ Cox, Frans Kaashoek, Robert Morris, Nickolai Zeldovich.请参阅ide.c 中的IDE 设备驱动程序，其中有更多细节。

[D07]“What Every Programmer Should Know About Memory”Ulrich Drepper November, 2007关于现代内存系统的极好的阅读材料，从DRAM 开始，一直到虚拟化和缓存优化算法。

[G08]“EIO: Error-handling is Occasionally Correct”Haryadi Gunawi, Cindy Rubio-Gonzalez, Andrea Arpaci-Dusseau, Remzi Arpaci-Dusseau, Ben Liblit FAST ’08, San Jose, CA, February 2008我们自己的工作，构建一个工具来查找Linux 文件系统中没有正确处理错误返回的代码。我们发现了成百上千个错误，其中很多错误现在已经修复。

[L94]“AT Attachment Interface for Disk Drives”Lawrence J. Lamers, X3T10 Technical Editor Reference number: ANSI X3.221 - 1994关于设备接口的相当枯燥的文档。你可以尝试读一下。

[MR96]“Eliminating Receive Livelock in an Interrupt-driven Kernel”Jeffrey Mogul and K. K. Ramakrishnan USENIX ’96, San Diego, CA, January 1996 Mogul 和同事在Web 服务器网络性能方面做了大量的开创性工作。这篇论文只是其中之一。

[S08]“Interrupts”Mark Smotherman, as of July ’08关于中断历史、DMA 以及早期相关计算思想的宝库。

[S03]“Improving the Reliability of Commodity Operating Systems”Michael M. Swift, Brian N. Bershad, and Henry M. Levy SOSP ’03 Swift 的工作重新燃起了对操作系统更像微内核方法的兴趣。至少，它终于给出了一些很好的理由，说明基于地址空间的保护在现代操作系统中可能有用。

[W10]“Hard Disk Driver”Washington State Course Homepage很好地总结了一个简单的IDE 磁盘驱动器接口，介绍了如何为它建立一个设备驱动程序。

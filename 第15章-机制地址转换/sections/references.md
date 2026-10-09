# 参考资料

[M65]“On Dynamic Program Relocation”W.C. McGee IBM Systems Journal Volume 4, Number 3, 1965, pages 184–199本文对动态重定位的早期工作和静态重定位的一些基础知识进行了很好的总结。

[P90]“Relocating loader for MS-DOS .EXE executable files”Kenneth D. A. Pillay Microprocessors &amp; Microsystems archive Volume 14, Issue 7 (September 1990)MS-DOS 重定位加载器的示例。不是第一个，而只是这样的系统如何工作的一个相对现代的例子。

[SS74]“The Protection of Information in Computer Systems”J. Saltzer and M. Schroeder CACM, July 1974摘自这篇论文：“在1957 年至1959 年间，在3 个有不同目标的项目中，显然独立出现了基址和界限寄存器和硬件解释描述符的概念。在MIT，McCarthy 建议将基址和界限的想法作为内存保护系统的一部分，以便让时分共享可行。IBM 独立开发了基本和界限寄存器，作为Stretch（7030）计算机系统支持可靠多道程序的机制。在Burroughs，R. Barton 建议硬件解释描述符可以直接支持B5000 计算机系统中高级语言的命名范围规则。”我们在Mark Smotherman 的超酷历史页面上找到了这段引用[S04]，更多信息请参见这些页面。

[S04]“System Call Support”Mark Smotherman, May 2004系统调用支持的简洁历史。Smotherman 还收集了一些早期历史，包括中断和其他有趣方面的计算历史。可以查看他的网页了解更多详情。

[WL+93]“Efficient Software-based Fault Isolation”Robert Wahbe, Steven Lucco, Thomas E. Anderson, Susan L. Graham SOSP ’93关于如何在没有硬件支持的情况下，利用编译器支持限定从程序中引用内存的一篇极好的论文。该论文引发了人们对用于分离内存引用的软件技术的兴趣。

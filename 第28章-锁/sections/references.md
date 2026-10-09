# 参考资料

[D91]“Just Win, Baby: Al Davis and His Raiders”Glenn Dickey, Harcourt 1991一本关于Al Davis 和他的名言“Just Win”的书。

[D+13]“Everything You Always Wanted to Know about Synchronization but Were Afraid to Ask”Tudor David, Rachid Guerraoui, Vasileios Trigonakis SOSP ’13, Nemacolin Woodlands Resort, Pennsylvania, November 2013一篇优秀的文章，比较了使用硬件原语构建锁的许多不同方法。很好的读物，看看多年来有多少想法在现代硬件上工作。

[D68]“Cooperating sequential processes”Edsger W. Dijkstra, 1968该领域早期的开创性论文之一，主要讨论Dijkstra 如何提出最初的并发问题以及Dekker 的解决方案。

[H93]“MIPS R4000 Microprocessor User’s Manual”Joe Heinrich, Prentice-Hall, June 1993

[H91]“Wait-free Synchronization”Maurice Herlihy ACM Transactions on Programming Languages and Systems (TOPLAS) Volume 13, Issue 1, January 1991一篇具有里程碑意义的文章，介绍了构建并发数据结构的不同方法。但是，由于涉及的复杂性，许多这些想法在部署系统中获得接受的速度很慢。

[L81]“Observations on the Development of an Operating System”Hugh Lauer SOSP ’81, Pacific Grove, California, December 1981关于Pilot 操作系统（早期PC 操作系统）开发的必读回顾，有趣且充满洞见。

[L09]“glibc 2.9 (include Linux pthreads implementation)”特别是，看看nptl 子目录，你可以在这里找到Linux 中大部分的pthread 支持。

[M82]“The Architecture of the Burroughs B5000 20 Years Later and Still Ahead of the Times?”Alastair J.W.Mayer, 1982摘自该论文：“一个特别有用的指令是RDLK（读锁）。这是一个不可分割的操作，可以读取和写入内存位置。”因此RDLK 是一个早期的测试并设置原语，如果不是最早的话。这里值得称赞的是一位名叫Dave Dahm的工程师，他显然为Burroughs 系统发明了许多这样的东西，包括一种自旋锁（称为“Buzz Locks”）以及一个名为“Dahm Locks”的两阶段锁。

[MS91]“Algorithms for Scalable Synchronization on Shared-Memory Multiprocessors”John M. Mellor-Crummey and M. L. Scott ACM TOCS, Volume 9, Issue 1, February 1991针对不同锁算法的优秀而全面的调查。但是，没有使用操作系统支持，只有精心设计的硬件指令。

[P81]“Myths About the Mutual Exclusion Problem”G. L. Peterson Information Processing Letters, 12(3), pages 115–116, 1981这里介绍了Peterson 的算法。

[S05]“Guide to porting from Solaris to Linux on x86”Ajay Sood, April 29, 2005

[S09]“OpenSolaris Thread Library”这看起来很有趣，但是谁知道Oracle 现在拥有的Sun 将会发生什么。感谢Mike Swift 推荐的代码。

[W09]“Load-Link, Store-Conditional”Wikipedia entry on said topic, as of October 22, 2009你能相信我们引用了维基百科吗？很懒，不是吗？但是，我们首先在那里找到了这些信息，感觉不对而没有引用它。而且，这里甚至列出了不同架构的指令：ldl l/stl c 和ldq l/stq c（Alpha），lwarx/stwcx（PowerPC），ll/sc（MIPS）和ldrex/strex（ARM 版本 6 及以上）。实际上维基百科很神奇，所以不要那么苛刻，好吗？

[WG00]“The SPARC Architecture Manual: Version 9”David L. Weaver and Tom Germond, September 2000 SPARC International, San Jose, California有关Sparc 原子操作的更多详细信息请参阅相关网站。

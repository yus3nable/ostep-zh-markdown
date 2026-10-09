# 参考资料

[A90]“The Performance of Spin Lock Alternatives for Shared-Memory Multiprocessors”Thomas E. Anderson IEEE TPDS Volume 1:1, January 1990这是一篇关于不同加锁方案扩展性好坏的经典论文。Tom Anderson 是非常著名的系统和网络研究者，也是一本非常好的操作系统教科书的作者。

[B+10]“An Analysis of Linux Scalability to Many Cores Abstract”Silas Boyd-Wickizer, Austin T. Clements, Yandong Mao, Aleksey Pesterev, M. Frans Kaashoek, Robert Morris,Nickolai Zeldovich OSDI ’10, Vancouver, Canada, October 2010关于将Linux 扩展到多核的很好的现代论文。

[CSG99]“Parallel Computer Architecture: A Hardware/Software Approach”David E. Culler, Jaswinder Pal Singh,and Anoop Gupta Morgan Kaufmann, 1999其中充满了并行机器和算法细节的宝藏。正如Mark Hill 幽默地在书的护封上说的——这本书所包含的信息比大多数研究论文都多。

[FLR98]“The Implementation of the Cilk-5 Multithreaded Language”Matteo Frigo, Charles E. Leiserson, Keith Randall PLDI ’98, Montreal, Canada, June 1998 Cilk 是用于编写并行程序的轻量级语言和运行库，并且是工作窃取范式的极好例子。

[G83]“Using Cache Memory To Reduce Processor-Memory Traffic”James R. Goodman ISCA ’83, Stockholm, Sweden, June 1983关于如何使用总线监听，即关注总线上看到的请求，构建高速缓存一致性协议的开创性论文。Goodman 在威斯康星的多年研究工作充满了智慧，这只是一个例子。

[M11]“Towards Transparent CPU Scheduling”Joseph T. Meehean Doctoral Dissertation at University of Wisconsin—Madison, 2011一篇涵盖了现代Linux 多处理器调度如何工作的许多细节的论文。非常棒！但是，作为Joe 的联合导师，我们可能在这里有点偏心。

[SHW11]“A Primer on Memory Consistency and Cache Coherence”Daniel J. Sorin, Mark D. Hill, and David A.Wood Synthesis Lectures in Computer Architecture Morgan and Claypool Publishers, May 2011内存一致性和多处理器缓存的权威概述。对于喜欢对该主题深入了解的人来说，这是必读物。

[SA96]“Earliest Eligible Virtual Deadline First: A Flexible and Accurate Mechanism for Pro- portional Share Resource Allocation”Ion Stoica and Hussein Abdel-Wahab Technical Report TR-95-22, Old Dominion University, 1996来自Ion Stoica 的一份技术报告，其中介绍了很酷的调度思想。他现在是U.C.伯克利大学的教授，也是网络、分布式系统和其他许多方面的世界级专家。

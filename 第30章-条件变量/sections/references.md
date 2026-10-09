# 参考资料

[D72]“Information Streams Sharing a Finite Buffer”E.W. Dijkstra Information Processing Letters 1: 179180, 1972这是一篇介绍生产者/消费者问题的著名文章。

[D01]“My recollections of operating system design”E.W. Dijkstra April, 2001如果你对这一领域的先驱们如何提出一些非常基本的概念（诸如“中断”和“栈”等概念）感兴趣，那么它是一本很好的读物！

[H74]“Monitors: An Operating System Structuring Concept”C.A.R. Hoare Communications of the ACM, 17:10, pages 549–557, October 1974 Hoare 在并发方面做了大量的理论工作。不过，他最出名的工作可能还是快速排序算法，那是世上最酷的排序算法，至少本书的作者这样认为。

[L11]“Pthread cond signal Man Page”Linux 手册页展示了一个很好的简单例子，以说明为什么线程可能会发生假唤醒——因为信号/唤醒代码中的竞态条件。

[LR80]“Experience with Processes and Monitors in Mesa”B.W. Lampson, D.R. Redell Communications of the ACM. 23:2, pages 105-117, February 1980一篇关于如何在真实系统中实际实现信号和条件变量的极好论文，导致了术语“Mesa”语义，说明唤醒意味着什么。较早的语义由Tony Hoare [H74]提出，于是被称为“Hoare”语义。

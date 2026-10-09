# 参考资料

[B+00]“Hoard: A Scalable Memory Allocator for Multithreaded Applications”Emery D. Berger, Kathryn S.McKinley, Robert D. Blumofe, and Paul R. Wilson ASPLOS-IX, November 2000 Berger 和公司的优秀多处理器系统分配程序。它不仅是一篇有趣的论文，也是能用于指导实战的！

[B94]“The Slab Allocator: An Object-Caching Kernel Memory Allocator”Jeff Bonwick USENIX ’94一篇关于如何为操作系统内核构建分配程序的好文章，也是如何专门针对特定通用对象大小的一个很好的例子。

[E06]“A Scalable Concurrent malloc(3) Implementation for FreeBSD”Jason Evans本文详细介绍如何构建一个真正的现代分配程序以用于多处理器。“jemalloc”分配程序今天在FreeBSD、NetBSD、Mozilla Firefox 和Facebook 中已广泛使用。

[K65]“A Fast Storage Allocator”Kenneth C. Knowlton Communications of the ACM, Volume 8, Number 10, October 1965伙伴分配的常见引用。一个奇怪的事实是：Knuth 不是把这个想法归功于Knowlton，而是归功于获得诺贝尔奖的经济学家Harry Markowitz。另一个奇怪的事实是：Knuth 通过秘书收发他的所有电子邮件。他不会自己发送电子邮件，而是告诉他的秘书要发送什么邮件，然后秘书负责发送电子邮件。最后一个关于Knuth的事实：他创建了TeX，这是用于排版本书的工具。这是一个惊人的软件[^p149-1]。

[S15]“Understanding glibc malloc”Sploitfun深入了解glibc malloc 是如何工作的。本文详细得令人惊讶，一篇非常好的阅读材料。

[W+95]“Dynamic Storage Allocation: A Survey and Critical Review”Paul R. Wilson, Mark S. Johnstone, Michael Neely, David Boles International Workshop on Memory Management Kinross, Scotland, September 1995对内存分配的许多方面进行了卓越且深入的调查，比这个小小的章节中所含的内容拥有更多的细节！

[^p149-1]: 实际上我们使用LaTeX，它基于Lamport 对TeX 的补充，但二者非常相似。

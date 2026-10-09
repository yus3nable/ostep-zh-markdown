# 参考资料

[BB+72]“TENEX, A Paged Time Sharing System for the PDP-10”Daniel G. Bobrow, Jerry D. Burchfiel, Daniel L. Murphy, Raymond S. Tomlinson Communications of the ACM,Volume 15, March 1972早期的分时操作系统，有许多好的想法来自于此。写时复制只是其中之一，在这里可以找到现代系统许多其他方面的灵感，包括进程管理、虚拟内存和文件系统。

[BJ81]“Converting a Swap-Based System to do Paging in an Architecture Lacking Page-Reference Bits”Ozalp Babaoglu and William N. Joy SOSP ’81, Pacific Grove, California, December 1981关于如何利用机器内现有的保护机制来模拟引用位的巧妙构思。这个想法来自Berkeley 的小组，他们正在致力于开发他们自己的UNIX 版本，也就是所谓的伯克利系统发行版，或称为BSD。该团队在UNIX 的发展中有很大的影响力，包括虚拟内存、文件系统和网络方面。

[BC05]“Understanding the Linux Kernel (Third Edition)”Daniel P. Bovet and Marco Cesati O’Reilly Media, November 2005关于Linux 的众多图书之一。它们很快就会过时，但许多基础知识仍然存在，值得一读。

[C03]“The Innovator’s Dilemma”Clayton M. Christenson Harper Paperbacks, January 2003一本关于硬盘驱动器行业的精彩图书，还涉及新的创新如何颠覆现有的技术。对于商科和计算机科学家来说，这是一本好书，提供了关于大型成功的公司如何完全失败的洞见。

[C93]“Inside Windows NT”Helen Custer and David Solomon Microsoft Press, 1993这本关于Windows NT 的书从头到尾地解释了系统，内容过于详细，你可能不喜欢。但认真地说，它是一本相当不错的书。

[LL82]“Virtual Memory Management in the VAX/VMS Operating System”Henry M. Levy, Peter H. Lipman IEEE Computer, Volume 15, Number 3 (March 1982)这是本章的大部分原始材料来源，它简洁易读。尤其重要的是，如果你想读研究生，你需要做的就是阅读论文、工作，阅读更多的论文、做更多的工作，最后写一篇论文，然后继续工作。但它很有趣！

[RL81]“Segmented FIFO Page Replacement”Rollins Turner and Henry Levy SIGMETRICS ’81, Las Vegas, Nevada, September 1981一篇简短的文章，显示了对于一些工作负载，分段的FIFO 可以接近LRU 的性能。

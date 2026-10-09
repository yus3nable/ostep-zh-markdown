# 参考资料

[B+10]“An Analysis of Linux Scalability to Many Cores”Silas Boyd-Wickizer, Austin T. Clements, Yandong Mao, Aleksey Pesterev, M. Frans Kaashoek, Robert Morris,Nickolai Zeldovich OSDI ’10, Vancouver, Canada, October 2010关于Linux 在多核机器上的表现以及对一些简单的解决方案的很好的研究。

[BH73]“Operating System Principles”Per Brinch Hansen, Prentice-Hall, 1973最早的操作系统图书之一。当然领先于它的时代。将观察者作为并发原语引入。

[BC05]“Understanding the Linux Kernel (Third Edition)”Daniel P. Bovet and Marco Cesati O’Reilly Media, November 2005关于Linux 内核的经典书籍。你应该阅读它。

[L+13]“A Study of Linux File System Evolution”Lanyue Lu, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau, Shan Lu FAST ’13, San Jose, CA, February 2013我们的论文研究了近十年来Linux 文件系统的每个补丁。论文中有很多有趣的发现，读读看！这项工作很痛苦，这位研究生Lanyue Lu 不得不亲自查看每一个补丁，以了解它们做了什么。

[MS98] “ Nonblocking Algorithms and Preemption-safe Locking on Multiprogrammed Sharedmemory Multiprocessors”M. Michael and M. Scott Journal of Parallel and Distributed Computing, Vol. 51, No. 1, 1998 Scott 教授和他的学生多年来一直处于并发算法和数据结构的前沿。浏览他的网页，并阅读他的大量的论文和书籍，可以了解更多信息。

[MS04]“Concurrent Data Structures”Mark Moir and Nir Shavit In Handbook of Data Structures and Applications(Editors D. Metha and S.Sahni) Chapman and Hall/CRC Press, 2004关于并发数据结构的简短但相对全面的参考。虽然它缺少该领域的一些最新作品（由于它的时间），但仍然是一个令人难以置信的有用的参考。

[MM00]“Solaris Internals: Core Kernel Architecture”Jim Mauro and Richard McDougall Prentice Hall, October 2000 Solaris 之书。如果你想详细了解Linux 之外的其他内容，就应该阅读本书。

[S+11]“Making the Common Case the Only Case with Anticipatory Memory Allocation”Swaminathan Sundararaman, Yupu Zhang, Sriram Subramanian,Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’11, San Jose, CA, February 2011我们关于从内核代码路径中删除可能失败的malloc 调用的工作。其主要想法是在做任何工作之前分配所有可能需要的内存，从而避免存储栈内部发生故障。

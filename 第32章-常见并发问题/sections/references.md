# 参考资料

[B+87]“Concurrency Control and Recovery in Database Systems”Philip A. Bernstein, Vassos Hadzilacos, Nathan Goodman Addison-Wesley, 1987数据库管理系统中并发性的经典教材。如你所知，理解数据库领域的并发性、死锁和其他主题本身就是一个世界。研究它，自己探索这个世界。

[C+71]“System Deadlocks”E.G. Coffman, M.J. Elphick, A. Shoshani ACM Computing Surveys, 3:2, June 1971这篇经典论文概述了死锁的条件以及如何处理它。当然有一些关于这个话题的早期论文，详细信息请参阅该论文的参考文献。

[D64]“Een algorithme ter voorkoming van de dodelijke omarming”Circulated privately, around 1964事实上，Dijkstra 不仅提出了死锁问题的一些解决方案，更重要的是他首先注意到了死锁的存在，至少是以书面形式。然而，他称之为“致命的拥抱”，（幸好）没有流行起来。

[GD02]“MapReduce: Simplified Data Processing on Large Clusters”Sanjay Ghemawhat and Jeff Dean OSDI ’04, San Francisco, CA, October 2004 MapReduce 论文迎来了大规模数据处理时代，提出了一个框架，在通常不可靠的机器群集上执行这样的计算。

[H91]“Wait-free Synchronization”Maurice Herlihy ACM TOPLAS, 13(1), pages 124-149, January 1991 Herlihy 的工作开创了无等待方式编写并发程序的想法。这些方法往往复杂而艰难，通常比正确使用锁更困难，可能会限制它们在现实世界中的成功。

[J+08]“Deadlock Immunity: Enabling Systems To Defend Against Deadlocks”Horatiu Jula, Daniel Tralamazza,Cristian Zamfir, George Candea OSDI ’08, San Diego, CA, December 2008最近的优秀文章，关于死锁以及如何避免在特定系统中一次又一次地陷入同一个问题。

[K81]“Soul of a New Machine”Tracy Kidder, 1980任何系统建造者或工程师都必须阅读，详细介绍Tom West 领导的Data General（DG）内部团队如何制造“新机器”的早期工作。Kidder 的其他图书也非常出色，其中包括《Mountains beyond Mountains》。或者，也许你不同意我们的观点？

[K87]“Deadlock Detection in Distributed Databases”Edgar Knapp ACM Computing Surveys, Volume 19, Number 4, December 1987分布式数据库系统中死锁检测的极好概述，也指出了一些其他相关的工作，因此是开始阅读的好文章。

[L+08]“Learning from Mistakes — A Comprehensive Study on Real World Concurrency Bug Characteristics”Shan Lu, Soyeon Park, Eunsoo Seo, Yuanyuan Zhou ASPLOS ’08, March 2008, Seattle, Washington首次深入研究真实软件中的并发错误，也是本章的基础。参见Y.Y. Zhou 或Shan Lu 的网页，有许多关于缺陷的更有趣的论文。

[T+94]“Linux File Memory Map Code”Linus Torvalds and many others感谢Michael Walfish（纽约大学）指出这个宝贵的例子。真实的世界，就像你在这个文件中看到的那样，可能比教科书中的简单、清晰更复杂一些。

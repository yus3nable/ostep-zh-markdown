# 参考资料

[B+07]“An Analysis of Latent Sector Errors in Disk Drives”Lakshmi N. Bairavasundaram, Garth R. Goodson, Shankar Pasupathy, Jiri Schindler SIGMETRICS ’07, San Diego, California, June 2007一篇详细研究潜在扇区错误的论文。正如引文[B+08]所述，这是威斯康星大学与NetApp 之间的合作。该论文还获得了Kenneth C. Sevcik 杰出学生论文奖。Sevcik 是一位了不起的研究者，也是一位太早过世的好人。为了向本书作者展示有可能从美国搬到加拿大并喜欢上这个地方，Sevcik 曾经站在餐馆中间唱过加拿大国歌。

[B+08]“An Analysis of Data Corruption in the Storage Stack”Lakshmi N. Bairavasundaram, Garth R. Goodson,Bianca Schroeder, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’08, San Jose, CA, February 2008一篇真正详细研究磁盘讹误的论文，重点关注超过150 万个驱动器3 年内发生此类讹误的频率。Lakshmi 做这项工作时还是威斯康星大学的一名研究生，在我们的指导下，同时也与他在NetApp 的同事合作，他有几个暑假都在NetApp 做实习生。与业界合作可以带来更有趣、有实际意义的研究，这是一个很好的例子。

[BS04]“Commercial Fault Tolerance: A Tale of Two Systems”Wendy Bartlett, Lisa Spainhower IEEE Transactions on Dependable and Secure Computing, Vol. 1, No. 1, January 2004这是构建容错系统的经典之作，是对IBM 和Tandem 最新技术的完美概述。对该领域感兴趣的人应该读这篇文章。

[C+04]“Row-Diagonal Parity for Double Disk Failure Correction”P. Corbett, B. English, A. Goel, T. Grcanac, S. Kleiman, J. Leong, S. Sankar FAST ’04, San Jose, CA, February 2004关于额外冗余如何帮助解决组合的全磁盘故障/部分磁盘故障问题的早期文章。这也是如何将更多理论工作与实践相结合的一个很好的例子。

[F04]“Checksums and Error Control”Peter M. Fenwick一个非常简单的校验和教程，免费提供给你阅读。

[F82]“An Arithmetic Checksum for Serial Transmissions”John G. Fletcher IEEE Transactions on Communication, Vol. 30, No. 1, January 1982 Fletcher 的原创工作，内容关于以他命名的校验和。当然，他并没有把它称为Fletcher 校验和，实际上他没有把它称为任何东西，因此用发明者的名字来命名它就变得很自然了。所以不要因这个看似自夸的名称而责怪老Fletcher。这个轶事可能会让你想起Rubik 和他的立方体（魔方）。Rubik 从未称它为“Rubik 立方体”。实际上，他只是称之为“我的立方体”。

[HLM94]“File System Design for an NFS File Server Appliance”Dave Hitz, James Lau, Michael Malcolm USENIX Spring ’94这篇开创性的论文描述了NetApp 核心的思想和产品。基于该系统，NetApp 已经发展成为一家价值数十亿美元的存储公司。如果你有兴趣了解更多有关其成立的信息，请阅读Hitz 的自传《How to Castrate a Bull:Unexpected Lessons on Risk, Growth, and Success in Business》（如何阉割公牛：商业风险，成长和成功的意外教训）”（这是真实的标题，不是开玩笑）。你本以为进入计算机科学领域可以避免“阉割公牛”吧？

[K+08]“Parity Lost and Parity Regained”Andrew Krioukov, Lakshmi N. Bairavasundaram, Garth R. Goodson, Kiran Srinivasan, Randy Thelen, Andrea C.Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’08, San Jose, CA, February 2008我们的这项工作与NetApp 的同事一起探讨了不同的校验和方案如何在保护数据方面起作用（或不起作用）。我们揭示了当前保护策略中的一些有趣缺陷，其中一些已导致商业产品的修复。

[M13]“Cyclic Redundancy Checks”Author Unknown不确定是谁写的，但这是一个非常简洁明了的CRC 说明。事实证明，互联网充满了信息。

[P+05]“IRON File Systems”Vijayan Prabhakaran, Lakshmi N. Bairavasundaram, Nitin Agrawal, Haryadi S. Gunawi, An- drea C.Arpaci-Dusseau, Remzi H. Arpaci-Dusseau SOSP ’05, Brighton, England, October 2005我们关于磁盘如何具有部分故障模式的论文，其中包括对Linux ext3 和Windows NTFS 等文件系统如何对此类故障作出反应的详细研究。事实证明，相当糟糕！我们在这项工作中发现了许多错误、设计缺陷和其他奇怪之处。其中一些已反馈到Linux 社区，从而有助于产生一些新的更强大的文件系统来存储数据。

[RO91]“Design and Implementation of the Log-structured File System”Mendel Rosenblum and John Ousterhout SOSP ’91, Pacific Grove, CA, October 1991一篇关于如何提高文件系统写入性能的开创性论文。

[S90]“Implementing Fault-Tolerant Services Using The State Machine Approach: A Tutorial”Fred B. Schneider ACM Surveys, Vol. 22, No. 4, December 1990这篇经典论文主要讨论如何构建容错服务，其中包含了许多术语的基本定义。从事构建分布式系统的人应该读一读这篇论文。

[Z+13]“Zettabyte Reliability with Flexible End-to-end Data Integrity”Yupu Zhang, Daniel S. Myers, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau MSST ’13, Long Beach,California, May 2013这是我们自己的工作，将数据保护添加到系统的页面缓存中，以防止内存讹误和磁盘讹误。

# 参考资料

[B+08]“An Analysis of Data Corruption in the Storage Stack”Lakshmi N. Bairavasundaram, Garth R. Goodson, Bianca Schroeder, Andrea C. Arpaci-Dusseau, Remzi H.Arpaci-Dusseau FAST ’08, San Jose, CA, February 2008我们自己的工作分析了磁盘实际损坏数据的频率。不经常，但有时会发生！因此，一个可靠的存储系统必须考虑。

[BJ88]“Disk Shadowing”D. Bitton and J. Gray VLDB1988首批讨论镜像的论文之一，这里称镜像为“影子”。

[CL95]“Striping in a RAID level 5 disk array”Peter M. Chen, Edward K. Lee SIGMETRICS 1995对RAID-5 磁盘阵列中的一些重要参数进行了很好的分析。

[C+04]“Row-Diagonal Parity for Double Disk Failure Correction”P. Corbett, B. English, A. Goel, T. Grcanac, S. Kleiman, J. Leong, S. Sankar FAST ’04, February 2004虽然不是第一篇关于带有两块磁盘以实现奇偶校验的RAID 系统的论文，但它是这个想法的最新和高度可理解的版本。阅读它，了解更多信息。

[DAA05]“Journal-guided Resynchronization for Software RAID”Timothy E. Denehy, A. Arpaci-Dusseau, R.Arpaci-Dusseau FAST 2005我们自己在一致更新问题上的研究工作。在这里，我们通过将上述文件系统的日志机制与其下的软件RAID集成在一起，来解决它的软件RAID 问题。

[HLM94]“File System Design for an NFS File Server Appliance”Dave Hitz, James Lau, Michael Malcolm USENIX Winter 1994, San Francisco, California, 1994关于稀疏文件系统的论文，介绍了存储中的标志性产品，任意位置写入文件布局，即WAFL 文件系统，这是NetApp 文件服务器的基础。

[K86]“Synchronized Disk Interleaving”M.Y. Kim.IEEE Transactions on Computers, Volume C-35: 11, November 1986在这里可以找到关于RAID 的一些最早的工作。

[K88]“Small Disk Arrays - The Emerging Approach to High Performance”F. Kurzweil.Presentation at Spring COMPCON ’88, March 1, 1988, San Francisco, California另一个早期的RAID 参考。

[P+88]“Redundant Arrays of Inexpensive Disks”D．Patterson, G. Gibson, R. Katz. SIGMOD 1988本论文由著名作者Patterson、Gibson 和Katz 撰写。此后，该论文赢得了众多奖项，宣告了RAID 时代的到来，甚至RAID 这个名字本身也源于此文。

[PB86]“Providing Fault Tolerance in Parallel Secondary Storage Systems”A．Park and K. Balasubramaniam Department of Computer Science, Princeton, CS-TR-O57-86, November 1986另一项关于RAID 的早期研究工作。

[SG86]“Disk Striping”K. Salem and H. Garcia-Molina.IEEE International Conference on Data Engineering, 1986是的，另一项早期的RAID 研究工作。当那篇RAID 论文在SIGMOD 发布时，有很多这类论文公开发表。

[S84]“Byzantine Generals in Action: Implementing Fail-Stop Processors”F.B. Schneider.ACM Transactions on Computer Systems, 2(2):145154, May 1984一篇不是关于RAID 的文章！本文实际上是关于系统如何发生故障，以及如何让某些运行变成故障就停止。

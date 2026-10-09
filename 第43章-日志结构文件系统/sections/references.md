# 参考资料

[B07]“ZFS: The Last Word in File Systems”Jeff Bonwick and Bill Moore关于ZFS 的幻灯片。遗憾的是，没有优秀的ZFS 论文。

[HLM94]“File System Design for an NFS File Server Appliance”Dave Hitz, James Lau, Michael Malcolm USENIX Spring ’94 WAFL 从LFS 和RAID 中获取了许多想法，并将其置于数十亿美元的存储公司NetApp 的高速NFS 设备中。

[L77]“Physical Integrity in a Large Segmented Database”R. Lorie ACM Transactions on Databases, 1977, Volume 2:1, pages 91-104这里介绍了影子分页的最初想法。

[M07]“The Btrfs Filesystem”Chris Mason September 2007最近的一种写时复制Linux 文件系统，其重要性和使用率逐渐增加。

[MJLF84]“A Fast File System for UNIX”Marshall K. McKusick, William N. Joy, Sam J. Leffler, Robert S. Fabry ACM TOCS, August, 1984, Volume 2,Number 3最初的FFS 文件。有关详细信息，请参阅有关FFS 的章节。

[MR+97]“Improving the Performance of Log-structured File Systems with Adaptive Methods”Jeanna Neefe Matthews, Drew Roselli, Adam M. Costello,Randolph Y. Wang, Thomas E. Anderson SOSP 1997, pages 238-251, October, Saint Malo, France最近的一篇论文，详细说明了LFS 中更好的清理策略。

[M94]“A Better Update Policy”Jeffrey C. Mogul USENIX ATC ’94, June 1994在该文中，Mogul 发现，因为缓冲写入时间过长，然后集中发送到磁盘中，读取工作负载可能会受到影响。因此，他建议更频繁地以较小的批次发送写入。

[P98]“Hardware Technology Trends and Database Opportunities”David A. Patterson ACM SIGMOD ’98 Keynote Address, Presented June 3, 1998, Seattle, Washington关于计算机系统技术趋势的一系列幻灯片。也许Patterson 很快就会制作另一个幻灯片。

[RO91]“Design and Implementation of the Log-structured File System”Mendel Rosenblum and John Ousterhout SOSP ’91, Pacific Grove, CA, October 1991关于LFS 的原始SOSP 论文，已被数百篇其他论文引用，并启发了许多真实系统。

[R92]“Design and Implementation of the Log-structured File System”Mendel Rosenblum关于LFS 的获奖学位论文，包含其他论文中缺失的许多细节。

[SS+95]“File system logging versus clustering: a performance comparison”Margo Seltzer, Keith A. Smith, Hari Balakrishnan, Jacqueline Chang, Sara McMains, Venkata Padmanabhan USENIX 1995 Technical Conference, New Orleans, Louisiana, 1995该文显示LFS 的性能有时会出现问题，特别是对于多次调用fsync()的工作负载（例如数据库工作负载）。该论文当时备受争议。

[SO90]“Write-Only Disk Caches”Jon A. Solworth, Cyril U. Orji SIGMOD ’90, Atlantic City, New Jersey, May 1990对写缓冲及其好处的早期研究。但是，缓冲太长时间可能会产生危害，详情请参阅Mogul [M94]。

[Z+12]“De-indirection for Flash-based SSDs with Nameless Writes”Yiying Zhang, Leo Prasath Arulraj, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’13, San Jose,California, February 2013我们的论文介绍了构建基于闪存的存储设备的新方法。由于FTL（闪存转换层）通常以日志结构样式构建，因此在基于闪存的设备中会出现一些LFS 中相同的问题。在这个例子中，它是递归更新问题，LFS 用imap巧妙地解决了这个问题。大多数SSD 中存在类似的结构。

# 参考资料

[B07]“ZFS: The Last Word in File Systems”Jeff Bonwick and Bill Moore实际上，ZFS 使用写时复制和日志，因为在某些情况下，对磁盘的写入记日志性能更好。

[C+12]“Consistency Without Ordering”Vijay Chidambaram, Tushar Sharma, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’12, San Jose,California我们最近发表的一篇关于基于反向指针的新形式的崩溃一致性的论文。阅读它，了解令人兴奋的细节内容！

[C+13]“Optimistic Crash Consistency”Vijay Chidambaram, Thanu S. Pillai, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau SOSP ’13, Nemacolin Woodlands Resort, PA, November 2013我们致力于更乐观、更高性能的日志协议。对于大量调用fsync()的工作负载，可以大大提高性能。

[GP94]“Metadata Update Performance in File Systems”Gregory R. Ganger and Yale N. Patt OSDI ’94一篇关于使用谨慎的写入顺序作为实现一致性的主要方法的优秀论文。后来在基于BSD 的系统中实现。

[G+08]“SQCK: A Declarative File System Checker”Haryadi S. Gunawi, Abhishek Rajimwale, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau OSDI ’08, San Diego, California我们自己的论文，介绍了一种使用SQL 查询构建文件系统检查程序的新方法。我们还展示了现有检查器的一些问题，发现了许多错误和奇怪的行为，这是FSCK 复杂性的直接结果。

[H87]“Reimplementing the Cedar File System Using Logging and Group Commit”Robert Hagmann SOSP ’87, Austin, Texas, November 1987第一项工作（我们所知的）将预写日志（即日志）应用于文件系统。

[M+13]“ffsck: The Fast File System Checker”Ao Ma, Chris Dragga, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’13, San Jose, California,February 2013这篇文章详细介绍了如何让FSCK 快一个数量级。一些想法已经集成到BSD 文件系统检查器[MK96]中，并已部署。

[MK96]“Fsck - The UNIX File System Check Program”Marshall Kirk McKusick and T. J. Kowalski Revised in 1996由开发FFS 的一些人编写的描述第一个全面的文件系统检查工具，即因此得名的FSCK。

[MJLF84]“A Fast File System for UNIX”Marshall K. McKusick, William N. Joy, Sam J. Leffler, Robert S. Fabry ACM Transactions on Computing Systems.August 1984, Volume 2:3你已经对FFS 了解得够多了，对吗？但是，可以在书中不止一次地引用这样的论文。

[P+05]“IRON File Systems”Vijayan Prabhakaran, Lakshmi N. Bairavasundaram, Nitin Agrawal, Haryadi S. Gunawi, An- drea C.Arpaci-Dusseau, Remzi H. Arpaci-Dusseau SOSP ’05, Brighton, England, October 2005该论文主要关注研究文件系统如何对磁盘故障做出反应。在最后，我们引入了一个事务校验和来加速日志，最终被Linux ext4 采用。

[PAA05]“Analysis and Evolution of Journaling File Systems”Vijayan Prabhakaran, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau USENIX ’05, Anaheim, California,April 2005我们早期写的一篇论文，分析了日志文件系统的工作原理。

[R+11]“Coerced Cache Eviction and Discreet-Mode Journaling”Abhishek Rajimwale, Vijay Chidambaram,Deepak Ramamurthi, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau DSN ’11, Hong Kong, China, June 2011我们自己的论文，关于磁盘缓冲写入内存缓存而不是强制它们写入磁盘的问题，即使明确告知不这样做！我们克服这个问题的解决方案：如果你想在B 之前将A 写入磁盘，首先写A，然后向磁盘发送大量“虚拟”写入，希望将A 强制写入磁盘，以便为它们在缓存中腾出空间。一个简洁但不太实际的解决方案。

[T98]“Journaling the Linux ext2fs File System”Stephen C. Tweedie The Fourth Annual Linux Expo, May 1998 Tweedie 在为Linux ext2 文件系统添加日志方面做了大量工作。结果毫不奇怪地被称为ext3。一些不错的设计决策包括强烈关注向后兼容性，例如，你只需将日志文件添加到现有的ext2 文件系统，然后将其挂载为ext3 文件系统。

[T00]“EXT3, Journaling Filesystem”Stephen Tweedie Talk at the Ottawa Linux Symposium, July 2000 olstrans.sourceforge.net/release/OLS2000-ext3/OLS2000-ext3.html Tweedie 关于ext3 的演讲的文字记录。

[T01]“The Linux ext2 File System”Theodore Ts’o, June, 2001.一个简单的Linux 文件系统，基于FFS 中的想法。有一段时间它被大量使用，现在它真的只是在内核中作为简单文件系统的一个例子。

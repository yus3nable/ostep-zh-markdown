# 参考资料

[A+07] Nitin Agrawal, William J. Bolosky, John R. Douceur, Jacob R. Lorch A Five-Year Study of File-System Metadata FAST ’07, pages 31–45, February 2007, San Jose, CA最近对文件系统实际使用方式的一个很好的分析。利用其中的文献目录可以追溯到20 世纪80 年代早期的文件系统分析论文。

[B07]“ZFS: The Last Word in File Systems”Jeff Bonwick and Bill Moore最新的重要文件系统之一，功能丰富，性能卓越。我们应该为它写一章，也许很快就会有这么一章。

[B02]“The FAT File System”Andries Brouwer, September, 2002关于FAT 的很好、很漂亮的描述。文件系统的类型，不是培根的类型。但你必须承认，培根可能味道更好。

[C94]“Inside the Windows NT File System”, Helen Custer Microsoft Press, 1994一本关于NTFS 的小书，其他书中可能有更多技术s 细节。

[H+88]“Scale and Performance in a Distributed File System”John H. Howard, Michael L. Kazar, Sherri G. Menees, David A. Nichols, M. Satyanarayanan, Robert N.Sidebotham, Michael J. West.ACM Transactions on Computing Systems (ACM TOCS), page 51-81, Volume 6, Number 1, February 1988经典的分布式文件系统，我们稍后会更多地了解它，不用担心。

[P09]“The Second Extended File System: Internal Layout”Dave Poirier, 2009有关ext2 的详细信息，这是一个非常简单的基于FFS 的Linux 文件系统，即Berkeley Fast File System。我们将在第41 章中详细解读。

[RT74]“The UNIX Time-Sharing System”M．Ritchie and K. Thompson CACM, Volume 17:7, pages 365-375, 1974关于UNIX 的较早的论文。阅读它，能了解许多现代操作系统的基础知识。

[S00]“UBC: An Efficient Unified I/O and Memory Caching Subsystem for NetBSD”Chuck Silvers FREENIX, 2000一篇关于NetBSD 集成文件系统缓冲区缓存和虚拟内存页面缓存的好文章。许多其他系统做了同样的事情。

[S+96]“Scalability in the XFS File System”Adan Sweeney, Doug Doucette, Wei Hu, Curtis Anderson, Mike Nishimoto, Geoff Peck USENIX ’96, January 1996, San Diego, CA第一次尝试让操作具有可伸缩性，其中包括在目录中拥有数百万个文件这样的事情，这是核心关注点。它是一个把想法推向极致的好例子。这个文件系统的关键思想是：一切都是树。我们也应该为这个文件系统写一章内容。

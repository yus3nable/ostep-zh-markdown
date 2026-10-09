# 参考资料

[B+91]“Measurements of a Distributed File System”Mary Baker, John Hartman, Martin Kupfer, Ken Shirriff, John Ousterhout SOSP ’91, Pacific Grove, California,October 1991早期的论文，测量人们如何使用分布式文件系统，符合AFS 中的大部分直觉。

[H+11]“A File is Not a File: Understanding the I/O Behavior of Apple Desktop Applications”Tyler Harter, Chris Dragga, Michael Vaughn,Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau SOSP ’11, New York, New York, October 2011我们自己的论文，研究Apple Desktop 工作负载的行为。事实证明，它们与系统研究社区通常关注的许多基于服务器的工作负载略有不同。本文也是一篇优秀的参考文献，指出了很多相关的工作。

[H+88]“Scale and Performance in a Distributed File System”John H. Howard, Michael L. Kazar, Sherri G. Menees, David A. Nichols, M. Satyanarayanan, Robert N.Sidebotham, Michael J. West ACM Transactions on Computing Systems (ACM TOCS), page 51-81, Volume 6, Number 1, February 1988著名的AFS 系统的期刊长版本，该系统仍然在全世界的许多地方使用，也可能是关于如何构建分布式文件系统的最早的清晰思考。它是测量科学和原理工程的完美结合。

[R+00]“A Comparison of File System Workloads”Drew Roselli, Jacob R. Lorch, Thomas E. Anderson USENIX ’00, San Diego, California, June 2000与Baker 的论文[B+91]相比，有最近的一些记录。

[S+85]“The ITC Distributed File System: Principles and Design”M．Satyanarayanan, J.H. Howard, D.A. Nichols, R.N. Sidebotham, A. Spector, M.J. West SOSP ’85, Orcas Island,Washington, December 1985关于分布式文件系统的较早的文章。AFS 的许多基本设计都在这个较早的系统中实现，但没有对扩展进行改进。

[V99]“File system usage in Windows NT 4.0”Werner Vogels SOSP '99, Kiawah Island Resort, South Carolina, December 1999对Windows 工作负载的一项很酷的研究，与之前已经完成的许多基于UNIX 的研究相比，它在本质上是不同的。

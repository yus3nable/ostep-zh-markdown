# 参考资料

[BS+09]“Tolerating File-System Mistakes with EnvyFS”Lakshmi N. Bairavasundaram, Swaminathan Sundararaman, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau USENIX ’09, San Diego, CA, June 2009一篇有趣的文章，讲述同时使用多个文件系统以容忍其中任何一个文件系统出现错误。

[BH00]“The Evolution of Operating Systems”P. Brinch Hansen In Classic Operating Systems: From Batch Processing to Distributed Systems Springer-Verlag, New York, 2000这篇文章介绍了与具有历史意义的系统相关的内容。

[B+72]“TENEX, A Paged Time Sharing System for the PDP-10”Daniel G. Bobrow, Jerry D. Burchfiel, Daniel L. Murphy, Raymond S. Tomlinson CACM, Volume 15, Number 3,March 1972 TENEX 拥有现代操作系统中的许多机制。请阅读更多关于它的信息，看看在20 世纪70 年代早期已经有了哪些创新。

[B75]“The Mythical Man-Month”Fred Brooks Addison-Wesley, 1975一本关于软件工程的经典教科书，非常值得一读。

[BOH10]“Computer Systems: A Programmer’s Perspective”Randal E. Bryant and David R. O’Hallaron Addison-Wesley, 2010关于计算机系统工作原理的另一本卓越的图书，与本书的内容有一点点重叠——所以，如果你愿意，你可以跳过本书的最后几章，或者直接阅读它们，以获取关于某些相同材料的不同观点。毕竟，健全与完善自己知识的一个好方法，就是尽可能多地听取其他观点，然后在此问题上扩展自己的观点和想法。

[K+61]“One-Level Storage System”T. Kilburn, D.B.G. Edwards, M.J. Lanigan, F.H. Sumner IRE Transactions on Electronic Computers, April 1962 Atlas 开创了你在现代系统中看到的大部分概念。但是，这篇论文并不是最好的读物。如果你只读一篇文章，可以了解一下下面的历史观点[L78]。

[L78]“The Manchester Mark I and Atlas: A Historical Perspective”S.H. Lavington Communications of the ACM archive Volume 21, Issue 1 (January 1978), pages 4-12关于计算机系统早期发展的历史和Atlas 的开拓性工作。当然，我们可以自己阅读Atlas 的论文，但是这篇论文提供了一个对计算机系统的很好的概述，并且增加了一些历史观点。

[O72]“The Multics System: An Examination of its Structure”Elliott Organick, 1972 Multics 的完美概述。这么多好的想法，但它是一个过度设计的系统，目标太多，因此从未真正按预期工作。Fred Brooks 是所谓的“第二系统效应”的典型例子[B75]。

[PP03]“Introduction to Computing Systems: From Bits and Gates to C and Beyond”Yale N. Patt and Sanjay J. Patel McGraw-Hill, 2003我们最喜欢的计算系统图书之一。它从晶体管开始讲解，一直讲到C。书中早期的素材特别好。

[RT74]“The UNIX Time-Sharing System”Dennis M. Ritchie and Ken Thompson CACM, Volume 17, Number 7, July 1974, pages 365-375关于UNIX 的杰出总结，作者撰写此书时，UNIX 正在计算世界里占据统治地位。

[S68]“SDS 940 Time-Sharing System”Scientific Data Systems Inc.TECHNICAL MANUAL, SDS 90 11168 August 1968这是我们可以找到的一本不错的技术手册。阅读这些旧的系统文件，能看到在20 世纪60 年代后期技术发展的进程，这很有意思。伯克利时分系统（最终成为SDS 系统）背后的核心构建者之一是Butler Lampson，后来他因系统贡献而获得图灵奖。

[SS+10]“Membrane: Operating System Support for Restartable File Systems”Swaminathan Sundararaman,Sriram Subramanian, Abhishek Rajimwale, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau, Michael M.Swift FAST ’10, San Jose, CA, February 2010写自己的课程注解的好处是：你可以为自己的研究做广告。但是这篇论文实际上非常简洁。当文件系统遇到错误并崩溃时，Membrane 会自动重新启动它，所有这些都不会导致应用程序或系统的其他部分受到影响。

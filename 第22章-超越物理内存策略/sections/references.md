# 参考资料

[AD03]“Run-Time Adaptation in River”Remzi H. Arpaci-Dusseau ACM TOCS, 21:1, February 2003本书作者之一关于River 系统的研究工作的总结。当然，在其中，他发现与理想情况做比较是系统设计人员的一项重要技术。

[B66]“A Study of Replacement Algorithms for Virtual-Storage Computer”Laszlo A. Belady IBM Systems Journal 5(2): 78-101, 1966这篇文章介绍了计算策略最优行为的简单方法（MIN 算法）。

[BNS69]“An Anomaly in Space-time Characteristics of Certain Programs Running in a Paging Machine”L. A. Belady and R. A. Nelson and G. S. Shedler Communications of the ACM, 12:6, June 1969介绍称为“Belady 的异常”的内存引用的小序列的文章。我们想知道，Nelson 和Shedler 如何看待这个名字呢？

[CD85]“An Evaluation of Buffer Management Strategies for Relational Database Systems”Hong-Tai Chou and David J. DeWitt VLDB ’85, Stockholm, Sweden, August 1985关于不同缓冲策略的著名数据库文章，你应该使用多种常见数据库访问模式。如果你知道有关工作负载的某些信息，那么就可以制订策略，让它比操作系统中常见的通用目标策略更好。

[C69]“A Paging Experiment with the Multics System”F.J. Corbato Included in a Festschrift published in honor of Prof. P.M. Morse MIT Press, Cambridge, MA, 1969对时钟算法的最初引用（很难找到！），但不是第一次使用位。感谢麻省理工学院的H. Balakrishnan 为我们找出这篇论文。

[D70]“Virtual Memory”Peter J. Denning Computing Surveys, Vol. 2, No. 3, September 1970 Denning 对虚拟存储系统的早期著名调查。

[EF78]“Cold-start vs. Warm-start Miss Ratios”Malcolm C. Easton and Ronald Fagin Communications of the ACM, 21:10, October 1978关于冷启动与热启动未命中的很好的讨论。

[FP89]“Electrochemically Induced Nuclear Fusion of Deuterium”Martin Fleischmann and Stanley Pons Journal of Electroanalytical Chemistry, Volume 26, Number 2, Part 1, April, 1989这篇著名的论文有可能为世界带来革命性的变化，它提供了一种简单的方法，可以从水罐中产生几乎无限的电力，而电力罐中只含有少许金属。但Pons 和Fleischmann 发表的（并广为宣传的）实验结果无法重现，因此这两位有梦想的科学家都丧失了名誉（当然也受到了嘲笑）。唯一真正为这个结果感到高兴的人是Marvin Hawkins，尽管他参与了这项工作，但他的名字却从本文中被删除了。他因而避免将他的名字与20世纪最大的科学失误之一联系起来。

[HP06]“Computer Architecture: A Quantitative Approach”John Hennessy and David Patterson Morgan-Kaufmann, 2006一本关于计算机体系结构的了不起而奇妙的书，必读！

[H87]“Aspects of Cache Memory and Instruction Buffer Performance”Mark D. Hill Ph.D. Dissertation, U.C. Berkeley, 1987 Mark Hill 在其论文工作中介绍了3C，后来因其被包含在H&amp;P [HP06]中而广泛流行。其中的引述：“我发现根据未命中的原因直观地将未命中划分为3 个部分是有用的（第49 页）。”

[KE+62]“One-level Storage System”T. Kilburn, and D.B.G. Edwards and M.J. Lanigan and F.H. Sumner IRE Trans. EC-11:2, 1962虽然Atlas 有一个使用位，但它只有很少量的页，因此在大型存储器中使用位的扫描并不是作者解决的问题。

[M+70]“Evaluation Techniques for Storage Hierarchies”R．L. Mattson, J. Gecsei, D. R. Slutz, I. L. Traiger IBM Systems Journal, Volume 9:2, 1970一篇主要关于如何高效地模拟缓存层次结构的论文。本文无疑是这方面的经典之作，还有对各种替代算法的一些特性的极佳讨论。你能弄清楚为什么栈属性可能对同时模拟很多不同大小的缓存有用吗？

[MM03]“ARC: A Self-Tuning, Low Overhead Replacement Cache”Nimrod Megiddo and Dharmendra S. Modha FAST 2003, February 2003, San Jose, California关于替换算法的优秀现代论文，其中包括现在某些系统中使用的新策略ARC。在2014 年FAST ’14 大会上，获得了存储系统社区的“时间考验”奖。

# 参考资料

[B04]“Implementing Condition Variables with Semaphores”Andrew Birrell December 2004一本关于在信号量上实现条件变量有多困难，以及作者和同事在此过程中犯的错误的有趣读物。因为该小组进行了大量的并发编程，所以讲述特别中肯。例如，Birrell 以编写各种线程编程指南而闻名。

[CB08]“Real-world Concurrency”Bryan Cantrill and Jeff Bonwick ACM Queue. Volume 6, No. 5. September 2008一篇很好的文章，来自一家以前名为Sun 的公司的一些内核黑客，讨论了并发代码中面临的实际问题。

[CHP71]“Concurrent Control with Readers and Writers”P.J. Courtois, F. Heymans, D.L. Parnas Communications of the ACM, 14:10, October 1971读者—写者问题的介绍以及一个简单的解决方案。后来的工作引入了更复杂的解决方案，这里跳过了，因为它们非常复杂。

[D59]“A Note on Two Problems in Connexion with Graphs”E. W. Dijkstra Numerische Mathematik 1, 269271, 1959你能相信人们在1959 年从事算法工作吗？我们很难相信。即使在计算机用起来有趣之前，这些人都感觉到他们会改变世界……

[D68a]“Go-to Statement Considered Harmful”E.W. Dijkstra Communications of the ACM, volume 11(3): pages 147148, March 1968有时被认为是软件工程领域的开始。

[D68b]“The Structure of the THE Multiprogramming System”E.W. Dijkstra Communications of the ACM, volume 11(5), pages 341346, 1968最早的论文之一，指出计算机科学中的系统工作是一项引人入胜的智力活动，也为分层系统式的模块化进行了强烈辩护。

[D72]“Information Streams Sharing a Finite Buffer”E.W. Dijkstra Information Processing Letters 1: 179180, 1972 Dijkstra 创造了一切吗？不，但可能差不多。他当然是第一位明确写下并发代码中的问题的人。然而，操作系统设计的从业者确实知道Dijkstra 所描述的许多问题，所以将太多东西归功于他也许是对历史的误传。

[D08]“The Little Book of Semaphores”A.B. Downey一本关于信号量的好书（而且免费！）。如果你喜欢这样的事情，有很多有趣的问题等待解决。

[DHO71]“Hierarchical ordering of sequential processes”E.W. Dijkstra介绍了许多并发问题，包括哲学家就餐问题。关于这个问题，维基百科也给出了很丰富的内容。

[GR92]“Transaction Processing: Concepts and Techniques”Jim Gray and Andreas Reuter Morgan Kaufmann, September 1992我们发现特别幽默的引用就在第485 页，第8.8 节开始处：“第一个多处理器，大约在1960 年，就有测试并设置指令……大概是OS 的实现者想出了正确的算法，尽管通常认为Dijkstra 在多年后发明信号量。”

[H87]“Aspects of Cache Memory and Instruction Buffer Performance”Mark D. Hill Ph.D. Dissertation, U.C. Berkeley, 1987 Hill 的学位论文工作，给那些痴迷于早期系统缓存的人。量化论文的一个很好的例子。

[L83]“Hints for Computer Systems Design”Butler Lampson ACM Operating Systems Review, 15:5, October 1983著名系统研究员Lampson 喜欢在设计计算机系统时使用暗示。暗示经常是正确的，但可能是错误的。在这种用法中，signal()告诉等待线程它改变了等待的条件，但不要相信当等待线程唤醒时条件将处于期望的状态。在这篇关于系统设计的暗示的文章中， Lampson 的一般暗示是你应该使用暗示。这并不像听上去那么令人困惑。

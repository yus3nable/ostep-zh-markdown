# 参考资料

[AA06]“A Comparison of Software and Hardware Techniques for x86 Virtualization”Keith Adams and Ole Agesen ASPLOS ’06, San Jose, California来自两位VMware 工程师的一篇优秀的论文，讲述了为虚拟化提供硬件支持所带来的惊人的小优势。此外，还有关于VMware 虚拟化的一般性讨论，包括为了虚拟化难以虚拟化的x86 平台，而必须采用的疯狂的二进制翻译技巧。

[AD+01] “ Information and Control in Gray-box Systems ” Andrea C. Arpaci-Dusseau and Remzi H.Arpaci-Dusseau SOSP ’01, Banff, Canada我们自己的工作是如何推断信息，甚至从应用程序级别对操作系统施加控制，而不对操作系统进行任何更改。其中最好的例子：使用基于概率探测器的技术确定在OS 中缓存哪些文件块。这样做可以让应用程序更好地利用缓存，优先安排会导致命中的工作。

[B00]“FreeBSD Developers’ Handbook:Chapter 11 x86 Assembly Language Programming”一本BSD 开发者手册中关于系统调用的很好的教程。

[BD+03]“Xen and the Art of Virtualization”Paul Barham, Boris Dragovic, Keir Fraser, Steven Hand, Tim Harris, Alex Ho, Rolf Neuge- bauer, Ian Pratt,Andrew Warfield SOSP ’03, Bolton Landing, New York该论文表明，对于半虚拟化系统，虚拟化系统的开销可以低得令人难以置信。这篇关于Xen 虚拟机监视器的论文如此成功，导致了一家公司的诞生。

[B+97]“Disco: Running Commodity Operating Systems on Scalable Multiprocessors”Edouard Bugnion, Scott Devine, Kinshuk Govil, Mendel Rosenblum SOSP ’97将系统社区重新带回虚拟机研究的论文。好吧，也许这是不公平的，因为Bressoud 和Schneider [BS95]也做了，但在这里我们开始理解为什么虚拟化会回来。然而更令人瞩目的是，这群优秀的研究人员创立了VMware，赚取了数十亿美元。

[BS95]“Hypervisor-based Fault-tolerance”Thomas C. Bressoud, Fred B. Schneider SOSP ’95最早引入虚拟机管理程序（hypervisor，这只是虚拟机监视器的另一个术语）的论文之一。然而，在这项工作中，这些管理程序用于提高硬件故障的系统容忍度，这可能不如本章讨论的一些更实际的场景有用。但它本身仍然是一篇非常有趣的论文。

[G74]“Survey of Virtual Machine Research”R.P. Goldberg IEEE Computer, Volume 7, Number 6一份对许多老的虚拟机研究的调查。

[SVL01]“Virtualizing I/O Devices on VMware Workstation’s Hosted Virtual Machine Monitor”Jeremy Sugerman, Ganesh Venkitachalam and Beng-Hong Lim USENIX ’01, Boston, Massachusetts本文很好地概述了在使用托管体系结构的VMware 中I/O 的工作方式。该体系结构利用了许多操作系统自身的功能，避免了在VMM 中重新实现它们。

[V98] VMware corporation.这可能是本书中最无价值的参考资料，因为你可以自己阅读一下。但无论如何，该公司成立于1998 年，是虚拟化领域的领导者。

[S+03]“Semantically-Smart Disk Systems”Muthian Sivathanu, Vijayan Prabhakaran, Florentina I. Popovici, Timothy E. Denehy, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau FAST ’03, San Francisco, California, March 2003又是我们的工作，这次展示了一个基于块的设备如何能够推断出它上面的文件系统正在做什么，例如删除文件。其中使用的技术在块设备内实现了有趣的新功能，例如安全删除或更可靠的存储。

[WSG02]“Scale and Performance in the Denali Isolation Kernel”Andrew Whitaker, Marianne Shaw, and Steven D.Gribble OSDI ’02, Boston, Massachusetts介绍术语半虚拟化的论文。虽然人们可以争辩说Bugnion 等人[B+97]在Disco 论文中介绍了半虚拟化的概念，但Whitaker 等人进一步说明，这个想法的通用性如何超出以前的想象。

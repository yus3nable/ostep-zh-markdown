# E.7 调试

最后，在创建了良好的构建环境和正确编译的程序之后，你可能会发现程序有问题。解决问题的一种方法是认真思考——这种方法有时会成功，但往往不会。问题是缺乏信息。你只是不知道程序中到底发生了什么，因此无法弄清楚为什么它没有按预期运行。幸运的是，有某种帮助工具：gdb，GNU 调试器。

将以下错误代码保存在buggy.c 文件中，然后编译成可执行文件。

```c
#include <stdio.h>
struct Data {
    int x;
};
```

```c
int
main(int argc, char *argv[])
{
    struct Data *p = NULL;
    printf("%d\n", p->x);
}
```

在这个例子中，主程序在变量p 为NULL 时引用它，这将导致分段错误。当然，这个问题应该很容易通过检查来解决，但在更复杂的程序中，找到这样的问题并非总是那么容易。

要为调试会话做好准备，请重新编译程序，并确保将-g 标志加入每个编译行。这让可执行文件包含额外的调试信息，这些信息在调试会话期间非常有用。另外，不要打开优化（-O）。尽管这可能也行，但在调试过程中也可能导致困扰。

使用-g 重新编译后，你就可以使用调试器了。在命令提示符处启动gdb，如下所示：

```text
prompt> gdb buggy
```

这让你进入与调试器的交互式会话。请注意，你还可以使用调试器来检查在错误运行期间生成的“核心”文件，或者连上已在运行的程序。阅读文档以了解更多相关信息。

进入调试器后，你可能会看到以下内容：

```text
prompt> gdb buggy
GNU gdb ...
Copyright 2008 Free Software Foundation, Inc.
(gdb)
```

你可能想要做的第一件事就是继续运行程序。这只需在gdb 命令提示符下输入run。在这个例子中，你可能会看到：

```text
(gdb) run
Starting program: buggy
Program received signal SIGSEGV, Segmentation fault.
0x8048433 in main (argc=1, argv=0xbffff844) at buggy.cc:19
19         printf("%d\n", p->x);
```

从示例中可以看出，在这种情况下，gdb 会立即指出问题发生的位置。在我们尝试引用p 的行中产生了“分段错误”。这就意味着我们访问了一些我们不应该访问的内存。这时，精明的程序员可以检查代码，然后说“啊哈！肯定是p 没有指向任何有效的地址，因此不应该引用！”，然后继续修复该问题。

但是，如果你不知道发生了什么，可能想要检查一些变量。gdb 允许你在调试会话期间以交互方式执行此操作。

```c
(gdb) print p
1 = (Data *) 0x0
```

通过使用print 原语，我们可以检查p，并看到它是指向Data 类型结构的指针，并且它当前设置为NULL（即零，即十六进制零，此处显示为“0x0”）。

最后，你还可以在程序中设置断点，让调试器在某个函数中停止程序。执行此操作后，单步执行（一次一行），看看发生了什么，这通常很有用。

```c
(gdb) break main
Breakpoint 1 at 0x8048426: file buggy.cc, line 17.
(gdb) run
Starting program: /homes/hacker/buggy
```

```c
Breakpoint 1, main (argc=1, argv=0xbffff844) at buggy.cc:17
17           struct Data *p = NULL;
(gdb) next
19           printf("%d\n", p->x);
(gdb)
```

```text
Program received signal SIGSEGV, Segmentation fault.
0x8048433 in main (argc=1, argv=0xbffff844) at buggy.cc:19
19          printf("%d\n", p->x);
```

在上面的例子中，在main()函数中设置了断点。因此，当我们运行程序时，调试器几乎立即停止在main 执行。在示例中的该点处，发出“next”命令，它将执行下一行源代码级指令。“next”和“step”都是继续执行程序的有用方法——在文档中阅读，以获取更多详细信息[^p493-1]。

这里的讨论真的对gdb 不公平，它是丰富而灵活的调试工具，有许多功能，而不只是这里有限篇幅中描述的功能。在闲暇之余阅读更多相关信息，你将成为一名专家。

[^p493-1]: 特别是，你可以在使用gdb 进行调试时使用交互式的“help”命令。

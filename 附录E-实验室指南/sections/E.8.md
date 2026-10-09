# E.8 文档

要了解有关所有这些事情的更多信息，你必须做两件事：第一是使用这些工具；第二是自己阅读更多相关信息。了解更多关于gcc、gmake 和gdb 的一种方法是阅读它们的手册页。在命令提示符下输入man gcc、man gmake 或man gdb。你还可以使用man -k 在手册页中搜索关键字，但这并非总如人意。谷歌搜索可能是更好的方法。

关于手册页有一个棘手的事情：如果有多个名为×××的东西，输入man ×××可能不会得到你想要的东西。例如，如果你正在寻找kill()系统调用手册页，如果只是在提示符下键入man kill，会得到错误的手册页，因为有一个名为kill 的命令行程序。手册页分为几个部分（section），默认情况下，man 将返回找到的最低层部分的手册页，在本例中为第1部分。请注意，你可以通过查看页面的顶部来确定你看到的手册页：如果看到kill（2），就知道你在第2 节的正确手册页中，这里放的是系统调用。有关手册页的每个不同部分中存储的内容，请键入man man 以了解更多信息。另外请注意，man -a kill 可用于遍历名为“kill”的所有手册页。

手册页对于查找许多内容非常有用。特别是，你经常需要查找要传递给库调用的参数，或者需要包含哪些头文件才能使用库调用。所有这些都在手册页中提供。例如，如果查找open()系统调用，你会看到：

```c
SYNOPSIS
     #include <sys/types.h>
     #include <sys/stat.h>
     #include <fcntl.h>
     int open(const char *path, int oflag, /* mode_t mode */...);
```

这告诉你包含头文件sys/types.h、sys/stat.h 和fcntl.h，以便使用open 调用。它还告诉你要传递给open 的参数，即名为path 的字符串和整数标志oflag，以及指定文件模式的可选参数。如果你需要链接某个库以使用该调用，这里也会告诉你。

需要一些努力才能有效使用手册页。它们通常分为许多标准部分。主体将描述如何传递不同的参数，以使函数具有不同的行为。

一个特别有用的部分是手册页的RETURN VALUES 部分，它告诉你成功或失败时函数将返回什么。再次引用open()的手册页：

```text
RETURN VALUES
     Upon successful completion, the open() function opens the
     file and return a non-negative integer representing the
     lowest numbered unused file descriptor. Otherwise, -1 is
     returned, errno is set to indicate the error, and no files
     are created or modified.
```

因此，通过检查open 的返回值，你可以看到是否成功打开。如果没有，open（以及许多标准库函数）会将一个名为errno 的全局变量设置为一个值，来告诉你错误。有关更多详细信息，请参见手册页的ERRORS 部分。

你可能还想做一件事，即查找未在手册页本身中指定的结构的定义。例如，gettimeofday()的手册页有以下概要：

```c
SYNOPSIS
     #include <sys/time.h>
     int gettimeofday(struct timeval *restrict tp,
                      void *restrict tzp);
```

在这个页面中，你可以看到时间被放入timeval 类型的结构中，但是手册页可能不会告诉你这个结构有哪些字段！（在这个例子中，它包含在内，但你可能并非总是如此幸运）因此，你可能不得不寻找它。所有包含文件都位于/usr/include 目录下，因此你可以用grep 这样的工具来查找它。例如，你可以键入：

```c
prompt> grep ’struct timeval’ /usr/include/sys/*.h
```

这让你在/usr/include/sys 中以.h 结尾的所有文件中查找该结构的定义。遗憾的是，这可能不一定有效，因为包含文件可能包括在别处的其他文件。

更好的方法是使用你可以使用的工具，即编译器。编写一个包含头文件time.h 的程序，假设名为main.c。然后，使用编译器调用预处理器，而不是编译它。预处理器处理文件中的所有指令，例如#define 指令和#include 指令。为此，请键入gcc -E main.c。结果是一个C 文件，其中包含所有需要的结构和原型，包括timeval 结构的定义。

可能还有找到这些东西的更好方法：google。你应该总是google 那些你不了解的东西——只要通过查找就可以学到很多东西，这令人惊奇！

## info 页面

info 页面在寻找文档方面也非常有用，它为许多GNU 工具提供了更详细的文档。你可以通过运行info 程序或通过emacs（黑客的首选编辑器）执行Meta-x info 来访问info 页面。像gcc 这样的程序有数百个标志，其中一些标志非常有用。gmake 还有许多功能可以改善你的构建环境。最后，gdb 是一个非常复杂的调试器。阅读man 和info 页面，尝试以前没有尝试过的功能，成为编程工具的强大用户。

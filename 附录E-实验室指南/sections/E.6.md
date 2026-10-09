# E.6 Makefile 文件

程序make 让你自动化大部分构建过程，因此对于任何认真的程序（和程序员）来说，都是一个至关重要的工具。来看一个简单的例子，它保存在名为Makefile 的文件。

要构建程序，只需输入：

```text
prompt> make
```

这会（默认）查找Makefile 或makefile，将其作为输入（你可以用标志指定不同的makefile，阅读手册页，找出是哪个标志）。gmake 是make 的gnu 版本，比传统的make 功能更多，所以我们将在下面的部分中重点介绍它（尽管我们互换使用这两个词）。这些讨论大多数都基于gmake 的info 页面，要了解如何查找这些页面，请参阅“E.8 文档”部分。另外请注意：在Linux 系统上，gmake 和make 是一样的。

```text
hw: hw.o helper.o
    gcc -o hw hw.o helper.o -lm
```

```text
hw.o: hw.c
    gcc -O -Wall -c hw.c
```

```text
helper.o: helper.c
    gcc -O -Wall -c helper.c
```

```text
clean:
    rm -f hw.o helper.o hw
```

Makefile 基于规则，这些规则决定需要发生的事情。规则的一般形式是：

```text
target: prerequisite1 prerequisite2 ...
    command1
    command2
    ...
```

target（目标）通常是程序生成的文件的名称。目标的例子是可执行文件或目标文件。目标也可以是要执行的操作的名称，例如在我们的示例中为“clean”。

prerequisite（先决条件）是用于生成目标的输入文件。目标通常依赖于几个文件。例如，要构建可执行文件hw，需要首先构建两个目标文件：hw.o 和helper.o。

最后，command（命令）是一个执行的动作。一条规则可能有多个命令，每个命令都在自己的行上。重要提示：必须在每个命令行的开头放一个制表符！如果你只放空格，make会打印出一些含糊的错误信息并退出。

通常，命令在具有先决条件的规则中，如果任何先决条件发生更改，就要重新创建目标文件。但是，为目标指定命令的规则不需要先决条件。例如，包含delete 命令、与目标“clean”相关的规则中，没有先决条件。

回到我们的例子，在执行make 时，大致工作如下：首先，看到目标hw，并且意识到要构建它，它必须具备两个先决条件，hw.o 和helper.o。因此，hw 依赖于这两个目标文件。然后，Make 将检查每个目标。在检查hw.o 时，看到它取决于hw.c。这是关键：如果hw.c最近被修改，但hw.o 没有被创建，make 会知道hw.o 已经过时，应该重新生成。在这种情况下，会执行命令行gcc -O -Wall -c hw.c，生成hw.o。因此，如果你正在编译大型程序，make会知道哪些目标文件需要根据其依赖项重新生成，并且只会执行必要的工作来重新创建可执行文件。另外请注意，如果hw.o 根本不存在，也会被创建。

继续，基于上面定义的相同标准，helper.o 也会重新生成或创建。当两个目标文件都已创建时，make 现在可以执行命令来创建最终的可执行文件，然后返回并执行以下操作：gcc-o hw hw.o helper.o -lm。

到目前为止，我们一直没提makefile 中的clean 目标。

要使用它，必须明确提出要求，键入以下代码：

```text
prompt> make clean
```

这会在命令行上执行该命令。因为clean 目标没有先决条件，所以输入make clean 将导致命令被执行。在这种情况下，clean 目标用于删除目标文件和可执行文件，如果你希望从头开始重建整个程序，就非常方便。

现在你可能会想，“好吧，这似乎没问题，但这些makefile 确实很麻烦！”你说得对——如果它们总是这样写的话。幸运的是，有很多快捷方式，让使用更容易。例如，这个makefile具有相同的功能，但用起来更好：

```text
# specify all source files here
SRCS = hw.c helper.c
# specify target here (name of executable)
TARG = hw
# specify compiler, compile flags, and needed libs
CC = gcc
OPTS = -Wall -O
LIBS = -lm
# this translates .c files in src list to .o’s
OBJS = $(SRCS:.c=.o)
# all is not really needed, but is used to generate the target
all: $(TARG)
# this generates the target executable
$(TARG): $(OBJS)
    $(CC) -o $(TARG) $(OBJS) $(LIBS)
# this is a generic rule for .o files
%.o: %.c
    $(CC) $(OPTS) -c $< -o $@
# and finally, a clean line
clean:
    rm -f $(OBJS) $(TARG)
```

虽然我们不会详细介绍make 语法，但如你所见，这个makefile 可以让生活更轻松一些。例如，它允许你轻松地将新的源文件添加到构建中，只需将它们加入makefile 顶部的SRCS变量即可。你还可以通过更改TARG 行轻松更改可执行文件的名称，并且可以轻松修改指定编译器，标志和库。

关于make 的最后一句话：找出目标的先决条件并非总是很容易，特别是在大型复杂程序中。毫不奇怪，有另一种工具可以帮助解决这个问题，称为makedepend。自己阅读它，看看是否可以将它合并到一个makefile 中。

# E.1 一个简单的C 程序

我们从一个简单的C 程序开始，它保存在文件“hw.c”中。与Java 不同，文件名和文件内容之间不一定有关系。因此，请以适当的方式，利用你的常识来命名文件。

第一行指定要包含的文件，在本例中为stdio.h，它包含许多常用输入/输出函数的“原型”。我们感兴趣的是printf()。当你使用#include 指令时，就告诉C 预处理器（cpp）查找特定文件（例如，stdio.h），并将其直接插入到#include 的代码中。默认情况下，cpp 将查看目录/usr/include/，尝试查找该文件。

下面一部分指定main()函数的签名，即它返回一个整数（int），并用两个参数来调用，一个整数argc，它是命令行上参数数量的计数。一个指向字符（argv）的指针数组，每个指针都包含命令行中的一个单词，最后一个单词为null。下面的指针和数组会更多。

```c
/* header files go up here */
/* note that C comments are enclosed within a slash and a star, and
   may wrap over lines */
// if you use gcc, two slashes will work too (and may be preferred)
#include <stdio.h>
/* main returns an integer */
int main(int argc, char *argv[]) {
    /* printf is our output function;
       by default, writes to standard out */
    /* printf returns an integer, but we ignore that */
    printf("hello, world\n");
    /* return 0 to indicate all went well */
    return(0);
}
```

程序然后简单打印字符串“hello，world”，并将输出流换到下一行，这是由printf()调用结束时的“\\n”实现的。然后，程序返回一个值并结束，该值被传递回执行程序的shell。终端上的脚本或用户可以检查此值（在csh 和tcsh shell 中，它存储在状态变量中），以查看程序是干净地退出还是出错。

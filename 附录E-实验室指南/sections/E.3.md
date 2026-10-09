# E.3 有用的标志

在继续使用C 语言之前，我们首先指出一些有用的gcc 编译标志。

```text
prompt> gcc -o hw hw.c # -o: to specify the executable name
prompt> gcc -Wall hw.c # -Wall: gives much better warnings
prompt> gcc -g hw.c     # -g: to enable debugging with gdb
prompt> gcc -O hw.c     # -O: to turn on optimization
```

当然，你可以根据需要组合这些标志（例如gcc -o hw -g -Wall hw.c）。在这些标志中，你应该总是使用-Wall，这会提供很多关于可能出错的额外警告。不要忽视警告！相反，要修复它们，让它们幸福地消失。

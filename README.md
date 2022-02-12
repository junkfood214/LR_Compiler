# 西电编译原理实验——函数绘图语言解释器

> 西安电子科技大学 软件工程 编译原理大作业 使用LR(1)文法完成的编译器

### 文件组成

1. LR(1).json为LR(1)文法所需的预测分析表(程序读取)
2. lexer.py为词法分析器
3. myParser.py为语法分析器
4. output.txt、output1.txt、test1.txt均为矩阵方式储存的预测分析表(debug使用)
5. painter为绘图器
6. read.py作用为读取预测分析表

---



### 题目要求

通过做上机题加深对编译器构造原理和方法的理解，巩固所学知识。

1. 会用正规式设计简单语言的词法；

2. 会用产生式设计简单语言的语法；

3. ~~会用递归下降子程序编写语言的解释器~~。LR(1)编写解释器

---



#### 函数绘图语言

##### 5 种语句

- 循环绘图（FOR-DRAW）

- 比例设置（SCALE）

- 角度旋转（ROT）

- 坐标平移（ORIGIN）

- 注释    （-- 或 //）

##### example

**函数f(t)=t的图形**

```
origin is (100, 300);	-- 设置原点的偏移量
rot is 0;			-- 设置旋转角度(不旋转)
scale is (1, 1);		-- 设置横坐标和纵坐标的比例
for T from 0 to 200 step 1 draw (t, 0);
				-- 横坐标的轨迹（纵坐标为0）
for T from 0 to 150 step 1 draw (0, -t);
				-- 纵坐标的轨迹（横坐标为0）
for T from 0 to 120 step 1 draw (t, -t);
				-- 函数f(t)=t的轨迹 
```

**默认值**

```
origin is (0, 0); 
rot is 0;
scale is (1, 1);
```
---
##规约产生式

0. B->P
1. A->c
2. A->t
3. A->u(E)
4. A->(E)
5. C->A@C
6. C->A
7. E->E+T
8. E->E-T
9. E->T
10. F->ftaEbEcEd(E,E)
11. G->+G
12. G->-G
13. G->C
14. O->op(E,E)
15. P->S;P
16. P->
17. R->rpE
18. S->qp(E,E)
19. S->U
20. S->R
21. S->F
22. S->O
23. T->T*G
24. T->T/G
25. T->G


# 20220508


## 加花比较
源程序 `start` 函数与加花后 `start` 函数比较

### 源程序:
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511161508.png)

### 小T个人加花
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511161655.png)

### 木马免疫器加花
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511162012.png)

### 木马彩衣 添加了名为 hnxyy 的新节并将start函数移至该处
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511162316.png)

### 花指令添加器 添加段KK并移动start到此处
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511162522.png)


### 超级加花器 添加新节 mmyym520 移动函数入口点到此处
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511162822.png)

## 去花脚本使用

**去花前**
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511165430.png)

**去花后**
![](https://raw.githubusercontent.com/CynosureSec/Imagebed/main/img/20220511165723.png)



# 去花脚本
```C
#include <idc.idc>
static matchBytes(StartAddr, Match) 
{ 
auto Len, i, PatSub, SrcSub; 
Len = strlen(Match);

while (i < Len) 
{ 
   PatSub = substr(Match, i, i+1); 
   SrcSub = form("%02X", Byte(StartAddr)); 
   SrcSub = substr(SrcSub, i % 2, (i % 2) + 1); 
   
   if (PatSub != "?" && PatSub != SrcSub) 
   { 
    return 0; 
   } 
   
   if (i % 2 == 1) 
   { 
    StartAddr++; 
   } 
   i++; 
}
return 1; 
}
static main() 
{ 
   auto Addr, Start, End, Condition, junk_len, i;
Start = 0x740; 
End = 0x7f3;
Condition = "740A7508E810000000EB04E8";
junk_len = 12;
for (Addr = Start; Addr < End; Addr++) 
{ 
   if (matchBytes(Addr, Condition)) 
   { 
    for (i = 0; i < junk_len; i++) 
    {
     PatchByte(Addr, 0x90); 
     MakeCode(Addr); 
     Addr++; 
    } 
   } 
}
AnalyzeArea(Start, End); 
Message("Clear Fake-Jmp Opcode Ok "); 
} 

```


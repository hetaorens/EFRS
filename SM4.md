```mermaid
graph TB
subgraph SM4加密算法
    A[开始]
    B[轮密钥生成]
    C[初始轮]
    D[加密轮]
    E[最终轮]
    F[输出密文]
    G[结束]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
end
```
```bash
在上述流程图中，SM4加密算法的主要流程包括以下几个步骤：

轮密钥生成：生成轮密钥用于加密过程。
初始轮：对明文进行初始处理，包括异或轮密钥和置换操作。
加密轮：执行多轮的加密操作，包括字节替代、行移位、列混合和轮密钥的异或操作。
最终轮：执行最后一轮的加密操作，不包括列混合。
输出密文：输出加密后的密文结果。
结束：结束加密算法流程。
请注意，SM4加密算法还涉及到解密过程，该流程图仅展示了加密算法的主要流程。
```


```mermaid
graph TB
subgraph 轮密钥生成
    A[开始]
    B[输入主密钥]
    C[密钥扩展]
    D[设置轮密钥变量]
    E[循环1-32]
    F[字节代换]
    G[行移位]
    H[列混合]
    I[轮密钥异或]
    J[输出轮密钥]
    K[结束]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> E
    E --> J
    J --> K
end
```
```bash
在上述流程图中，详细展示了SM4加密算法中轮密钥生成的流程。具体流程如下：

输入主密钥：接收输入的主密钥。
密钥扩展：对主密钥进行扩展，生成轮密钥所需的扩展密钥。
设置轮密钥变量：初始化轮密钥的变量，包括轮密钥W和轮常量FK。
循环1-32：进行32轮的密钥生成操作。
字节代换：对轮密钥的一部分进行字节代换操作。
行移位：对轮密钥的一部分进行行移位操作。
列混合：对轮密钥的一部分进行列混合操作。
轮密钥异或：将扩展密钥与轮常量FK进行异或，得到轮密钥的一部分。
输出轮密钥：输出生成的轮密钥。
结束：结束轮密钥生成的流程。
这个流程图更加详细地展示了SM4加密算法中轮密钥生成部分的流程，包括了具体的操作步骤和循环过程。
```

```mermaid
graph TB
subgraph 初始轮
    A[开始]
    B[输入明文块]
    C[初始轮密钥异或]
    D[轮函数运算]
    E[输出中间结果]
    F[结束]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
end
```
```mermaid
graph TB
subgraph 最终轮
    G[开始]
    H[输入中间结果]
    I[轮函数运算]
    J[最终轮密钥异或]
    K[输出密文块]
    L[结束]

    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
end
```
```bash

初始轮的主要流程包括以下几个步骤：

输入明文块：接收输入的明文块。
初始轮密钥异或：将初始轮密钥与明文块进行异或操作。
轮函数运算：使用轮函数对异或结果进行运算。
输出中间结果：输出初始轮的中间结果。
结束：结束初始轮的流程。
最终轮的主要流程包括以下几个步骤：

开始：最终轮的开始节点。
输入中间结果：接收初始轮输出的中间结果。
轮函数运算：使用轮函数对中间结果进行运算。
最终轮密钥异或：将最终轮密钥与轮函数运算结果进行异或操作。
输出密文块：输出加密后的密文块。
结束：结束最终轮的流程。
```


加密轮

```mermaid
graph TB
subgraph SM4加密轮
    A[开始]
    B[输入明文块]
    C[轮密钥异或]
    D[轮函数运算]
    E[输出密文块]
    F[结束]

    style A fill:#F9F9F9,stroke:#333,stroke-width:2px
    style F fill:#F9F9F9,stroke:#333,stroke-width:2px
   
    style C stroke-dasharray: 5,5
    style D stroke-dasharray: 5,5

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
end
```

```mermaid
graph TB
subgraph SM4扩展轮函数
    A[开始]
    B[输入32位字]
    C[循环左移]
    D[S盒替换]
    E[R轮运算]
    F[输出32位字]
    G[结束]

    style A fill:#F9F9F9,stroke:#333,stroke-width:2px
    style G fill:#F9F9F9,stroke:#333,stroke-width:2px
    style C stroke-dasharray: 5,5
    style D stroke-dasharray: 5,5

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
end

```


```mermaid
graph BT

subgraph SM4加密轮
    A[开始]
    B[输入明文块]
    C[轮密钥异或]
    D[扩展轮函数]
    E[轮函数运算]
    F[输出密文块]
    G[结束]

    style A fill:#F9F9F9,stroke:#333,stroke-width:2px
    style G fill:#F9F9F9,stroke:#333,stroke-width:2px
    style C stroke-dasharray: 5,5
    style D stroke-dasharray: 5,5

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
end

subgraph SM4扩展轮函数
    H[扩展轮函数]
    I[输入32位字]
    J[循环左移]
    K[S盒替换]
    L[R轮运算]
    M[输出32位字]
    N[结束]

    style H fill:#F9F9F9,stroke:#333,stroke-width:2px
    style N fill:#F9F9F9,stroke:#333,stroke-width:2px

    style J stroke-dasharray: 5,5
    style K stroke-dasharray: 5,5

    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
end

C --> H
E --> L

```
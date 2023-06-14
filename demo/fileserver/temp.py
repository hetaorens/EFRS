def get_prime_numbers(n):
    prime_numbers = []
    
    # 遍历范围内的每个数字
    for num in range(2, n + 1):
        is_prime = True
        
        # 检查是否有因子能整除该数字
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # 如果没有因子能整除该数字，则它是质数
        if is_prime:
            prime_numbers.append(num)
    
    return prime_numbers

# 示例调用
while True:
    try:
        n=int(input("请输入数字："))
        primes = get_prime_numbers(n)
        print("在1到", n, "之间的质数：", primes)  
    except:
        break
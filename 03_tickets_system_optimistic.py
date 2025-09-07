import threading
import time
import atomics

tickets = 20  # 剩余票数
tickets_version = atomics.atomic(width=4, atype=atomics.INT,) # 剩余票数版本号
tickets_version.store(0) # 初始值为0
success_count = 0  # 成功购票人数计数器

def buy_ticket(user_id):
    global tickets,tickets_version,success_count
    # 乐观锁重试机制
    buyCount = 0
    while tickets > 0:
        tmp_tickets_version = tickets_version.load()
        buyCount += 1
        time.sleep(0.1) # （关键）购票时长，并发主要发生才此处
        cmpxchgResult = tickets_version.cmpxchg_strong(tmp_tickets_version,tmp_tickets_version+1)
        if cmpxchgResult.success:
            tickets -= 1
            success_count += 1
            print(f"用户 {user_id} 抢票成功！剩余票数: {tickets}")
            return
        else:
            print(f"抢票人数过多，用户 {user_id} 正在第{buyCount}次尝试...")
    print(f"用户 {user_id} 抢票失败，票已售罄！")       

if __name__ == "__main__":
    threads = []
    for i in range(1000):
        t = threading.Thread(target=buy_ticket, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"\n最终剩余票数: {tickets}")
    print(f"成功购票人数: {success_count}")
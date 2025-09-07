import threading
import time

tickets = 20  # 剩余票数
success_count = 0  # 成功购票人数计数器

lock = threading.Lock()

def buy_ticket(user_id):
    global tickets,success_count
    with lock:
        if tickets > 0:
            time.sleep(0.1) # （关键）购票时长，并发主要发生才此处
            tickets -= 1
            success_count += 1
            print(f"用户 {user_id} 抢票成功！剩余票数: {tickets}")
        else:
            print(f"用户 {user_id} 抢票失败")


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
from multiprocessing import Manager, Process  
  
class SharedData:  
    def __init__(self):  
        self.value = 0  
  
    def increment(self):  
        self.value += 1  
  
def worker_with_closure(shared_data, num_increments):  
    def worker():  
        nonlocal shared_data, num_increments  
        for _ in range(num_increments):  
            shared_data.increment()  
    # 在这里，worker是一个闭包函数，它引用了外部的shared_data实例  
    worker()  
  
if __name__ == "__main__":  
    with Manager() as manager:  
        # 使用Manager的dict()方法创建一个可以在进程间共享的字典  
        # 我们可以将类的实例作为字典的值来共享  
        shared_dict = manager.dict()  
        shared_data = SharedData()  
        shared_dict["data"] = shared_data  
  
        # 创建多个进程，每个进程都会增加shared_data的value  
        processes = []  
        for _ in range(5):  
            p = Process(target=worker_with_closure, args=(shared_dict["data"], 2))  
            processes.append(p)  
            p.start()  
  
        # 等待所有进程完成  
        for p in processes:  
            p.join()  
  
        # 检查结果  
        print(shared_dict["data"].value)  # 应该输出 10，因为每个进程都增加了2次

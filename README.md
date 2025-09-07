# python_concurrent_sample
python并发示例代码，悲观锁、乐观锁示例

```python
# 本工程的python版本为3.13.3，其中乐观锁依赖了atomics库来支持原子操作，需要安装
pip install atomics
```

以“售票系统”的资源冲突为例
示例代码：01为无并发处理，02为悲观锁，03为乐观锁

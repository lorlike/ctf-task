# ctf-task
用于部署ctf远程题目的docker环境

## crypto

### python

```bash
# 制作docker镜像
cd crypto4python
docker build -t crypto4python .

# 启动docker容器，对外端口为10000，容器名字是task-test
docker run -d --name task-test -p 10000:19132 crypto4python
```


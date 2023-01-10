# fastGithub
简化CDN加速访问github流程，只需要执行main.py文件，即可自动完成相关步骤  
## CDN加速访问github操作流程
1. 访问[ipaddress](https://www.ipaddress.com/)
2. 查询下列三个链接的DNS解析地址
    1. github.com  
    2. assets-cdn.github.com
    3. github.global.ssl.fastly.net  
3. 接着,打开系统hosts文件(需管理员权限)。路径：C:\Windows\System32\drivers\etc  
4. 添加三行记录并保存
```
140.82.113.3    github.com
185.199.108.153 assets-cdn.github.com
199.232.69.194  github.global.ssl.fastly.net
```
5. 刷新系统DNS缓存
```
Windows+X 打开系统命令行（管理员身份）或powershell
运行 ipconfig /flushdns 手动刷新系统DNS缓存。
```
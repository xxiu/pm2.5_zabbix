pm2.5 zabbix 监控
-----------------



文件
--------  
1. pm2.5.py 用来获取pm值  
2. zabbix-pm25.conf 配置 zabbix 的 UserParameter  

github: https://github.com/xxiu/pm2.5_zabbix

配置
---------------
我的 zabbix 配置文件目录在 `/usr/local/etc`
将 pm2.5.py 拷贝到/usr/local/etc/zabbix_agentd.conf.d
将 zabbix-pm25.conf 拷贝到 /usr/local/etc/script
重启 zabbix-agentd

可以在zabbix-server上测试一下配置是否成功
```
zabbix_get -s IP -p 10050 -k 'pm25[beijing]'
```

触发器
---------------
添加一个项目 pm25_beijing 键值为 pm25[beijing]
添加一个图像来监控这个项目的走势 
添加3个触发器，表达式如下，用来监控pm2.5超过100，200，350的变化，过了350的感觉就生无可恋了。
{pm25:pm25[beijing].last()}>100 
{pm25:pm25[beijing].last()}>200 
{pm25:pm25[beijing].last()}>350


告警
----------------
action 那里已经配置了全局的告警，就不需要配置了。
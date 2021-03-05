# NUIST-Internet
南京信息工程大学校园网认证自动化
  
  使用POST将用户名（username) 网络运营商（domain） 密码（password）直接上传到：http://a.nuist.edu.cn/index.php/index/login
  使用config1.txt是否存在来判断是否为首次运行
  所有配置保存在config.txt内
  因为C盘需要管理员权限，而程序依靠bat来实现开机自启动，所以无法在管理员身份下同时运行bat和exe本体程序，所以只好将配置文件保存在c盘
  稍后将在exe本体中集成开机自启动模块，无D盘的同学也可以使用
  

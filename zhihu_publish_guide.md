# 知乎文章发布完整指南

## 任务概述
目标：将文章自动发布到知乎平台

## 当前状态分析
- OpenClaw网关已启动并运行
- 浏览器控制服务已就绪
- Chrome扩展已安装但无标签页连接

## 第一步：建立浏览器连接
1. 打开Chrome浏览器
2. 访问任意网页（如百度、知乎等）
3. 点击地址栏右侧的OpenClaw扩展图标
4. 确认标签页已被扩展接管（图标会变色或显示状态）

## 第二步：编写发布脚本
以下是用于发布知乎文章的Python代码示例：

```python
from openclaw import browser
import time

def publish_to_zhihu(title, content, username, password):
    """
    发布文章到知乎
    """
    try:
        # 连接到已连接的浏览器标签页
        print("连接到浏览器...")
        
        # 导航到知乎登录页面
        browser.navigate("https://www.zhihu.com/signin")
        
        # 如果未登录，则进行登录
        time.sleep(2)
        
        # 输入用户名
        browser.fill("#username", username)
        
        # 输入密码
        browser.fill("#password", password)
        
        # 点击登录按钮
        browser.click("button[type='submit']")
        
        time.sleep(3)
        
        # 导航到创作中心
        browser.navigate("https://zhuanlan.zhihu.com/write")
        
        time.sleep(2)
        
        # 填写标题
        title_element = browser.find_element("input[placeholder='请输入标题']")
        title_element.send_keys(title)
        
        # 填写内容
        content_element = browser.find_element(".CodeMirror textarea")
        content_element.send_keys(content)
        
        # 发布文章
        publish_button = browser.find_element("button:contains('发布')")
        publish_button.click()
        
        print("文章已成功发布到知乎！")
        
    except Exception as e:
        print(f"发布过程中出现错误: {str(e)}")

# 使用示例
if __name__ == "__main__":
    title = "文章标题"
    content = "这里是文章的详细内容..."
    username = "你的知乎用户名"
    password = "你的知乎密码"
    
    publish_to_zhihu(title, content, username, password)
```

## 第三步：使用Browser Agent技能发布内容

如果使用OpenClaw的browser-agent技能，可以这样操作：

```json
{
  "skill": "browser-agent",
  "action": "fillForm",
  "url": "https://www.zhihu.com/signin",
  "fields": {
    "#username": "your_username",
    "#password": "your_password"
  },
  "submit": "button[type='submit']"
}
```

## 第四步：实际执行步骤

1. 确保Chrome扩展已连接标签页
2. 准备好要发布的文章标题和内容
3. 知乎账户凭据（用户名/邮箱和密码）
4. 运行自动化脚本
5. 监控发布过程并处理可能出现的验证码等安全验证

## 注意事项
- 知乎可能有反爬虫机制，需要适当延时
- 可能需要处理人机验证（如滑块验证、图形验证码等）
- 确保文章内容符合知乎社区规范
- 避免频繁发布，以免被限制账号功能

## 备用方案
如果自动化发布遇到困难，可以考虑：
1. 使用知乎官方API（如果有）
2. 通过复制粘贴方式手动发布
3. 使用第三方内容管理工具
import zmail
#邮箱地址和密码或者授权码
server = zmail.server('342976175@qq.com', 'wkgubhkismgpcabe')



with open('C:\\Users\\v_bingbqi\\PycharmProjects\\untitled\\demo\\zdh_lx\\baidu_report\\baidu_test.html',buffering=1024,encoding='utf-8') as f:
    con=f.read()

mail_content={
    "subject":"测试主题",#主题
    "content_html":con,#内容
    "attachments":"C:\\Users\\v_bingbqi\\PycharmProjects\\untitled\\demo\\zdh_lx\\baidu_report\\baidu_test.html"
}
server.send_mail(['342976175@qq.com','qbbeibing@gmail.com'],mail_content)
# Retrieve mail
latest_mail = server.get_latest()
zmail.show(latest_mail)
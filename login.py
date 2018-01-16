import itchat
from itchat.content import TEXT

if itchat.load_login_status():  # itchat.load_login_status() 用于读取设置
    @itchat.msg_register(TEXT)
    def simple_reply(msg):
        print(msg["Text"])

    itchat.run()
    itchat.dump_login_status()  # itchat.dump_login_status() 用于导出设置

else:
    itchat.auto_login()
    itchat.dump_login_status()
    print("Config stored, so exit.")
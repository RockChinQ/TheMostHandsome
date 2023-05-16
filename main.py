from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

from mirai import At

"""
在收到私聊或群聊消息"hello"时，回复"hello, <发送者id>!"或"hello, everyone!"
"""


# 注册插件
@register(name="TheMostHandsome", description="群里说 世界上最帅的人是谁", version="0.1", author="RockChinQ")
class HandsomePlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    # 当收到群消息时触发
    @on(GroupMessageReceived)
    def group_normal_message_received(self, event: EventContext, host: PluginHost, **kwargs):
        msg = str(kwargs['message_chain'])
        if msg == "世界上最帅的人是谁":

            # 输出调试信息
            logging.info("{} is the most handsome one.".format(kwargs['sender_id']))

            # event.add_return("reply", [At(target=kwargs['sender_id'])])

            host.send_group_message(kwargs['launcher_id'], ["最帅的人是：", At(target=kwargs['sender_id']), "!"])

            # 阻止该事件默认行为（向接口获取回复）
            event.prevent_default()
            event.prevent_postorder()

    # 插件卸载时触发
    def __del__(self):
        pass

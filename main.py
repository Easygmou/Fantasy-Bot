from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("Fantasy-Bot", "1mWan", "一个简单的 Fantasy-Bot 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 verify。注册成功后，发送 `/verify` 就会触发这个指令，并post请求body为发送人qq号访问https://127.0.0.1:10001/bot/verify
    @filter.command("verify")
    async def verify(self, event: AstrMessageEvent):
        """这是一个 verify 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        # 判断qq群聊是否为1084990390
        if event.get_group_id() != 1084990390:
            return
        user_id = event.get_sender_id()
        logger.info(f"verify {user_id}")
        # 发送post请求
        import requests
        url = "https://127.0.0.1:10001/bot/verify"
        data = {"qq": user_id}
        response = requests.post(url, json=data)
        logger.info(response.text)
        # 解析json
        import json
        data = json.loads(response.text)
        # 回复消息
        yield event.plain_result(data["message"])

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""

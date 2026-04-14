from random import randint

from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register
from astrbot.core.star.filter.event_message_type import EventMessageType


@register("astrbot_plugin_henan_ongeki", "诶嘿怪awa", "一个简单的河南音击插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.command("河南音击", alias={"河南音擊"})
    async def hello(self, event: AstrMessageEvent):
        """随机河南音击"""
        yield event.image_result(f"data/plugins/{self.name}/image/{str(randint(1, 44))}.jpg")

    @filter.event_message_type(EventMessageType.ALL)
    async def henan_ongeki_no_slash(self, event: AstrMessageEvent):
        """当消息中包含“河南音击”但不以“/”开头时触发"""
        msg= event.message_str.strip() # 去除消息两端的空白字符
        commands={"河南音击", "河南音擊" }
        if msg in commands:
            yield event.image_result(f"data/plugins/{self.name}/image/{str(randint(1, 44))}.jpg")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""

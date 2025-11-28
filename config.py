import os

#配置类
class Config:
    # 类属性，默认配置
    SONG_PATH = "./data/songs.json"
    ALIAS_PATH = "./data/alias.json"
    COVER_URL = "https://reiwa.f5.si/jackets/chunithm/"
    ID2NAME_PATH = "./data/chartId2Name.json"
    ID2GEN_PATH = "./data/chartId2Gen.json"
    ID2DIFF_WE_PATH = "./data/chartId2Diff_we.json"
    SEGA_SONG_PATH = "./data/data_new.json"
    SEGA_COVER_URL = "https://new.chunithm-net.com/chuni-mobile/html/mobile/img/"
    CHART_URL = "https://sdvx.in/chunithm/<gen>/obj/data<chartid>mst.png"
    CHART_BG_URL = "https://sdvx.in/chunithm/<gen>/bg/<chartid>bg.png"
    CHART_BAR_URL = "https://sdvx.in/chunithm/<gen>/bg/<chartid>bar.png"
    BOT_QQ = "2537971097"

    #插件数据路径
    DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"../plugin_data/astrbot_plugin_chunithm_util/"))

    @classmethod
    def update_from_dict(cls, config_dict:dict):
        """从字典更新类属性"""
        for key, value in config_dict.items():
            if hasattr(cls, key):
                setattr(cls, key, str(value))

    @classmethod
    def get(cls, key, default=None):
        """获取类属性，如果不存在返回默认值"""
        return getattr(cls, key, default)

    @classmethod
    def set(cls, key, value):
        """设置类属性"""
        setattr(cls, key, str(value))

    @classmethod
    def to_dict(cls):
        """将类属性转换为字典"""
        # 获取所有不以双下划线开头的类属性
        return {key: getattr(cls, key) for key in dir(cls) 
                if not key.startswith('_') and not callable(getattr(cls, key)) and key.isupper()}

    @classmethod
    def __str__(cls):
        """字符串表示，便于调试"""
        return str(cls.to_dict())

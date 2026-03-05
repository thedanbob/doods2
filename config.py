from typing import List, Optional, Union
from pydantic_settings import BaseSettings, SettingsConfigDict

class DoodsDetectorConfig(BaseSettings):
    name: str
    type: str
    modelFile: str
    labelFile: Optional[str]
    labelsStartFromZero: Optional[bool] = False
    hwAccel: Optional[bool] = False
    numThreads: Optional[int] = 2

class DoodsBoxesConfig(BaseSettings):
    enabled: Optional[bool] = True
    boxColor: Optional[Union[List[int], str]] = [0, 255, 0]
    boxThickness: Optional[int] = 1
    fontScale: Optional[float] = 1.2
    fontColor: Optional[Union[List[int], str]] = [0, 255, 0]
    fontThickness: Optional[int] = 2

class DoodsRegionsConfig(BaseSettings):
    enabled: Optional[bool] = True
    boxColor: Optional[Union[List[int], str]] = [0, 255, 0]
    boxThickness: Optional[int] = 1
    fontScale: Optional[float] = 1.2
    fontColor: Optional[Union[List[int], str]] = [0, 255, 0]
    fontThickness: Optional[int] = 2

class DoodsGlobalsConfig(BaseSettings):
    enabled: Optional[bool] = True
    fontScale: Optional[float] = 1.2
    fontColor: Optional[Union[List[int], str]] = [0, 255, 0]
    fontThickness: Optional[int] = 2

class DoodsConfig(BaseSettings):
    boxes: Optional[DoodsBoxesConfig] = DoodsBoxesConfig()
    regions: Optional[DoodsRegionsConfig] = DoodsRegionsConfig()
    globals: Optional[DoodsGlobalsConfig] = DoodsGlobalsConfig()
    detectors: List[DoodsDetectorConfig]
    log: Optional[str] = 'detections'
    model_config = SettingsConfigDict(
        env_prefix = 'doods_'
    )

class LoggerConfig(BaseSettings):
    level: str = "info"
    model_config = SettingsConfigDict(
        env_prefix = 'logger_'
    )

class ServerConfig(BaseSettings):
    host: Optional[str] = "0.0.0.0"
    port: Optional[int] = 8080
    auth_key: Optional[str] = ''
    trace: Optional[bool] = False
    model_config = SettingsConfigDict(
        env_prefix = 'server_'
    )

class Config(BaseSettings):
    logger: LoggerConfig = LoggerConfig()
    server: Optional[ServerConfig] = ServerConfig()
    doods: DoodsConfig

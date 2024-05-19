
from dataclasses import dataclass
from aiohttp import ClientSession
from json import dumps


class ApiException(Exception):
    pass

@dataclass
class HozoryTranslateResult(Base):
    translated_text: str
    translation_language: str
    voice_link: str

    @staticmethod
    def parse(d: dict, dest: str) -> "HozoryTranslateResult":
        return HozoryTranslateResult(
            translated_text=d["translate"],
            translation_language=dest,
            voice_link=d["Voice_link"],
        )


class AsyncHozoryTranslator:
    def __init__(self) -> None:
        pass

    async def translate(self, text: str, dest: str = "en") -> "HozoryTranslateResult":
        async with ClientSession() as session:
            async with session.get(
                f"https://hozory.com/translate/?target={dest}&text={text}"
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if not result["status"] == "ok":
                    raise ApiException(
                        dumps(result["result"], indent=2, ensure_ascii=False)
                    )

                return HozoryTranslateResult.parse(result["result"], dest)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self

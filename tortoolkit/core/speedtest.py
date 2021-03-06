import logging

from speedtest import Speedtest

from ..functions.Human_Format import human_readable_bytes

torlog = logging.getLogger(__name__)


async def get_speed(message):
    imspd = await message.reply("β±πΏπππππππππ πππππππππ...")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    (result["share"])
    string_speed = f"""
β±**__κ±α΄α΄α΄α΄α΄α΄κ±α΄ Κα΄κ±α΄Κα΄...__**

π±**Server Name:** `{result["server"]["name"]}`
π**Country:** `{result["server"]["country"]}, {result["server"]["cc"]}`
π¨π»βπΌ**Sponsor:** `{result["server"]["sponsor"]}`
π€**Upload:** `{human_readable_bytes(result["upload"] / 8)}/s`
π₯**Download:** `{human_readable_bytes(result["download"] / 8)}/s`
π‘**Ping:** `{result["ping"]} ms`
π§π»βπ»**ISP:** `{result["client"]["isp"]}`
"""
    await imspd.delete()
    await message.reply(string_speed, parse_mode="markdown")
    torlog.info(
        f'<b>πͺκ±α΄Κα΄ α΄Κ κ±α΄α΄α΄α΄ Κα΄κ±α΄Κ</b>\n\n<b>DL:</b> {human_readable_bytes(result["download"] / 8)}/s <b>UL:</b> {human_readable_bytes(result["upload"] / 8)}/s'
    )

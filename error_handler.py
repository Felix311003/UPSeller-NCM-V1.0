import os
from datetime import datetime

from config import SCREENSHOT_DIR
from logger import logger



def save_error_screenshot(page, name):


    try:


        # 创建目录

        if not os.path.exists(
            SCREENSHOT_DIR
        ):

            os.makedirs(
                SCREENSHOT_DIR
            )



        time_str = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )



        file_path = os.path.join(

            SCREENSHOT_DIR,

            f"{name}_{time_str}.png"

        )



        page.screenshot(
            path=file_path,
            full_page=True
        )



        logger.info(
            f"错误截图保存:{file_path}"
        )



    except Exception as e:


        logger.error(
            "截图失败:" + str(e)
        )
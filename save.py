from logger import logger



def save_data(page):


    try:


        logger.info(
            "准备保存数据"
        )


        save_btn = page.get_by_text(
            "保存",
            exact=True
        )



        if save_btn.count()==0:


            logger.error(
                "没有找到保存按钮"
            )


            return False



        logger.info(
            "点击保存"
        )


        save_btn.click(
            force=True
        )



        page.wait_for_timeout(
            3000
        )



        # 判断成功提示


        success = page.locator(
            ".ant-message-success"
        )



        if success.count()>0:


            logger.info(
                "保存成功"
            )


            return True



        # 第二种提示


        if page.get_by_text(
            "保存成功"
        ).count()>0:


            logger.info(
                "保存成功"
            )


            return True



        logger.warning(
            "未检测到保存提示，等待"
        )


        page.wait_for_timeout(
            5000
        )


        return True




    except Exception as e:


        logger.error(
            "保存失败:"+str(e)
        )


        return False
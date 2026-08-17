from logger import logger


def check_login(page):

    """
    检查UPSseller是否登录
    """

    try:

        logger.info(
            "检查UPSseller登录状态"
        )


        page.wait_for_timeout(
            3000
        )


        # 登录页面特征
        login_text = page.get_by_text(
            "登录",
            exact=True
        )


        if login_text.count() > 0:


            logger.warning(
                "检测到未登录"
            )


            return False



        # 商品页面特征

        product = page.locator(
            "tbody tr"
        )


        if product.count() > 0:


            logger.info(
                "登录状态正常"
            )


            return True



        logger.warning(
            "无法确认登录状态"
        )


        return False



    except Exception as e:


        logger.error(
            "登录检测失败:" + str(e)
        )


        return False





def wait_login(page):

    """
    等待用户登录
    """


    logger.warning(
        "请在浏览器中完成登录"
    )


    print(
        "\n====================="
    )

    print(
        "请登录 UPSeller"
    )

    print(
        "登录完成后按回车继续..."
    )

    print(
        "=====================\n"
    )


    input()


    page.reload()


    page.wait_for_timeout(
        5000
    )



    if check_login(page):


        logger.info(
            "登录成功，继续执行"
        )


        return True



    else:


        logger.error(
            "登录仍未成功"
        )


        return False
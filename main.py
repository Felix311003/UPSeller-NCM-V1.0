from browser_manager import BrowserManager
from logger import logger

from ncm_ai import generate_ncm
from origin import set_origin

from config import (
    WAIT_TIME,
    PRODUCT_LIMIT,
    ENABLE_AI
)

from error_handler import save_error_screenshot
from login_check import check_login, wait_login
from save import save_data


def get_cell_text(row, field):

    try:

        cell = row.locator(
            f'td[data-field-column="{field}"]'
        )

        if cell.count() == 0:
            return ""

        return (
            cell.inner_text()
            .strip()
        )


    except Exception:

        return ""



def check_ncm(value):

    """
    判断NCM是否真实存在
    """

    if not value:
        return False


    invalid_values = [

        "+添加",
        "添加",
        "请选择",
        "暂无"

    ]


    if value in invalid_values:
        return False


    return True




def main():

    logger.info(
        "====================="
    )


    logger.info(
        "UPSeller NCM助手启动"
    )



    browser = BrowserManager()
    page = None



    try:


        page = browser.start()


        page.wait_for_timeout(
            3000
        )


# ===============================
# 登录检测
# ===============================


        if not check_login(page):


            success = wait_login(page)


            if not success:


                logger.error(
                   "登录失败，程序退出"
        )


                return



        # ===============================
        # 选择商品
        # ===============================


        checkboxes = page.locator(
            "input.ant-checkbox-input"
        )


        count = checkboxes.count()


        print(
            "找到复选框:",
            count
        )


        if count == 0:


            print(
                "没有商品"
            )


            return




        checkboxes.nth(0).check()


        print(
            "选择第一个商品"
        )





        # ===============================
        # 批量编辑
        # ===============================


        page.get_by_text(
            "批量编辑",
            exact=True
        ).click()



        page.wait_for_timeout(
            5000
        )





        # ===============================
        # 切换bulk页面
        # ===============================


        for p in page.context.pages:


            if "bulk-edit" in p.url:


                page = p

                break




        print(
            "当前页面:",
            page.url
        )


        page.wait_for_timeout(
            3000
        )






        # ===============================
        # 开启字段
        # ===============================


        for field in [


            "Ncm",

            "Origin"


        ]:



            checkbox = page.locator(

                f'input.ant-checkbox-input[value="{field}"]'

            )


            if checkbox.count():


                if not checkbox.is_checked():


                    checkbox.check()


                    page.wait_for_timeout(
                        2000
                    )


                    print(
                        field,
                        "开启"
                    )





        page.wait_for_timeout(
            3000
        )






        # ===============================
        # 获取商品数量
        # ===============================


        rows = page.locator(
            "tbody tr"
        )


        row_count = rows.count()

        if row_count > PRODUCT_LIMIT:

           row_count = PRODUCT_LIMIT



        print(
            "商品数量:",
            row_count
        )







        # ===============================
        # 循环处理商品
        # ===============================


        for i in range(row_count):


            print(
                "====================="
            )



            rows = page.locator(
                "tbody tr"
            )


            row = rows.nth(i)



            page.wait_for_timeout(
                500
            )




            product_title = get_cell_text(

                row,

                "ProductName"

            )



            print(

                "商品:",

                product_title

            )




            if not product_title:


                print(

                    "标题为空跳过"

                )


                continue





            # ===============================
            # NCM检查
            # ===============================


            ncm = get_cell_text(

                row,

                "Ncm"

            )



            print(

                "当前NCM:",

                ncm

            )





            if check_ncm(ncm):


                print(

                    "已有有效NCM，跳过AI"

                )



            else:


                print(

                    "NCM为空，开始AI生成"

                )



                if ENABLE_AI:


                    result = generate_ncm(
                        page,
                        row,
                        product_title
    )


                else:


                    result = None



                print(

                    "AI结果:",

                    result

                )








            # ===============================
            # Origin设置
            # ===============================


            rows = page.locator(
                "tbody tr"
            )


            row = rows.nth(i)



            page.wait_for_timeout(
                1000
            )



            print(
                "检查原产地"
            )



            origin = get_cell_text(

                row,

                "Origin"

            )





            if origin and "2 -" in origin:



                print(

                    "原产地已经是2:",

                    origin

                )




            else:



                print(

                    "当前原产地:",

                    origin,

                    "需要修改为2"

                )



                origin_result = set_origin(

                    page,

                    row

                )




                if origin_result:


                    print(

                        "原产地修改成功"

                    )


                else:


                    print(

                        "原产地修改失败"

                    )

                    save_error_screenshot(
                        page,

                        f"origin_error_{i}"

                    )








        # ===============================
        # 全部完成，自动保存
        # ===============================
        print(
            "全部商品处理完成"
      )


        logger.info(
            "开始自动保存"
)


        save_result = save_data(page)



        if save_result:


            print(
                "保存成功"
    )


            logger.info(
                "保存成功"
    )


        else:


            print(
                "保存失败"
    )


            logger.error(
                "保存失败"
    )


            save_error_screenshot(
                page,
                "save_error"
    )

       



            success = page.locator(
                ".ant-message-success"
            )



            if success.count() > 0:



                logger.info(
                    "保存成功"
                )


            elif page.get_by_text(
                "保存成功",
                exact=False
            ).count() > 0:



                logger.info(
                    "保存成功"
                )


            else:


                logger.warning(
                    "未检测到保存提示，等待结束"
                )

                save_error_screenshot(
                    page,
                    "save_warning"
                )



                page.wait_for_timeout(
                    5000
                )



    except Exception as e:



        logger.error(

            str(e)

        )


        if page:


            save_error_screenshot(
                page,
                "main_error"
            )

    except Exception :
            pass




    finally:


        pass




if __name__ == "__main__":


    main()
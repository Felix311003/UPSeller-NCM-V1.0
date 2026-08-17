from logger import logger


def set_origin(page, row):

    try:

        logger.info(
            "开始设置Origin为2"
        )


        # ==========================
        # Origin单元格
        # ==========================

        origin_cell = row.locator(
            'td[data-field-column="Origin"]'
        )


        if origin_cell.count() == 0:

            logger.error(
                "没有找到Origin字段"
            )

            return False



        origin_cell.scroll_into_view_if_needed()

        page.wait_for_timeout(
            500
        )



        # ==========================
        # hover显示编辑按钮
        # ==========================


        text_area = origin_cell.locator(
            ".line_overflow"
        )


        logger.info(
            f"文字区域数量:{text_area.count()}"
        )


        if text_area.count() > 0:

            text_area.last.hover(
                force=True
            )

        else:

            origin_cell.hover(
                force=True
            )



        page.wait_for_timeout(
            1000
        )



        # ==========================
        # 点击编辑按钮
        # ==========================


        edit_btn = origin_cell.locator(
            "i.edit_btn"
        ).last



        if edit_btn.count() == 0:

            logger.error(
                "没有找到编辑按钮"
            )

            return False



        logger.info(
            "点击Origin编辑按钮"
        )


        edit_btn.click(
            force=True
        )



        page.wait_for_timeout(
            1500
        )



        # ==========================
        # 找编辑后的select
        # ==========================


        select = origin_cell.locator(
            ".ant-select"
        )



        if select.count() == 0:


            logger.error(
                "编辑后没有生成select"
            )

            return False



        logger.info(
            "找到Origin select"
        )



        # ==========================
        # 点击select打开列表
        # ==========================


        select.click(
            force=True
        )


        logger.info(
            "打开Origin下拉"
        )



        page.wait_for_timeout(
            1500
        )



        # ==========================
        # 查找选项
        # ==========================


        option = page.locator(
            ".ant-select-dropdown-menu-item"
        ).filter(
            has_text="2 - Estrangeira"
        )



        if option.count() == 0:


            option = page.locator(
                ".ant-select-dropdown .ant-select-dropdown-menu-item"
            ).filter(
                has_text="2 - Estrangeira"
            )



        if option.count() == 0:


            # 新版antd

            option = page.locator(
                ".ant-select-item-option"
            ).filter(
                has_text="2 - Estrangeira"
            )



        if option.count() == 0:


            logger.error(
                "没有找到Origin选项2"
            )

            return False



        logger.info(
            "找到Origin选项2"
        )



        option.last.click(
            force=True
        )



        logger.info(
            "选择Origin 2完成"
        )



        page.wait_for_timeout(
            3000
        )



        # ==========================
        # 验证
        # ==========================


        new_origin = origin_cell.inner_text().strip()



        logger.info(
            f"修改后Origin:{new_origin}"
        )



        if "2 -" in new_origin:


            logger.info(
                "Origin修改成功"
            )

            return True



        else:


            logger.error(
                "Origin没有更新"
            )

            return False




    except Exception as e:


        logger.error(
            "Origin失败:" + str(e)
        )


        return False
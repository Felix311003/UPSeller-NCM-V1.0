from logger import logger



def generate_ncm(page, row, product_title):

    try:

        logger.info(
            "开始AI生成NCM:"
            + product_title
        )


        # =================================
        # 当前商品 NCM 单元格
        # =================================

        ncm_cell = row.locator(
            'td[data-field-column="Ncm"]'
        )


        if ncm_cell.count() == 0:

            logger.error(
                "没有找到NCM字段"
            )

            return None



        # =================================
        # 点击 +添加
        # =================================

        add_btn = ncm_cell.locator(
            "span.my_txt_btn",
            has_text="+添加"
        )


        if add_btn.count():

            logger.info(
                "点击当前商品NCM添加"
            )

            add_btn.click()


        else:

            logger.info(
                "NCM已有编辑入口"
            )

            ncm_cell.click()



        page.wait_for_timeout(
            2000
        )



        # =================================
        # 搜索框
        # =================================


        search_input = page.locator(
            "input.ant-select-search__field"
        ).last


        if search_input.count()==0:

            logger.error(
                "没有找到NCM搜索框"
            )

            return None



        search_input.click()



        page.wait_for_timeout(
            1000
        )



        # 点击搜索按钮

        search_icon = page.locator(
            "i.icon_search"
        ).last



        if search_icon.count():

            search_icon.click()



        page.wait_for_timeout(
            3000
        )




        # =================================
        # AI按钮
        # =================================


        ai_btn = page.locator(
            "i.icon_svg_Ai"
        ).last



        if ai_btn.count()==0:


            logger.error(
                "没有找到AI按钮"
            )

            return None



        ai_btn.click()



        page.wait_for_timeout(
            3000
        )





        # =================================
        # 输入商品名称
        # =================================


        textarea = page.locator(
            "textarea.ant-input"
        ).last



        if textarea.count()==0:


            logger.error(
                "没有找到AI输入框"
            )

            return None




        textarea.fill(
            product_title
        )





        # =================================
        # 生成NCM
        # =================================


        page.get_by_text(
            "生成NCM",
            exact=False
        ).click()



        logger.info(
            "等待AI生成NCM"
        )



        page.wait_for_timeout(
            10000
        )




        # =================================
        # 获取AI结果
        # =================================


        result_box = page.locator(
            "div.mt_20 span"
        ).last



        if result_box.count()==0:


            logger.error(
                "没有找到AI结果"
            )

            return None




        ncm_result = (
            result_box.inner_text()
            .strip()
        )



        logger.info(
            "AI生成NCM:"
            + ncm_result
        )





        # =================================
        # 应用
        # =================================


        page.get_by_text(
            "应用",
            exact=True
        ).click()



        page.wait_for_timeout(
            3000
        )




        # =================================
        # 选择
        # =================================


        page.get_by_text(
            "选择",
            exact=True
        ).click()



        page.wait_for_timeout(
            3000
        )



        return ncm_result




    except Exception as e:


        logger.error(
            "AI生成NCM失败:"
            + str(e)
        )


        return None
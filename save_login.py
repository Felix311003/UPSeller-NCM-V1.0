from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://app.upseller.com/zh-CN/products/product-list")


    print("请手动登录...")
    input("登录完成后按回车保存状态")


    context.storage_state(
        path="login.json"
    )

    print("登录状态已保存")

    browser.close()
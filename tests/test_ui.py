from playwright.sync_api import Page, expect


def test_pagina_inicial_carrega(page: Page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")
    expect(page.get_by_text("Swag Labs")).to_be_visible()


def test_login_com_dados_invalidos(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("usuario_invalido")
    page.locator('[data-test="password"]').fill("senha_incorreta")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_be_visible()

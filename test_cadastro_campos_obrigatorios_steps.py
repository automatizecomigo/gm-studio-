from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/cadastro_campos_obrigatorios.feature')


@given('que estou na página Goden Movie Studio')
def pagina_golden_movie_studio(browser: Page):
    browser.goto('http://127.0.0.1:8080/')


@when(parse("faco o preechimento dos campos obrigatórios"), converters=dict(texto=str))
def preencher_campos_obrigatorios(browser: Page):
    browser.locator('[placeholder="Nome...*"]').fill('Rafael')
    browser.locator('[placeholder="Sobrenome...*"]').fill('Pantoja')
    browser.locator('[placeholder="Email...*"]').fill('Pantoja1@gmail.com')
    browser.locator('[placeholder="Telefone..."]').fill('91983074577')
    browser.locator('[placeholder="Senha...*"]').fill('@Panquecaria20246')
    browser.get_by_text('Cadastrar', exact=True).click()


@then(parse("valido se o usuario foi cadastra com sucesso"), converters=dict(texto=str))
def validacao_de_cadastro_de_usuario(browser: Page):
    expect(browser.get_by_text('Cadastro realizado com sucesso!')).to_be_visible()

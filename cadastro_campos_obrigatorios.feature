# Created by rafael.pantoja at 06/07/2024
Feature: Acessar a pagina Goden Movie Studio e realizar o preenchimento de
  campos obrigatórios

  Scenario: Realizar o preenchimento de campos obrigatórios
    Given que estou na página Goden Movie Studio
    When faco o preechimento dos campos obrigatórios
    Then valido se o usuario foi cadastra com sucesso
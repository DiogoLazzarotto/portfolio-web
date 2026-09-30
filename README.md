# Portfólio web

Página estática responsiva em HTML/CSS/JavaScript, com apresentação, três projetos, filtro por área e links para código. Sem frameworks, rastreadores ou recursos externos. Projeto preparado com apoio de IA.

## Site publicado

[Abrir portfólio](https://diogolazzarotto.github.io/portfolio-web/). Hospedado no GitHub Pages a partir da branch `main`, pasta raiz.

## Executar

```bash
python -m http.server 8080 --bind 127.0.0.1
```

Abra http://127.0.0.1:8080. Alternativamente, abra `index.html` diretamente. O filtro é executado no navegador.

## Decisões

Paleta grafite, azul e ciano; tipografia do sistema; layout responsivo. Estrutura semântica, idioma declarado, foco visível, botões com `aria-pressed` e resultado de filtro com anúncio acessível. Os números nos cards são exemplos fictícios, não métricas profissionais.

## Limites

Links apontam para os repositórios independentes dos projetos. A página não hospeda os servidores Python. Não há formulário de contato nem dados pessoais inventados. O site está publicado no GitHub Pages; somente a página estática é hospedada, os servidores Python são executados localmente.

## Obter o projeto

```bash
git clone https://github.com/DiogoLazzarotto/portfolio-web.git
cd portfolio-web
```

[Voltar ao perfil](https://github.com/DiogoLazzarotto)

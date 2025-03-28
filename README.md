<h1>Estrutura MVC - Login</h1>

<p>Este projeto é um modelo em MVC para Python, que demonstra um sistema de login simples com o objetivo de facilitar a compreensão da lógica do código.</p>

<h2>Funcionalidades</h2>
<ul>
    <li>Campo de texto para digitar Usuário e Senha</li>
    <li>Botão para fazer login</li>
</ul>

<h2>Tecnologias e Bibliotecas Utilizadas</h2>
<ul>
    <li><strong>Linguagens</strong>:
        <ul>
            <li>Python</li>
        </ul>
    </li>
    <li><strong>Bibliotecas/Frameworks - Instalados pelo Pip</strong>:
        <ul>
            <li>Flet - Interface Gráfica</li>
            <li>PyInstaller - Empacotador de aplicações Python</li>
        </ul>
    </li>
</ul>

<h2>Técnicas e Práticas</h2>
<ul>
    <li>Implementação do padrão MVC para organização do código</li>
    <li>Empacotamento do app Flet com o <strong>flet pack</strong> para distribuição multiplataforma</li>
</ul>

<h2>Instruções para Empacotar o Aplicativo</h2>
<p>Para empacotar o aplicativo em um arquivo executável para Windows ou outras plataformas, utilize o <strong>flet pack</strong>.</p>

<pre>
1. Certifique-se de que você tem o ambiente Python configurado corretamente (com o Flet e o PyInstaller instalados). Caso não tenha, instale as dependências:

    pip install flet pyinstaller

2. Desenvolva seu código no arquivo principal (geralmente main.py ou algo semelhante).

3. Empacote com o comando:

    flet pack main.py --icon your-icon.png

    - <strong>main.py</strong>: Substitua pelo nome do arquivo Python que contém o aplicativo Flet no caso atual é o main.py
    - <strong>--icon your-icon.png</strong>: (opcional) Substitua pelo caminho do ícone que deseja adicionar ao executável.

4. O arquivo executável será gerado na pasta <strong>dist/</strong>. Execute o arquivo gerado para testar o aplicativo.
</pre>


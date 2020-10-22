# StreamLit

StreamLit Web Lib: https://www.tornadoweb.org/en/stable/_modules/tornado/auth.html?highlight=session#     
How to use Tornado: https://discuss.streamlit.io/t/how-to-get-all-ip-addresses-and-their-countries-connecting-to-a-live-streamlit-app-on-aws-ec2/2273


Run Streamlit: ``` streamlit run app.py ```


PyCharm Debug Streamlit
![PyCharmDebugStreamlit](https://i.stack.imgur.com/rePKV.png)

1. Configuração do Virtual Env (VENV)

    1. Criação do VENV
        ```shell script
           # Vem instalado com o PIP, não precisa instalar o VirtualEnv
           $ pip install virtualenv 
           $ virtualenv -p python3 venv
        ```

    1.  Ativando o VENV (faça isso toda vez que for executar o projeto)
        ```shell script
            # MacOS
            $ source venv/bin/activate

            # Windows (Gitbash)
            $ /c/Projects/gaesi/msdaf/predictive/venv/Scripts/activate.bat
            # Windows (Prompt)
            > cd C:\Projects\gaesi\msdaf\predictive
            > venv\Scripts\activate.bat
        ```

1. Instalando as dependências com as versões unificadas

    ```shell script
        # MAC
        $ pip install -r requirements_mac.txt
        # WINDOWS
        $ pip install -r requirements_win.txt
    ```
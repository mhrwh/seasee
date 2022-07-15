## 導入手順

1. pythonのダウンロード[https://www.python.org/downloads/](https://www.python.org/downloads/)

1. 仮想環境の作成 
    - Mac

      ターミナルで以下を実行
      ```
      $ python3 -m venv venv
      ```
      <br>

    - Windows
      
      PowerShellで以下を実行
      ```
      > PowerShell Set-ExecutionPolicy RemoteSigned CurrentUser
      ```
      ```
      > py -m venv venv
      ```
      <br>

1. 仮想環境の有効化
    - Mac

      ターミナルで以下を実行
      ```
      $ source venv/bin/activate
      ```
      <br>

    - Windows

      PowerShellで以下を実行
      ```
      > venv\\Scripts\\Activate.ps1
      ```
      <br>

1. ライブラリのインストール
    ```
    (venv)$ pip install -r requirements.txt
    ```

1. サーバーの起動
    ```
    (venv) $ flask run
    ```


## 備考
- VSCodeならPythonの拡張機能を入れておきましょう
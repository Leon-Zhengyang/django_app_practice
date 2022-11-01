// 仮想環境作る
python -m venv env

//仮想環境に入る(win)
env\Scripts\Activate.ps1
//仮想環境に入る(mac)
source env/bin/activate

// 仮想環境quite
deactivate

// requirementsを作成する
pip freeze > requirements.txt

// libaryのインストール
pip install -r requirements.txt

//現在の環境にインストールされたパッケージ確認
pip freeze
pip list

//パッケージ削除
pip uninstall Django

//requirements.txt中のライブラリを一括インストール
pip install -r requirements.txt

// プロジェクト作成する
django-admin startproject config .

// アプリを作成する
python manage.py startapp appname

// サーバーを起動する
python manage.py runserver

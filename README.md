# Backup Qiita md

## これはなに

- Qiitaのユーザー投稿をすべて取得できます。
- 自分のじゃなくても取得できます。
- 記事タイトルのMarkdownファイルで書き出してくれます。

## セットアップ

### 前提

- Python3 (開発環境は3.8)
- pip (開発環境ではpipenvを使用)
- Git

### ソースの取得

`git clone https://github.com/Chipsnet/backup-qiita-md.git`

### 依存関係のインストール

グローバルを汚したくない人は`pipenv`を使ってください。

- Pipenvの場合
    - `pipenv install`
- pipの場合
    - `pip install -r requirements.txt`

### tokenの取得

[Qiitaのアプリケーション設定](https://qiita.com/settings/applications)から取得できます。

### 実行

`python run.py`で実行、tokenとユーザーIDさえ入れればあとは勝手にmdフォルダ作ってMarkdownブチこんでくれます。

## ライセンス

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

## donate

よろしくお願いします      
https://minato86.me/donate.html

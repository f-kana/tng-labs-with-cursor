# The Next Generation Labs with Cursor

Django 5を使用したプロトタイプ開発環境です。

## 前提条件

- macOS (Apple Silicon)
- Python 3.13
- Cursor IDE
- ngrok

## セットアップ手順

### 1. MCPツールのセットアップ

前提知識無しで作業するとあなたの既存の設定を破壊する場合があるので、エンジニアに作業を依頼してください。

必要なツール

* Playwright MCP

**注意：** この手順はCursorを再起動する前に実行してください。

### 2. リポジトリのクローン

```bash
git clone <repository-url>
cd tng-labs-with-cursor
```

### 3. 仮想環境の作成と依存関係のインストール

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

### 3. Cursorの起動

```bash
cursor .
```

## 開発開始

Cursorを起動したら、Cursorに以下の作業を依頼してください：

- Djangoプロジェクトの初期化（マイグレーション、スーパーユーザー作成など）
- 開発サーバーの起動
- その他の開発作業

## 開発コマンド

主要なコマンドはMakefileに記載されています：

```bash
# 開発サーバーの起動
make run

# データベースのマイグレーション
make migrate

# 静的ファイルの収集
make collectstatic

# コードの品質チェック
make lint
```

## プロジェクト構成

- **Django 5**: Webフレームワーク
- **SQLite**: データベース（開発用）
- **Class-based Views**: ビューの実装方式
- **Admin画面**: 管理者向け機能

## 開発方針

- 完璧なコードより動作するプロトタイプを優先
- Server Side Rendering
- 高速なプロトタイプ開発を主目的
- 自動テストは不要
- セキュリティの考慮は不要

## トラブルシューティング

### 仮想環境が認識されない場合

Cursorを起動する前に、必ず仮想環境をアクティベートしてください：

```bash
source venv/bin/activate
cursor .
```

### Playwright MCPが動作しない場合

1. Cursorを完全に終了
2. MCP設定ファイルが正しい場所に配置されているか確認
3. Cursorを再起動

### その他の問題

時間をかけてもエラー解消しない場合や、Cursorが把握できない外部環境起因のエラーが疑われる場合は、シニアエンジニアにヘルプを求めてください。

## 注意事項

- このプロジェクトはローカル開発環境でのプロトタイプ開発を目的としています
- 本番環境はありません
- ngrokを使用して暫定公開を行います

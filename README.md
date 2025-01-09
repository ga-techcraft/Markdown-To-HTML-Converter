# Markdown to HTML Converter

このスクリプトは、**Markdown ファイル (.md)** を **HTML ファイル (.html)** に変換する Python プログラムです。  
Markdown ファイルを入力し、HTML ファイルを出力します。

---

## 🚀 **使い方**

以下のコマンドをターミナルで実行してください：

```bash
python file-converter.py <入力ファイル>.md <出力ファイル>.html
```

### ✅ **使用例**

`sample.md` を `output.html` に変換する場合：

```bash
python file-converter.py sample.md output.html
```

---

## 📋 **必要な環境**

- **Python 3.6以上**
- **`markdown` パッケージ**

---

## 🛠 **セットアップ手順**

1. **リポジトリをクローン**：

   ```bash
   git clone <リポジトリのURL>
   cd markdown_to_html_converter
   ```

2. **仮想環境を作成して有効化**（推奨）：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **必要なパッケージをインストール**：

   ```bash
   pip install markdown
   ```

4. **スクリプトを実行**：

   ```bash
   python file-converter.py <入力ファイル>.md <出力ファイル>.html
   ```

---

## 🧩 **コードの説明**

このスクリプトは、以下の手順で動作します：

1. コマンドライン引数の個数を確認します。
2. 第1引数が **Markdown ファイル (.md)**、第2引数が **HTML ファイル (.html)** であることを確認します。
3. **`markdown` パッケージ**を使用して、Markdown テキストを HTML に変換します。
4. **ファイル操作時のエラー**を適切に処理します。

---

## 📄 **サンプルファイル：`sample.md`**

以下のテキストを **`sample.md`** という名前で保存してください：

```markdown
# タイトル: 私のブログ

## セクション 1: 自己紹介

こんにちは！私はプログラミングが大好きです。  
このブログでは、学んだことを共有していきます。

## セクション 2: 学んでいる技術

- Python
- Flask
- HTML & CSS
- JavaScript
- SQL

## セクション 3: お問い合わせ

何か質問があれば、次のメールアドレスにご連絡ください。

📧 **メール:** example@example.com
```

---

## 📄 **生成される HTML ファイル：`output.html` の例**

```html
<h1>タイトル: 私のブログ</h1>
<h2>セクション 1: 自己紹介</h2>
<p>こんにちは！私はプログラミングが大好きです。<br>このブログでは、学んだことを共有していきます。</p>
<h2>セクション 2: 学んでいる技術</h2>
<ul>
<li>Python</li>
<li>Flask</li>
<li>HTML &amp; CSS</li>
<li>JavaScript</li>
<li>SQL</li>
</ul>
<h2>セクション 3: お問い合わせ</h2>
<p>何か質問があれば、次のメールアドレスにご連絡ください。</p>
<p>📧 <strong>メール:</strong> example@example.com</p>
```
import markdown
import sys
import os

# ファイル操作時の例外処理の関数
def handlerFileError(e):
  if isinstance(e, FileNotFoundError):
    print('エラー: ファイルが見つかりません。')
  elif isinstance(e, PermissionError):
    print('エラー: ファイルにアクセスする権限がありません。')
  elif isinstance(e, IsADirectoryError):
    print('エラー: 指定したパスがディレクトリです。')
  elif isinstance(e, OSError):
    print('エラー: OSエラーが発生しました。')
  else:
    print(f'予期しないエラーが発生しました: {e}')

# 引数の個数を確認する 
if len(sys.argv) != 3:
  print(f'file-converterの引数の個数が合いません。')
  sys.exit()

# 第一引数はmdファイル、第二引数はhtmlファイルかどうか確認する
if not sys.argv[1].endswith('.md'):
  print(f'{sys.argv[1]}の第１引数には拡張子が.mdのマークダウンファイルを指定してください。')
  sys.exit()
if not sys.argv[2].endswith('.html'):
  print(f'{sys.argv[1]}の第２引数には拡張子が.htmlのHTMLファイルを指定してください。')
  sys.exit()

mdFile = sys.argv[1]
htmlFile = sys.argv[2]

# md形式のテキストをhmltに変換する
try:
  with open(mdFile, 'r') as mdFD:
    mdText = mdFD.read()
    htmlText = markdown.markdown(mdText)

  with open(htmlFile, 'w') as htmlFD:
    htmlFD.write(htmlText)
    print('マークダウン形式のテキストをhtml形式に変換しました。')
except Exception as e:
  handlerFileError(e)
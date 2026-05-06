# プロジェクト概要
## プロジェクト名
generate_tree

## プロジェクトの目的
```
ファイルツリーが欲しかった。
でもvscodeの拡張機能は使いたくなかった。
せや！Geminiに書かせたろ！
```

## プロジェクト構成
本プロジェクトは、pythonファイル1つだけという簡単なつくり
- `generate_tree.py`: python

## 動作環境
本プロジェクトは**python標準ライブラリのみ**で作成されています。<br>
外部ライブラリのインストール(pip等)は不要です<br>
そのため、pythonさえインストールされていればどんな環境でも動く「**ポータブル**」なコードになっています。
### 使用ライブラリ
- sys
- pathlib
※どちらもpython標準ライブラリ

---

# 使い方
どこのパスから始めるか、どの深さまで検出するかをパラメータで設定できる。<br>
以下に使い方のレパートリとその実行内容について示す。

## 基本コマンド
```bash
python generate_tree.py [パス] [深さ]
```

## 1.現在の場所をすべて表示
パスも深さも指定しない場合、カレントディレクトリから全階層を表示します。
```bash
python generate_tree.py
```

## 2.特定のフォルダをすべて表示
表示したいディレクトリのパスを第1引数に指定します。
```bash
python generate_tree.py ./src
```

## 3.現在の場所を、階層を絞って表示
現在の場所（.）を指定し、第2引数に制限したい深さを指定します。
```bash
python generate_tree.py . 3
```

## 特定のフォルダを、階層を絞って表示
パスと深さを両方指定します。
```bash
python generate_tree.py ./my_project 2
```

---

# 表示ルール
- **ファイル優先**: 各階層では、まず「ファイル」が名前順に表示されます。
- **ボリューム順**: 「ディレクトリ」は、その中身の合計アイテム数が少ない順に並びます。これにより、複雑な構造が後半にまとまり、画面が見やすくなります。
- **深さ制限**: 深さを指定した場合、表示だけでなくファイル数のカウントもその深さまでで計算されます。

---

# 出力イメージ
```text
>> python generate_tree.py ./sample_project 2
sample_project/
├── .gitignore
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_main.py
├── docs/
│   ├── index.html
│   └── setup.md
├── src/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
└── data/
    ├── input.csv
    ├── output.json
    └── logs/
```

---

## 余談
今回は**完全**にGeminiに書かせた。<br>
1つのエラーもなく、**30分**くらいで完成した。<br>
Gemini君すげー。

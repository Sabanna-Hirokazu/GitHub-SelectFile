# GitHub-SelectFile
GitHubのレポジトリ内の任意のファイルをダウンロードすることができる。
svnのコマンドの使用方法をよく忘れてしまう人のためのツール。実際のファイルのURLを引数に置くだけでsvnに必要なURLに変換し、ダウンロードを行うものである。

## インストール
こちらのツールを使う際に必要なパッケージをインストールする必要があります。
[こちらのページ](http://subversion.apache.org/packages.html)を参考にインストールすることができる。

### Ubuntu or Linux Mint

```
apt-get install subversion
apt-get install libapache2-svn
```

### CentOS

```
yum install subversion
yum install mod_dav_svn
```

### Mac OS

```
brew options subversion
brew install (OPTIONS) subversion
```

## 実行
クローンしてきたPythonのファイルを実行することでGitHubから一部のファイルをダウンロードすることができる。
実行する際にダウンロードしたいファイルのURLを引数に入れる必要がある。引数には複数代入可能で、まとめてダウンロードすることができる。

```
python3 SelectFile.py URL
```

### 実行例
このレポジトリのsampleフォルダの中身をダンロードするものになる。
この[リンク](https://github.com/Sabanna-Hirokazu/GitHub-SelectFile/tree/master/sample)はsampleフォルダの中のリンクであり、このURLを入れることでsampleフォルダとその中にあるsample.pyとsample1のフォルダとその中に含まれるsample2.pyをダンロードすることができる。

```
python3 SelectFile.py https://github.com/Sabanna-Hirokazu/GitHub-SelectFile/tree/master/sample
```
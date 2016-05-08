# CountApp

## count.py

- layout: BoxLayoutを継承
- メソッドとして、```count_up```と```count_down```を用意。
- count.kv側からボタンのアクションを登録。

```count.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CountView(BoxLayout):
    def __init__(self, **kwargs):
        super(CountView, self).__init__(**kwargs)

    def count_up(self):
        current_val = int(self.ids.total_count_view.text)
        self.ids.total_count_view.text = str(current_val + 1)

    def count_down(self):
        current_val = int(self.ids.total_count_view.text)
        self.ids.total_count_view.text = str(current_val - 1)


class CountApp(App):
    def build(self):
        return CountView()


if __name__ == '__main__':
    CountApp().run()
```

**count.kv**

ルールコンテキストとして**root**ルールと、**class**ルールの2種類がある。
kvファイルでこれらは次のように区別して記述する


|context|kv内|
|:----|:----|
|root|```Widget:```|
|class|```<Widget>:```|


```
#:kivy 1.9.0

<CountView>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: total_count_view
            text: "0"
            font_size: 100
        Button:
            id: btn_count_up
            text: "Count Uppp"
            font_size: 50
            on_press: root.count_up()
        Button:
            id: btn_count_down
            text: "Count Down"
            font_size: 50
            on_press: root.count_down()
```

## buildozer osx debug

```
buildozer osx debug
```

### ハマりどころ

#### Keka.appが必要

パッケージ化するときに[Keka,app](http://www.kekaosx.com/ja/)が必要。先にインストールしておく。

#### Kivy.appのインストールと名前に注意。

```Kivy.app```がインストール当所、```Kivy 2.app```となっていたので、```buildozer```のスクリプトが見つけられなかった。

Mac OS Xの場合、以下の用に```Kivy.app```が設置されていれば良い。

```
/Application/Kivy.app
```

**Kivy.appが見つからない場合のエラー**

```
7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,4 CPUs)

Processing archive: Kivy2.7z

Error: Can not open file as archive

Traceback (most recent call last):
  File "/usr/local/bin/buildozer", line 9, in <module>
    load_entry_point('buildozer==0.32.dev0', 'console_scripts', 'buildozer')()
  File "/usr/local/lib/python2.7/site-packages/buildozer/scripts/client.py", line 13, in main
    Buildozer().run_command(sys.argv[1:])
  File "/usr/local/lib/python2.7/site-packages/buildozer/__init__.py", line 992, in run_command
    self.target.run_commands(args)
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 234, in run_commands
    func(args)
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 247, in cmd_debug
    self.buildozer.prepare_for_build()
  File "/usr/local/lib/python2.7/site-packages/buildozer/__init__.py", line 159, in prepare_for_build
    self.target.check_requirements()
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 101, in check_requirements
    self.ensure_kivyapp()
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 89, in ensure_kivyapp
    self.download_kivy(kivy_app_dir)
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 75, in download_kivy
    'x', '{}.7z'.format(kivy)), cwd=cwd)
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 540, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '('Keka.app/Contents/Resources/keka7z', 'x', 'Kivy2.7z')' returned non-zero exit status 2
```

#### NameError: global name 'sh' is not defined

解決策

```
pip install sh --user
```


**shがインストールされていない場合のエラー**

```
Traceback (most recent call last):
  File "package_app.py", line 234, in <module>
    main(arguments)
  File "package_app.py", line 217, in main
    bootstrap(source_app, appname, confirm)
  File "package_app.py", line 79, in bootstrap
    sh.cp('-a', source_app, appname)
NameError: global name 'sh' is not defined
Traceback (most recent call last):
  File "/usr/local/bin/buildozer", line 9, in <module>
    load_entry_point('buildozer==0.32.dev0', 'console_scripts', 'buildozer')()
  File "/usr/local/lib/python2.7/site-packages/buildozer/scripts/client.py", line 13, in main
    Buildozer().run_command(sys.argv[1:])
  File "/usr/local/lib/python2.7/site-packages/buildozer/__init__.py", line 992, in run_command
    self.target.run_commands(args)
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 234, in run_commands
    func(args)
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 250, in cmd_debug
    self.buildozer.build()
  File "/usr/local/lib/python2.7/site-packages/buildozer/__init__.py", line 198, in build
    self.target.build_package()
  File "/usr/local/lib/python2.7/site-packages/buildozer/targets/osx.py", line 155, in build_package
    check_output(cmd, cwd=cwd)
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 573, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '['python', 'package_app.py', '/Users/$USER/PycharmProjects/SampleKivy/countApp/.buildozer/osx/app', '--appname=kivycounter', '--bundlename=Kivy Counter', '--bundleid=org.test', '--bundleversion=0.1', '--displayname=Kivy Counter']' returned non-zero exit status 1
```

こちらは、[ソースコードの45-49行目(kivy-sdk-packager/osx/package_app.py)](https://github.com/kivy/kivy-sdk-packager/blob/master/osx/package_app.py)に対策が書いてあるけれど、ログに出力されていなかった。

## References


- [Programming Guide » Kv language](https://kivy.org/docs/guide/lang.html#how-to-load-kv)
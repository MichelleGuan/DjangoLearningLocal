# Django/DjangoCMS踩坑指南 #
----------

## Python Django Crash Course ##
###  (by Traversy Media) ###
1. 在urls.py中，import url方法已经过时，新版本django引用path方法 `from django.urls import path,include`
2. path第一个参数是url地址，直接在引号中间写就可以。第二个参数可以include其他app的URL或者调用views.py的方法，渲染页面。比如： `path('details/<id>',views.details,name='details')`  `path('posts/', include('posts.urls'))`
3. 在虚拟环境下建好的项目只能在虚拟环境运行，可以在不同虚拟环境之间切换，但是关闭虚拟环境之后会报错。常用虚拟环境指令包括： 创建环境 mkvirtualenv name; 切换环境 workon name; 退出虚拟环境 deactivate name
4. Video使用的是MySQL，但是实际上自带的sqlite也可以运行项目，不需要更改配，跟着视频做下来就可以了。
5. 关于环境配置，尽量安装在项目上而不是全局。git bash在python运行的时候有时候有一些问题，建议使用CMD elevated权限
6. 关于vscode，安装vscode-flow-ide插件会导致提示非常缓慢，目前没有解决，Java Runtime的报错需要提交Non-Standard的申请安装。HTML提示的插件和自带提示也有冲突，所以这几个插件我都没安装。
7. 所有和数据库有关的更改，比如在Models.py里面更改数据格式名字，都需要重新migration，只需要重新执行makemigration和migrate指令就可以了。千万别去改自动生成的初始化文件！！，否则django没法比对你更改了什么。
8. 视频提到了引用一个样式库，直接贴链接就可以，不需要下载。如果取数据出现问题，常规错误一般在拼写大小写单复数上。
9. 需要注意temlates extends问题，如果跨不同app，只需要写从templates文件夹下面的目录，因为django遍历的时候只遍历templates下的文件。URL写到再上层会找不到文件。
10. 其他地方有疑问或者不想再打一遍视频内容可以直接下载代码，有任何问题随时交流。

----------
## Getting Started with django CMS ##
###  (by django CMS) ###
1. DjangoCMS创建新项目，如果需要多语言包之类要配置的问题时要加-w，视频的命令是旧版本的。示例：
`djangocms -p modern_business modern_business -w`
2. 虚拟环境参照上一个django教程，cms官方教程的我没跑通。成功创建虚拟环境后，CMD路径前面会有一个小括号包含虚拟环境名称。
3. DjangoCMS多语言支持，在项目配置生成之后可能也进不去，会报404错误，显示en/fr的URL检索不到。这个时候需要进入admin后台在page上再做配置，其他语言支持也是在后台编辑。不是setting代码问题！！
4. 目前卡在CMS-TEMPLATES上，视频和文档都说这个地方加载的顺序，会影响首页次序，但实际操作的时候，就算删了原页面，也能加载出来。。。
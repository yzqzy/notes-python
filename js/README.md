[night_team](https://notes.yueluo.club/crawler/night_team/)

## 瑞数

debugger 中间、多层 debugger

cookie: 80T - 4es 

## 反爬虫

### 头部签名验证

* base64 编码或者 16 进制编码数据，x-api-key、x-sign 等头部参数

### 请求参数签名验证

* 请求体中携带参数

### cookie 验证

建议使用无痕浏览器，或者使用浏览器插件

* 验证 cookie 签名，id_cookie

### 响应数据验证

* 响应体数据加密

## 源代码替换

读取本地文件

1. 方便调试，对于混淆的 JS 文件，可以还原 JS，然后进行替换
2. JS 文件 动态变量名 使用替换，保持名称不变，方便调试
3. 修改文件，调试输出，插入 debugger

对于瑞数，可以这样去调试。

debugger, 调试的时候 也可以使用这种方式，即断点调试。

## 断点

DOM 断点、XHR 断点 等。

DOM 断点执行比较靠前，距离加密函数比较远。
XHR 断点执行比较靠后，距离加密函数比较近，可以根据栈快速定位。

## debug 原理

无限 debugger 其实并不是死循环，而是有规律地执行逻辑，通常使用定时器来实现。

```js
Function('debugger;').call(null);
```

### 过 debug 方法

1. 浏览器条件断点，返回 false或者一律不在此处暂停；

2. 方法置空

无限 debugger 产生的原因是某个函数导致的，我们只需要重写这个函数，让函数为空，就可以过掉 debugger。

```js
origin_interval = setInterval
setInterval = function() {}
```
3. 修改响应文件

把 JS 文件保存到本地修改，可以将 debugger 相关的代码删除或者改写，可以使用本地文件替换或者抓包工具拦截等方式。

4. 注入代码到 JS 文件

```js
var _constructor = constructor
Function.propotype.constructor = function(s) {
  if (s === 'debugger') return null;
  return _constructor.apply(this, arguments)
}
```

## hook 技术

hook 是一种钩子技术，在系统没有调用函数之前，钩子程序就先得到控制权，钩子函数既可以加工处理该函数的执行行为，也可以强制结束消息的传递。

hook 实现有两个条件：

* 客户端拥有 js 的最高解释权，可以决定在任何时候注入 js，服务器无法干预（服务端只能通过检测和混淆的手段，使 hook 难度加大，无法直接阻止）。
* 除了上面的必要条件之外，还有一个条件。因为 js 使一种弱类型语言，同一个变量可以多次定义，根据需要进行不同的赋值，这种情况如果在其他强语言类型中可能会报错，导致代码无法执行。js 的这种特性，为我们 Hook 代码提供了便利。

> JS 变量是有作用域的，只有当被 hook 函数和 debugger 函数断点在同一个作用域时，才能 hook 成功。

### hook 步骤

1. 找到 hook 点，通常是某个函数，或者某个变量的赋值。
2. 编写 hook 逻辑，将 hook 点替换为自己的逻辑。
3. 注入 hook 逻辑到目标函数。
4. 调试，验证 hook 逻辑是否正常运行。

> 最常用：hookie cookie

hook 可以借助控制面板，油猴插件或者抓包工具进行注入。

### hook 方法

在 JavaScript 中，我们可以使用 hook 方法来修改函数的执行逻辑。例如 JSON.stringify() 方法用于将 JavaScript 对象转换为 JSON 字符串，JSON.parse() 方法可以将 JSON 字符串转换为 JavaScript 对象。某些站点在向服务器传输用户名密码时，就会用到这两个方法。

```js
(function() {
  var stringify = JSON.stringify;
  JSON.stringify = function(params){
    console.log('hooked stringify', params)
    debugger
    return stringify.apply(this, arguments)
  }
})()
```

### hook xhr 请求

定义变量 open 保留原始 `XMLHttppRequest.open` 方法，然后重写 open 方法，在 open 方法中添加 hook 逻辑，在 hook 逻辑中，我们可以修改 xhr 请求的 url、method、headers 等参数。

识别 xhr 请求：请求头 x-requested-with 包含 XMLHttpRequest。

```js
(function() {
  var open = XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
    if (url.indexOf('example.com') > -1) {
      console.log('hooked open', method, url, async, user, password)
      debugger
    }
    open.apply(this, arguments)
  }
})()
```

Interceptors 拦截器：

* 请求拦截器：发送请求之前，可以借助一些函数对请求的内容和参数做一些检测。如果有问题可以直接取消请求。
* 响应拦截器：当服务器返回响应数据时，响应拦截器会在会在我们得到响应数据之前，对响应数据做一些处理。

```js
axios.interceptors.request.use(function (config) {
  if (config.url.indexOf('example.com') > -1) {
    console.log('hooked request', config)
    debugger
  }
  return config;
}, function (error) {
  return Promise.reject(error);
});

axios.interceptors.response.use(function (response) {
  if (response.config.url.indexOf('example.com') > -1) {
    console.log('hooked response', response)
    debugger
  }
  return response;
}, function (error) {
  return Promise.reject(error);
});
```

> android 系统中，经常会进行抓包检测、模拟器检测、VPN 检测，我们可以借助 hook 技术进行处理。

### hook cookie

```js

```

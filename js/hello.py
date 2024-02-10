import execjs

"""
python 调用 js 代码
"""

with open('./js/hello.js', 'r') as f:
  js_code = f.read()

ctx = execjs.compile(js_code)

# 简单函数
print(ctx.call('hello_01'))  # Hello, world!
# 带参数的函数
print(ctx.call('hello_02', 'Python'))  # Hello, Python!

# 执行 JavaScript 代码
print(execjs.eval('Date.now()'))

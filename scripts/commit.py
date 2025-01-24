'''
使用 gemini 来根据 diff 生成提交信息

可以自行调整 prompt 来修改提示信息

需要自行提供 gemini api key，修改源码或放在 .env 文件里

需要自行使用 `pip install dotenv google-generativeai` 安装 py 库
'''

# 1. 设置当前 script 所在目录为工作目录
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 2. 读取 .env 文件
from dotenv import load_dotenv
load_dotenv()

# 3. 获取环境变量 GEMINI_API_KEY
import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 4. 读取当前准备提交的目录
cmd = 'git diff --staged'
# 读取输出内容
import subprocess
ret = subprocess.run(cmd, shell=True, text=True, capture_output=True)
# print(ret.stdout) 
diff = ret.stdout
print('读取 git diff 结果成功，现在开始调用 AI 生成 commit message')

# 5. 使用 AI 总结内容， gemini api 调用
prompt = f"""
这个是 AI-Commit 插件的 prompts，用于自动根据 [conventional commit conventio][ccc] 规范来生成内容

[ccc]: https://www.conventionalcommits.org/en/v1.0.0/

你根据 git 提交记录来创建 commit messages，应该遵循 conventional commit conventio 规范.

要遵守如下要求:

- 你应该使用中文而不是英文
- 你创建的内容应该不包含 ``` 代码块
- 其中 <type> 代表了规范中提及的类型，以下是 type 应该包含的列表
  - build
  - chore
  - ci
  - docs
  - feat
  - fix
  - perf
  - refactor
  - revert
  - style
  - test
- <title> 表示本次主要修改了什么信息
- <item?> 表示修改的详情
- 单行不能超过74个字符
- 仅包含一个 type 行


以下是一个模板:


<type>: <title>

- <item1>
- <item2>

这是一个示例:

chore: 更新了依赖

- 本次升级了 junit 的版本号


如下是 git commit diff: 
{diff}
```
""".strip()

## 引入 google 的 gemini api
def call_gemini_api(prompt):
  print('请稍候，正在请求 AI 生成 commit message\n')

  import google.generativeai as genai

  genai.configure(api_key=GEMINI_API_KEY)
  model = genai.GenerativeModel("gemini-2.0-flash-exp")
  response = model.generate_content(prompt)
  res = response.text.strip()

  return res

while True:
  response = call_gemini_api(prompt)
  
  # 输出生成的 commit message 到 log 中，并询问用户是否满意
  print(response)
  print('\n')
  print('是否满意?')
  print('  y:满意，r:重试，e:退出')
  confirm = input('输入你的选择: ')
  
  if confirm == "y":
    break
  elif confirm == "r":
    continue
  else:
    exit(0)


# 6. 提交

cmd = f'git commit -m "{response}"'
ret = subprocess.run(cmd, shell=True, text=True, capture_output=True)
print(ret.stdout)

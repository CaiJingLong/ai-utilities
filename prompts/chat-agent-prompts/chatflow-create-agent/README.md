# 关于聊天工具中使用 Agent 时的工作流、提示词

这里其实就是正常的聊天工具中如何配置提示词、tools 的方式。

这里我主要使用 Cluade 4.5 作为 llm 来演示我的工作流。

## 利用 AI 对于 AI 的了解，让 AI 生成提示词

### 创建 Agent 提示词生成器

通过输入，让 AI 来生成提示词，然后将提示词配置到 Agent 中。

实践1: 直接和 AI 对话，通过如下提示词，让 AI 生成提示词：

我希望为聊天工具生成 Agent 的提示词，它的职责如下，它是负责生成 Agent 提示词的 Agent，它负责通过提问来获取用户的需求，然后生成 Agent 的提示词

它这时候输出如下：

[./agents/agent-gen.md](./agents/agent-gen.md)

### 新建名为 “Agent 提示词生成器” 的 Agent

将上面的提示词配置到 Agent 中，然后就可以通过对话，让它来生成提示词了

这里还有一个优化技巧，就是让这个 Agent 自举，即，把上述的内容，作为 Agent 的用户输入，然后让这里 Agent 来生成提示词，即自优化。

### 反复自举

通过自举、调整，最终可以得到一个比较符合你需求的提示词。

## 生成其他 Agent

[AI 模拟 coding 助手](./agents/Mock-Code-Assistant.md)

[AI 自主编码助手](./agents/ai-coder.md)

[文生图提示词增强 Agent](./agents/ai-draw-enhancer.md)

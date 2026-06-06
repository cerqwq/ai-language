# 🗣️ AI Language

AI语言工具，支持语言学习、语法检查、翻译。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📚 语言课程生成
- ✅ 语法检查
- 📖 词汇表生成
- 🃏 闪卡创建
- 💬 对话生成
- 🔤 习语解释

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_language import create_tools

tools = create_tools()

# 课程生成
lesson = tools.generate_lesson("英语", "intermediate", "商务会议")

# 语法检查
grammar = tools.check_grammar(text, "英语")

# 词汇表
vocabulary = tools.generate_vocabulary_list("旅游", "英语", 20)

# 闪卡
flashcards = tools.create_flashcards(words, "英语")

# 对话
conversation = tools.generate_conversation("餐厅点餐", "英语", "beginner")

# 习语解释
idiom = tools.explain_idiom("break a leg", "英语")
```

## 📁 项目结构

```
ai-language/
├── tools.py       # 语言工具核心
└── README.md
```

## 📄 许可证

MIT License

"""
AI Language - AI语言工具
支持语言学习、语法检查、翻译
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AILanguageTools:
    """
    AI语言工具
    支持：学习、语法、翻译
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_lesson(self, language: str, level: str, topic: str) -> Dict:
        """生成语言课程"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{language}的{level}级别课程：

主题：{topic}

请返回JSON格式：
{{
    "title": "课程标题",
    "vocabulary": [{{"word": "单词", "meaning": "含义", "example": "例句"}}],
    "grammar_points": ["语法点"],
    "exercises": [{{"type": "类型", "question": "问题", "answer": "答案"}}],
    "dialogue": "对话示例"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"lesson": content}

    def check_grammar(self, text: str, language: str) -> Dict:
        """检查语法"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请检查以下{language}文本的语法：

{text}

请返回JSON格式：
{{
    "corrected": "修正后的文本",
    "errors": [
        {{"original": "原文", "corrected": "修正", "explanation": "解释"}}
    ],
    "score": "语法评分"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"grammar": content}

    def generate_vocabulary_list(self, topic: str, language: str, count: int) -> List[Dict]:
        """生成词汇表"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请生成{count}个{language}的{topic}相关词汇：

请返回JSON格式：
[
    {{"word": "单词", "pronunciation": "发音", "meaning": "含义", "example": "例句"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"vocabulary": content}]

    def create_flashcards(self, words: List[Dict], language: str) -> List[Dict]:
        """创建闪卡"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        words_text = json.dumps(words, ensure_ascii=False)

        prompt = f"""请为以下{language}词汇创建闪卡：

{words_text}

请返回JSON格式：
[
    {{"front": "正面", "back": "背面", "hint": "提示"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"flashcards": content}]

    def generate_conversation(self, scenario: str, language: str, level: str) -> str:
        """生成对话"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{level}水平的{language}对话：

场景：{scenario}

要求：
1. 自然流畅
2. 包含常用表达
3. 有中文翻译"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def explain_idiom(self, idiom: str, language: str) -> Dict:
        """解释习语"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请解释{language}习语：{idiom}

请返回JSON格式：
{{
    "idiom": "习语",
    "literal_meaning": "字面意思",
    "actual_meaning": "实际含义",
    "origin": "起源",
    "examples": ["使用示例"],
    "similar": ["类似习语"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"idiom": content}


def create_tools(**kwargs) -> AILanguageTools:
    """创建语言工具"""
    return AILanguageTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Language Tools")
    print()

    # 测试
    lesson = tools.generate_lesson("英语", "intermediate", "商务会议")
    print(json.dumps(lesson, ensure_ascii=False, indent=2))

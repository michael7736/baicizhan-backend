# 百词斩AI后端

## 快速启动（推荐使用 uvx）

1. 克隆项目
   ```
   git clone git@github.com:michael7736/baicizhan-backend.git
   cd baicizhan-backend/backend
   ```

2. 安装 [uv](https://github.com/astral-sh/uv)（如未安装）
   ```
   pip install uv
   # 或
   curl -Ls https://astral.sh/uv/install.sh | sh
   ```

3. 创建并激活虚拟环境
   ```
   uv venv
   source .venv/bin/activate
   ```

4. 安装依赖
   ```
   uv pip install -r requirements.txt
   ```

5. 配置环境变量
   - 复制 `.env.example` 为 `.env`
   - 编辑 `.env`，填写你的 OpenRouter API Key

6. 启动服务
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 主要接口

- `/get_word_card` 获取单词卡片
- `/get_quiz` 获取选择题
- `/check_answer` 判题 
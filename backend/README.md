# 百词斩AI后端

## 快速启动

1. 克隆项目
   ```
   git clone git@github.com:michael7736/baicizhan-backend.git
   cd baicizhan-backend/backend
   ```

2. 安装依赖
   ```
   pip install -r requirements.txt
   ```

3. 配置环境变量
   - 复制 `.env.example` 为 `.env`
   - 编辑 `.env`，填写你的 OpenRouter API Key

4. 启动服务
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 主要接口

- `/get_word_card` 获取单词卡片
- `/get_quiz` 获取选择题
- `/check_answer` 判题 
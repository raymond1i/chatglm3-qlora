# chatglm3-qlora
ChatGLM3-6B微调练习

GLM是基于自回归的空白填充的通用语言模型，通过增加二维位置编码并允许以任意顺序预测跨度开改进空白填充预训练。

## 构造微调训练数据集

借助 ChatGLM-4 和 GPT API 我们可以实现自动化批量构造训练数据集。

下面我们以中国古典哲学数据集为例，展示了自动构造训练集的主要流程：

 - 使用 LangChain 构造训练数据样例
    - 基于 ChatGPT 设计 `System Role` 提示词
    - 使用 `GLM-4-Flash-250414` 生成基础数据
    - 解析 GLM-4 生成的训练数据
    - 持久化存储`dataset.csv`训练数据集文件
    - 使用 GLM-4 实现训练数据多样化
 - 自动化批量生成训练数据集
    - 整理收集原始数据`raw_data.txt`
    - 自动解析原始数据样例 `raw_data_content[]`
    - 设计 `gen_data` 训练数据生成器函数
    - 设计训练数据生成流水线
## 数据准备
 - 下载数据集
 - 设计Tokenizer函数处理样本（map\shuffle\flatten)
 - 自定义批量数据处理类DataCollChatorForChatGLM
## 训练模型
 - 加载ChatGLM3-6B量化模型
 - PEFT量化模型预处理（prepare_model_for_kbit_training）
 - QLoRA Adapter 配置（TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING）
 - 微调训练超参配置（Training Arguments）
 - 开启训练（trainer.train()）
 - 保存QLoRA模型（trainer.model.save_pretrained)
## 模型推理
- 加载ChatGLM3-6B基础模型
- 加载ChatGLM3-6B QLoRA模型（PEFT Adapter）
- 微调前后对比


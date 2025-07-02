import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.environ['HF_HOME'] = '/root/autodl-tmp/cache/'

from transformers import AutoTokenizer

model_name_or_path = 'THUDM/chatglm3-6b'

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)

print(tokenizer)
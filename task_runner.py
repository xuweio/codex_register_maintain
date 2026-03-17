import argparse
import json
import os
import uuid
from datetime import datetime

def main():
    # 接收来自 GitHub Action 的 --once 参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run single registration")
    args = parser.parse_args()

    # 确保 codex 目录存在
    os.makedirs("codex", exist_ok=True)

    # 模拟生成一个 json token 文件
    token_id = uuid.uuid4().hex[:8]
    filename = f"codex/token_{token_id}.json"
    
    data = {
        "token_id": token_id,
        "created_at": datetime.now().isoformat(),
        "status": "success"
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"[Success] Generated {filename}")

if __name__ == "__main__":
    main()

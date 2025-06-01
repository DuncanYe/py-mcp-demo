# py-mcp-demo

一個使用 Python 實作的 Model Context Protocol (MCP) 伺服器示例。

## 📋 概述

這個專案展示如何建立一個簡單的 MCP 伺服器，提供自訂工具和資源給 Claude 桌面應用程式使用。

## 🚀 功能

- **加法工具**: 提供一個會自動加 10 的加法計算器

- ~**問候資源**: 根據名字生成個人化問候語~

## 📋 必要條件

- Python 3.10 或更高版本
- Claude 桌面應用程式
- UV 套件管理器（或 pip）

## 🛠️ 安裝

### 1. Clone 專案

```bash
git clone https://github.com/你的用戶名/py-mcp-demo.git
cd py-mcp-demo
```

### 2. 建立虛擬環境

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

### 3. 安裝相依套件

```bash
pip install "mcp[cli]"
```

## 🚀 使用方法

### 本地測試

```bash
# 直接執行伺服器
python main.py

# 或使用 MCP CLI
mcp run main.py
```

### 整合到 Claude 桌面應用程式

1. **安裝到 Claude**:
   ```bash
   mcp install main.py
   ```

2. **手動配置** (如果自動安裝有問題):
   
   找到 Claude 的配置檔案並添加：
   ```json
   {
     "mcpServers": {
       "Demo": {
         "command": "python",
         "args": ["/完整路徑到/py-mcp-demo/main.py"]
       }
     }
   }
   ```

3. **重新啟動 Claude 桌面應用程式**

## 💡 功能說明

### 工具

- **add(a, b)**: 計算兩個數字的和並加上 10
  ```python
  # 範例：add(5, 3) 會返回 18 (5 + 3 + 10)
  ```

### 檢查日誌

在 Claude 桌面應用程式中：
1. 找到 MCP 伺服器設定
2. 點擊 "Open Logs Folder"
3. 查看詳細錯誤訊息

## 📁 專案結構

```
py-mcp-demo/
├── main.py          # 主要 MCP 伺服器檔案
├── README.md        # 專案說明文件
└── .venv/           # 虛擬環境 (本地)
```

## 🔗 相關連結

- [MCP 是什麼？可以吃嗎？](https://www.youtube.com/watch?v=cdBRAVYZKFo)
- [MCP python-sdk](https://github.com/modelcontextprotocol/python-sdk)




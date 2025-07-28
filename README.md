# 🕵️ Bug Bounty Program Watcher

A Python automation tool that monitors major bug bounty platforms for **new programs** or **updates to existing programs**, and notifies you via Telegram bot in real-time.

Python で書かれた自動化ツールで、主要なバグバウンティプラットフォーム（HackerOne、Bugcrowdなど）を監視し、新しいプログラムや変更があった場合に Telegram ボットで通知します。

---

## 🌐 Supported Platforms / 対応プラットフォーム

- ✅ HackerOne
- ✅ Bugcrowd (top 4 programs, page content change detection)
- 🔜 Intigriti, YesWeHack (after login)

---

## 📦 Features / 特徴

| Feature                         | 説明 (Japanese)                                 |
|--------------------------------|--------------------------------------------------|
| 🕵️ Monitor new bounty programs | 新しいバグバウンティプログラムを検出             |
| 🔁 Check updates to companies  | 企業ページの更新（例：ドメイン変更）を監視       |
| ☁ Headless browser (Playwright)| サーバー上でも GUI なしで JavaScript をレンダリング |
| 📩 Telegram Notification        | 更新があったら Telegram でリアルタイム通知        |

---

## ⚙️ Installation / インストール方法

```bash
git clone https://github.com/YOUR_USERNAME/bugbounty-watcher.git
cd bugbounty-watcher
pip install -r requirements.txt
playwright install


📝 Configuration / 設定ファイル

Edit config.json like this:

{
  "tel_token": "YOUR_BOT_TOKEN",
  "tel_chatid": "YOUR_CHAT_ID"
}

※ Telegram Bot を作成し、@BotFather からトークンを取得してください。
▶️ Run / 実行方法
One-time run / 一度だけ実行

python main.py

Periodic check / 毎分チェック (自動ループ)

while True:
    run_bugcrowd_checker()
    run_hackerone_checker()
    time.sleep(60)

※ 実際の main.py にこのループを入れてください
📁 Project Structure / プロジェクト構成

bugbounty-watcher/
│
├── main.py
├── config.json
├── sites/
│   ├── hackerone.py
│   └── bugcrowd_playwright.py
├── storage/
│   └── company_pages/
├── utils/
│   └── telegram.py

📬 Telegram Bot Setup / Telegram ボットの使い方

    Open @BotFather

    Create a new bot → get the token

    Send any message to your bot

    Visit:

https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates

Get your chat_id from the response.
📌 Notes / 補足

    Bugcrowd uses Playwright to detect updates in company program pages, including JavaScript-rendered content.

    HackerOne fetches latest program activity via public JSON endpoint.

    Future updates will include login-based scraping for Intigriti, YesWeHack, etc.

👤 Author / 作者

Made by Shayan for automated bug bounty recon 🔍
自動バグバウンティ監視のために Shayan によって作成されました。

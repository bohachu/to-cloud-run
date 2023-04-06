# 自動化 Github 和 Vercel 部署

這是一個可以自動化 Github 和 Vercel 部署的網頁應用程式，只需要填寫一些參數，就可以在大約 25 秒內完成應用程式的部署。以下是使用說明：

## 使用步驟

1. 複製 Github 儲存庫的網址，例如：`https://github.com/bohachu/fastapi-vercel-005`
2. 在 Vercel 上創建一個新的項目，並選擇您的團隊
3. 在本網頁的表單中填寫以下參數：

- `github_access_token`：輸入您的 Github 存取權杖，您可以從此處創建一個新的存取權杖：https://github.com/settings/tokens/new
- `vercel_access_token`：輸入您的 Vercel 存取權杖，您可以在您的 Vercel 帳戶設置中找到這個存取權杖
- `source_url`：輸入您要從 Github 克隆的儲存庫網址，例如 `marcorichetta/fastapi-vercel`
- `target_name`：輸入您要將儲存庫克隆到本地計算機上的目標文件夾名稱
- `github_repo_url`：輸入您在 Github 上創建的儲存庫網址，例如 `https://github.com/bohachu/fastapi-vercel-005`
- `vercel_project_name`：輸入您在 Vercel 上創建的項目名稱，例如 `fastapi-vercel-005`
- `vercel_team_id`：輸入您的 Vercel 團隊 ID，您可以在您的 Vercel 帳戶設置中找到此 ID

4. 點擊“提交”按鈕，等待約 25 秒，系統會自動完成 Github 和 Vercel 的部署

## 注意事項

- 在使用本網頁之前，請確認您已經具備了足夠的 Github 和 Vercel 權限
- 在填寫 Github 和 Vercel 存取權杖時，請注意保密，不要將這些權杖洩露給其他人
- 在填寫參數時，請確保您輸入的是正確的信息，否則部署可能會失敗
- 如果您在使用過程中遇到任何問題，請聯繫我們的客服人員求助

## 技術細節

本網頁使用了以下技術：

- 前端框架：Bootstrap 4
- JavaScript 函式庫：jQuery、Popper.js、axios
- 後端框架：FastAPI

## 開發人員

- Bowen Chiu
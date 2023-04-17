import os

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import HTMLResponse

import git_clone
import vercel_deploy

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Params(BaseModel):
    github_access_token: str
    vercel_access_token: str
    source_url: str
    target_name: str
    github_repo_url: str
    vercel_project_name: str
    vercel_team_id: str


@app.post("/submit")
async def submit_params(params: Params):
    # 設定環境變數
    os.environ["GITHUB_ACCESS_TOKEN"] = params.github_access_token
    os.environ["VERCEL_ACCESS_TOKEN"] = params.vercel_access_token

    # 呼叫 git_clone.main()
    git_clone_response = git_clone.main(params.source_url, params.target_name)

    # 呼叫 vercel_deploy.main()
    vercel_deploy_response = vercel_deploy.main(params.github_repo_url, params.vercel_project_name,
                                                params.vercel_team_id)

    # 返回結果給前端
    return {
        "git_clone_response": git_clone_response,
        "vercel_deploy_response": vercel_deploy_response,
    }


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

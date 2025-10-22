# 贡献指南（Contribution Guidelines）

感谢你对 **Awesome ZJU Tools** 的关注与支持 🎉  
本项目旨在收集、整理并分享浙江大学生态圈中能提升学习、科研与生活效率的各类工具与资源。  
无论是脚本、插件、课程助手，还是模板、自动化脚本，都欢迎你的补充与分享！

> 💡 本项目遵循 [Contributor Code of Conduct](code-of-conduct.md)。  
> 参与贡献即表示你同意遵守其条款与行为规范。

---

## 提交前请检查以下内容

请确保你的 Pull Request 满足以下要求：

- 🧩 **条目规范**：  
  每个新增条目应包括项目名称、简要说明、来源链接，并归类到合适的分区（如“课程助手”、“模板与写作工具”等）。

- 💬 **描述清晰**：  
  请使用简洁、客观的描述，避免带有广告、主观评价或夸张措辞。

- 🧠 **内容相关**：  
  仅收录与浙大学习、科研、生活效率提升相关的资源。  
  不接受无关项目、非公开资源或违反使用条款的内容。
  链接最好有 Github 或 Chrome 应用商店链接，最好有较为明确的使用说明或指南。
  尽量推荐免费开源工具。

- ⚙️ **格式一致**：  
  - 使用 Markdown 表格格式添加项目；  
  - 确保链接有效；  
  - 保持排版与已有部分一致。

使用下面的工具进行检查：

- [huacnlee/autocorrect](https://github.com/huacnlee/autocorrect/)
- [DavidAnson/markdownlint-cli2-action](https://github.com/DavidAnson/markdownlint-cli2-action)
- [gaurav-nelson/github-action-markdown-link-check](https://github.com/gaurav-nelson/github-action-markdown-link-check)

```shell
autocorrect --fix README.md
markdownlint --fix README.md
markdown-link-check README.md
```

---

## 如何贡献

1. Fork 本仓库；
2. 新建一个分支（如 `add-new-tool`）；
3. 在合适分类中添加你的内容；
4. 提交 Pull Request。

如果只是建议添加某个项目，也可以直接开一个 Issue，格式如下：

```text
项目名称：
项目简介：
推荐理由：
项目链接：
所属分类：
```

## 致谢

感谢每一位为 ZJUer 共享工具与资源的贡献者！
你的分享让更多人受益，也让这份 Awesome 列表更加完善 🌟

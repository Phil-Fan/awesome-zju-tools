# AGENTS.md — awesome-zju-tools

浙大相关工具 Awesome 列表。内容几乎全部在根 `README.md` 分类表格中维护；GitHub Pages 壳 + `remote_theme`。

## 技术栈

| 项 | 规范 |
|----|------|
| 内容 | 根 `README.md` Markdown 表格 |
| 站点 | GitHub Pages（`remote_theme` 等，见仓内配置） |

## 目录

```text
awesome-zju-tools/
├── README.md                 # ★ 主内容
├── website/                  # Fumadocs + Next.js 站点
│   ├── content/docs/         # 分类 MDX（自 README 整理）
│   └── package.json
├── AGENTS.md
└── …
```

## 站点（Fumadocs）

```bash
cd website && pnpm install && pnpm dev
```

内容在 `website/content/docs/`，按 README 分类拆页；增删资源时同步更新 README 与对应 MDX。

## Conventional Commits

```text
docs(readme): add zju-scholar skill
docs(agents): remove stale pre-commit requirements
```

## Agent

- 增删资源以 README 表格行为单位；遵守贡献指南。

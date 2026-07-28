# Awesome ZJU Tools — Website

基于 [Fumadocs](https://fumadocs.dev) + Next.js 的文档站点，内容来自仓库根目录 `README.md`，按分类拆分至 `content/docs/`。

## 开发

```bash
cd website
pnpm install
pnpm dev
```

打开 http://localhost:3000

## 构建

```bash
pnpm build
pnpm start
```

## 目录

| 路径 | 说明 |
|------|------|
| `content/docs/` | MDX 文档（分类内容） |
| `app/` | Next.js App Router |
| `lib/` | 站点配置与 source loader |
| `source.config.ts` | fumadocs-mdx 配置 |

## 内容维护

优先在根目录 `README.md` 维护工具列表；本站 `content/docs/` 为分类展示副本。新增分类时请同步更新两侧内容。

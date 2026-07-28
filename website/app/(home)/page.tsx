import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="mx-auto flex w-full max-w-2xl flex-1 flex-col items-center justify-center px-6 py-24 text-center">
      <h1 className="mb-4 text-4xl font-bold tracking-tight sm:text-5xl">
        Awesome ZJU Tools
      </h1>
      <p className="mb-8 text-base text-fd-muted-foreground sm:text-lg">
        浙江大学生态圈中提高学习、科研与生活效率的工具、脚本、资源与模版合集
      </p>
      <div className="flex flex-wrap items-center justify-center gap-3">
        <Link
          href="/docs/learning"
          className="rounded-full bg-fd-primary px-5 py-2.5 text-sm font-medium text-fd-primary-foreground transition-opacity hover:opacity-90"
        >
          浏览工具
        </Link>
        <a
          href="https://github.com/Phil-Fan/awesome-zju-tools"
          target="_blank"
          rel="noreferrer"
          className="rounded-full border px-5 py-2.5 text-sm font-medium transition-colors hover:bg-fd-accent"
        >
          GitHub
        </a>
      </div>
    </main>
  );
}

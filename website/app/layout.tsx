import { RootProvider } from 'fumadocs-ui/provider/next';
import './global.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  metadataBase: new URL('https://zjutools.top'),
  title: {
    default: 'Awesome ZJU Tools',
    template: '%s | Awesome ZJU Tools',
  },
  description:
    '浙江大学生态圈中提高学习、科研与生活效率的工具、脚本、资源与模版合集',
};

export default function Layout({ children }: LayoutProps<'/'>) {
  return (
    <html lang="zh-CN" suppressHydrationWarning>
      <body className="flex min-h-screen flex-col font-sans antialiased">
        <RootProvider>{children}</RootProvider>
      </body>
    </html>
  );
}

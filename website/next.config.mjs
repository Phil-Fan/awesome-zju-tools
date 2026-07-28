import { createMDX } from 'fumadocs-mdx/next';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const withMDX = createMDX();
const root = path.dirname(fileURLToPath(import.meta.url));

/** @type {import('next').NextConfig} */
const config = {
  output: 'export',
  reactStrictMode: true,
  turbopack: {
    root,
  },
  images: {
    unoptimized: true,
    // contrib.rocks / shields 返回 SVG badge，需放行
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'stg.contrib.rocks',
      },
      {
        protocol: 'https',
        hostname: 'contrib.rocks',
      },
      {
        protocol: 'https',
        hostname: 'img.shields.io',
      },
      {
        protocol: 'https',
        hostname: 'awesome.re',
      },
    ],
  },
};

export default withMDX(config);

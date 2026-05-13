import { defineConfig } from 'vite';
import fs from 'node:fs';
import path from 'node:path';
import { URL as NodeURL } from 'node:url';

function body(req) {
  return new Promise(resolve => {
    let s = '';
    req.on('data', c => { s += c; });
    req.on('end', () => resolve(JSON.parse(s)));
  });
}

function json(res, data, status = 200) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(data));
}

function makeTemplate(number, title) {
  return `<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Занятие ${number} - ${title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimal-ui">
    <link rel="stylesheet" href="/utils/css/reveal.css">
    <link rel="stylesheet" href="/utils/lib/css/animate.css">
    <link rel="stylesheet" href="/utils/css/theme/night.css" id="theme">
    <link rel="stylesheet" href="/utils/lib/css/zenburn.css">
    <link rel="stylesheet" href="/utils/css/custom-base.css">
    <link rel="stylesheet" href="css-custom/custom.css">
    <script>
        var link = document.createElement('link');
        link.rel = 'stylesheet'; link.type = 'text/css';
        link.href = window.location.search.match(/print-pdf/gi) ? '/utils/css/print/pdf.css' : '/utils/css/print/paper.css';
        document.getElementsByTagName('head')[0].appendChild(link);
    <\/script>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section style="font-size: 70px; height: 100%; width: 100%">
                <div class="lesson-time">0</div>
                <div class="fragment">
                    <h1 class="animated" style="font-size: 1.6em;">${title}</h1>
                    <p style="text-align: center; font-size: 0.4em; opacity: 0.5;">Занятие ${number}</p>
                </div>
            </section>
        </div>
    </div>
    <script src="/utils/lib/js/head.min.js"><\/script>
    <script src="/utils/js/reveal.js"><\/script>
    <script>
        Reveal.initialize({
            controls: true, progress: true, history: true, center: true,
            transition: 'fade', transitionSpeed: 'fast',
            dependencies: [
                { src: '/utils/lib/js/classList.js', condition: function() { return !document.body.classList; } },
                { src: '/utils/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                { src: '/utils/plugin/zoom-js/zoom.js', async: true },
                { src: '/utils/plugin/notes/notes.js', async: true }
            ]
        });
        Reveal.configure({ slideNumber: 'c/t' });
    <\/script>
</body>
</html>`;
}

export default defineConfig({
  root: '.',
  server: {
    host: '0.0.0.0',
    port: 8001,
    open: '/?view_all=true',
  },
  plugins: [
    {
      name: 'admin-api',
      configureServer(server) {
        const cwd = process.cwd();

        // POST /api/save-lessons
        server.middlewares.use('/api/save-lessons', async (req, res) => {
          if (req.method !== 'POST') { json(res, {}, 405); return; }
          try {
            const data = await body(req);
            fs.writeFileSync(path.join(cwd, 'lessons.json'), JSON.stringify(data, null, 2));
            json(res, { ok: true });
          } catch (e) { json(res, { error: e.message }, 500); }
        });

        // GET /api/check-dir?path=lessons/15-sorting-n2
        server.middlewares.use('/api/check-dir', (req, res) => {
          const u = new NodeURL(req.url, 'http://localhost');
          const dirPath = u.searchParams.get('path') || '';
          const full = path.join(cwd, dirPath);
          const exists = fs.existsSync(full) && fs.statSync(full).isDirectory();
          json(res, { exists });
        });

        // POST /api/rename-dir  { from, to }
        server.middlewares.use('/api/rename-dir', async (req, res) => {
          if (req.method !== 'POST') { json(res, {}, 405); return; }
          try {
            const { from, to } = await body(req);
            fs.renameSync(path.join(cwd, from), path.join(cwd, to));
            json(res, { ok: true });
          } catch (e) { json(res, { error: e.message }, 500); }
        });

        // POST /api/create-dir  { dirPath, number, title }
        server.middlewares.use('/api/create-dir', async (req, res) => {
          if (req.method !== 'POST') { json(res, {}, 405); return; }
          try {
            const { dirPath, number, title } = await body(req);
            const full = path.join(cwd, dirPath);
            fs.mkdirSync(path.join(full, 'css-custom'), { recursive: true });
            fs.writeFileSync(path.join(full, 'css-custom', 'custom.css'), `/* Занятие ${number} - ${title} */\n`);
            fs.writeFileSync(path.join(full, 'index.html'), makeTemplate(number, title));
            json(res, { ok: true });
          } catch (e) { json(res, { error: e.message }, 500); }
        });
      },
    },
  ],
});

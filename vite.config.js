import { defineConfig } from 'vite';

export default defineConfig({
  root: '.',
  server: {
    port: 8001,
    open: '/?view_all=true',
  },
});

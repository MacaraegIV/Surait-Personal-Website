import { defineConfig } from 'astro/config';

// GitHub supplies this during deployment; local development stays at /.
const [owner, repository] = (process.env.GITHUB_REPOSITORY || '').split('/');
const isUserSite = repository?.toLowerCase() === `${owner?.toLowerCase()}.github.io`;

export default defineConfig({
  site: owner ? `https://${owner}.github.io` : 'https://example.com',
  base: repository && !isUserSite ? `/${repository}` : '/',
  output: 'static',
});

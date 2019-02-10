const path = require('path');
config = {
      baseUrl: '/static/dist',
      assetsDir: './',
      outputDir: './dist',
      pages: {
        app: {
          entry: 'src/main.js',
          template: 'public/index.html',
          filename:
            path.resolve(
              '../templates', 'index.html'),
          title: 'Wizybit'
        }
      }
    };

module.exports = config;
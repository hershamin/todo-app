// Karma configuration
// Generated on Tue Feb 20 2018 22:05:13 GMT-0600 (CST)

module.exports = function(config) {
  config.set({

    // base path that will be used to resolve all patterns (eg. files, exclude)
    basePath: '',


    // frameworks to use
    // available frameworks: https://npmjs.org/browse/keyword/karma-adapter
    frameworks: ['jasmine'],

   
    // list of files / patterns to load in the browser
    files: [
      'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular-cookies.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/1.0.3/angular-ui-router.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular-animate.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular-aria.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular-messages.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/angular-material/1.1.6/angular-material.min.js',
      'tests/angular-mocks.js',
      'app.js',
      '*/*.js',
      'tests/*/*spec.js'
    ],


    // list of files / patterns to exclude
    exclude: [],


    // preprocess matching files before serving them to the browser
    // available preprocessors: https://npmjs.org/browse/keyword/karma-preprocessor
    preprocessors: {
    },


    // test results reporter to use
    // possible values: 'dots', 'progress'
    // available reporters: https://npmjs.org/browse/keyword/karma-reporter
    reporters: ['progress'],


    // web server port
    port: 9876,


    // enable / disable colors in the output (reporters and logs)
    colors: true,


    // level of logging
    // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
    logLevel: config.LOG_INFO,


    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: true,


    // start these browsers
    // available browser launchers: https://npmjs.org/browse/keyword/karma-launcher
    browsers: ['Chrome'],


    // Continuous Integration mode
    // if true, Karma captures browsers, runs the tests and exits
    singleRun: false,

    // Concurrency level
    // how many browser should be started simultaneous
    concurrency: Infinity
  })
}

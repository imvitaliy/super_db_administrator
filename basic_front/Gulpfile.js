var gulp      = require('gulp');
var browserSync = require('browser-sync');
var sass = require('gulp-sass');
var prefix = require('gulp-autoprefixer');
var cp = require('child_process');
var gutil = require('gulp-util'),
    jshint = require('gulp-jshint'),
    browserify = require('gulp-browserify'),
    concat = require('gulp-concat'),
    clean = require('gulp-clean');


gulp.task('views', function() {
  gulp.src('./src/html/index.html')
  .pipe(gulp.dest('app/'))
  .pipe(browserSync.reload({stream:true}));


  gulp.src('./src/html/views/**/*')
  .pipe(gulp.dest('app/views/'))
  .pipe(browserSync.reload({stream:true}));
});

gulp.task('images', function() {
  gulp.src('./src/img/**/*')
  .pipe(gulp.dest('app/img/'))
  .pipe(browserSync.reload({stream:true}));
});

// JSHint task
gulp.task('lint', function() {
  gulp.src('./src/js/*.js')
  .pipe(jshint())
  // You can look into pretty reporters as well, but that's another story
  .pipe(jshint.reporter('default'));
});

// Browserify task
gulp.task('browserify', function() {
  // Single point of entry (make sure not to src ALL your files, browserify will figure it out for you)
  gulp.src(['src/js/main.js'])
  .pipe(browserify({
    insertGlobals: true,
    debug: true
  }))
  // Bundle to a single file
  .pipe(concat('main.js'))
  // // Output it to our dist folder
   .pipe(browserSync.reload({stream:true}))
   .pipe(gulp.dest('app/js'));
  //gulp.src('./src/js/**/*')
  //.pipe(gulp.dest('app/js/'))
  //.pipe(browserSync.reload({stream:true}));
});

// Browser Sync
gulp.task('browser-sync', ['sass'], function(){
  browserSync({
    server: {
      baseDir: './app/'
    }
  })
});

gulp.task('sass', function(){
  return gulp.src('src/sass/main.sass')
    .pipe(sass({}))
    .pipe(prefix(['> 1%'], {cascade: false}))
    .pipe(gulp.dest('app/css/'))
    .pipe(browserSync.reload({stream:true}))
    .pipe(gulp.dest('app/css'));
});


gulp.task('watch', function (){
  gulp.watch('src/html/**/*.html', ['views']);
  gulp.watch('src/img/**/*.*', ['images']);
  gulp.watch('src/sass/**/*.sass', ['sass']);
  gulp.watch(['src/js/**/*.js'],['lint', 'browserify']);
});

gulp.task('default', ['views', 'images', 'browser-sync', 'lint', 'browserify', 'watch']);

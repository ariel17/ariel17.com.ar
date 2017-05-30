var gulp = require('gulp');
var less = require('gulp-less');
var minify = require('gulp-minify');
var browserSync = require('browser-sync').create();

var files = {
    less: [
      './bower_components/bootstrap-less/less/bootstrap.less',
      './assets/less/**/*.less'
    ],
    html: [
        'index.html'
    ],
    javascript: [
        './bower_components/jquery/dist/jquery.js',
        './bower_components/bootstrap-less/js/collapse.js'
    ],
    images: [
        './assets/img/**/*'
    ]
};


gulp.task('less', function () {
  return gulp.src(files.less)
    .pipe(less())
    .pipe(gulp.dest('./public/css'));
});

gulp.task('js', function() {
  gulp.src(files.javascript)
    .pipe(minify({
        ext:{
            src:'.js',
            min:'.min.js'
        },
        ignoreFiles: ['min.js'],
        noSource: true
    }))
    .pipe(gulp.dest('public/js'));
});

gulp.task('images', function() {
  gulp.src(files.images)
    .pipe(gulp.dest('public/img'));
});

gulp.task('sync', function() {
    gulp.watch(files.less, ['less']).on("change", browserSync.reload);
    gulp.watch(files.javascript, ['js']).on("change", browserSync.reload);
    gulp.watch(files.images, ['images']).on("change", browserSync.reload);
    gulp.watch(files.html).on("change", browserSync.reload);

    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
});

gulp.task('default', ['less', 'js', 'images', 'sync']);

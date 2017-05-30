var gulp = require('gulp');
var less = require('gulp-less');
var browserSync = require('browser-sync').create();

gulp.task('less', function () {
  return gulp.src('./assets/less/**/*.less')
    .pipe(less())
    .pipe(gulp.dest('./public/css'));
});

gulp.task('sync', function() {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
});

gulp.watch('./assets/less/**/*.less', ['less']);

gulp.task('default', ['less', 'sync']);

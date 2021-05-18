//gulp stuff
const {src, dest, watch, parallel, series} = require('gulp');
const gulp = require("gulp");

//scss stuff
const scss = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');

//general stuff
const concat = require('gulp-concat');

//browser stuff
const browserSync = require('browser-sync').create();
const reload = browserSync.reload;
const exec = require('child_process').exec;

//js stuff
const uglify = require('gulp-uglify-es').default;
const plumber = require('gulp-plumber');
const babel = require('gulp-babel');

//images stuff
// const imagemin = require('gulp-imagemin');

//build stuff
const del = require('del');


// function browser_sync() {
//     browserSync.init({
//         server: {
//             baseDir: 'app/'
//         },
//         browser: 'chrome',
//         notify: false
//     });
// }

function cleanDist() {
    return del('dist')
}

// Minimizing all images
// function images() {
//     return src('app/images/**/*')
//         .pipe(imagemin([
//             imagemin.gifsicle({ interlaced: true }),
//             imagemin.mozjpeg({ quality: 75, progressive: true }),
//             imagemin.optipng({ optimizationLevel: 5 }),
//             imagemin.svgo({
//                 plugins: [
//                     { removeViewBox: true },
//                     { cleanupIDs: false }
//                 ]
//             })
//         ]))
//         .pipe(dest('dist/images'))   //way to save minimized images
// }

//Creating minimized file Js
function scripts() {
    return src([
        'node_modules/jquery/dist/jquery.slim.js',
        'node_modules/bootstrap/dist/js/bootstrap.bundle.js',
        'node_modules/bootstrap/dist/js/bootstrap.js',
        'app/static/js/main_script.js',
        'app/static/js/korniichuk_scripts/app_slider.js'
    ])
        .pipe(concat('main_script.min.js'))
        .pipe(plumber())
        .pipe(babel({
            presets: ['@babel/preset-env'],
            plugins: ["@babel/plugin-proposal-class-properties"]
        }))
        // .pipe(uglify())
        .pipe(gulp.dest('app/static/js/minimized'))
        .pipe(browserSync.reload({
            stream: true
        }));
}


// Convert scss into css
function styles() {
    return src([
        'node_modules/bootstrap/dist/css/bootstrap-reboot.css',
        'node_modules/bootstrap/dist/css/bootstrap-grid.css',
        'node_modules/bootstrap/dist/css/bootstrap.css',
        'app/static/scss/style.scss'
    ])
        .pipe(scss({outputStyle: 'expanded'}))
        .pipe(concat('main_style.min.css'))
        .pipe(autoprefixer({
            overrideBrowserslist: ['last 10 version'],
            grid: true
        }))
        .pipe(gulp.dest('app/static/css'))
        .pipe(browserSync.reload({
            stream: true
        }));
}

// Building files into "dist" folder
function build() {
    return src([
        'app/css/style.min.css',
        'app/fonts/**/*',
        'app/js/main.min.js',
        'app/*.html'
    ], {base: 'app'})
        .pipe(dest(`dist`))
}

function run_server() {
    let proc = exec('python manage.py runserver');
}


function browser_sync() {
    browserSync.init({
        browser: 'chrome',
        notify: false,
        port: 8000,
        proxy: 'localhost:8000'
    });
    run_server();
}

// Watching for changes
function watching() {
    watch(['app/static/scss/**/*.scss'], styles).on('change', reload);        //command to watch for all files which have ending in .scss
    watch(['app/static/js/**/*.js', '!app/static/js/minimized/main_script.min.js'], scripts).on('change', reload);//watching for all js files except main.min.js
    watch(['app/templates/**/*.html']).on('change', reload);//refresh browser if html has change
}

exports.styles = styles;
// Available command "gulp styles" to convert scss into css

exports.watching = watching;
// Available command "gulp watching" to Auto convert scss into css

exports.browser_sync = browser_sync;
// Available command "gulp browser_sync" to Auto refresh browser

// Available command "gulp scripts" to unite js files in one
exports.scripts = scripts;

// Available command "gulp images" to minimize images
// exports.images = images;

// Available command "gulp cleanDist" to clean "dist" folder
exports.cleanDist = series(cleanDist, build);

// Available command "gulp build" to build project into "dist" folder
// exports.build = series(cleanDist, build);


exports.default = parallel(styles, scripts, watching, browser_sync);
// Available command "gulp" to Auto refresh browser and Auto convert scss into css, unite js files



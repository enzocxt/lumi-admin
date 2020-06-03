# Lumi-Admin-Front

> This is the front-end part of the Content Manage System project for website [Luminocity](http://luminocity.cn/).  
> The back-end part comes [here](https://github.com/enzocxt/Lumi-Admin-Back).  
> I try to learn web development skills by this project, although *Luminocity* does not need many of the functions.  

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).


## API
base URL : http://localhost:8088

Authentication APIs
* `/api/login`
* `/api/register`

Admin APIs
* `/api/admin/menu`
* `/api/admin/user`
* `/api/admin/role`
* `/api/admin/user/status`

Article APIs
* `/api/article/<int:id>`
* `/api/article/<int:per_page>/<int:page>`

Book APIs
* `/api/books`
* `[POST] /api/book`
* `/api/book/<int:id>`
* `[POST]: /api/delete`
* `[POST]: /api/search`
* `/api/category/<int:cid>/books`

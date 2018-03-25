FROM nginx

ADD ["./index/index.html", "/usr/share/nginx/html/"]
ADD ["./index/public", "/usr/share/nginx/html/public"]
ADD ["./blog/output/blog", "/usr/share/nginx/html/blog"]
ADD ["./blog/output/projects", "/usr/share/nginx/html/projects"]
ADD ["./blog/output/galleries", "/usr/share/nginx/html/galleries"]
ADD ["./blog/output/assets", "/usr/share/nginx/html/assets"]

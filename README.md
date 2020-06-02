# ariel17.com.ar

The [ariel17.com.ar][1] web site content. This is a personal page where I talk
about myself to fatigue. There is a humble blog too :)

The site is powered by [Nikola][2] static web generator.

![Screenshot](./screenshot.png)

## Building image

```bash
$ docker build -t ariel17/www .
$ docker run -p 8080:80 ariel17/www
```

[1]: http://ariel17.com.ar/
[2]: http://getnikola.com/

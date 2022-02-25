Учебный проект одностраничный сайт портфолио
http://test-portfolio.quiet-cmd.tk/

### Инструкция для установки на ubuntu 20.04

### Обновление пакетов

```bash
sudo apt update
sudo apt upgrade
```

### Устанавливаем HTTP-сервер и открываем порт 80

```bash
sudo apt install nginx

sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
sudo netfilter-persistent save
```

### Добавляем каталог сайта
В каталог сайта нужно поместить index.html и папку static

```bash
sudo mkdir -p /var/www/your_domain/html
```

### Добавляем конфиг

```bash
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/your_domain
```

### Редактируем конфиг

```bash
sudo nano /etc/nginx/sites-available/your_domain
```

server {
        listen 80;
        listen [::]:80;

        root /var/www/your_domain/html;

        index index.html index.htm index.nginx-debian.html;

        server_name your_domain;
        location / {
            try_files $uri $uri/ =404;
        }
}

### активация виртуальных хостов и перезапуск Nginx

```bash
sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
sudo service nginx restart
```
